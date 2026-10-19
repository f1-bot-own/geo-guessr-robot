"""
Admin Authentication & Security Module for GeoGuru & GeoGuessr Web Dashboard.
Includes 2FA OTP generation and rate-limiting / IP lockout,
Telegram WebApp HMAC-SHA256 validation, JWT session token lifecycle,
and @require_admin route decorators.
"""

import time
import json
import hmac
import hashlib
import secrets
import base64
import logging
from urllib.parse import parse_qsl, unquote
from typing import Optional, Dict, Any, Callable
from functools import wraps
from aiohttp import web

import config

logger = logging.getLogger("AdminAuth")

# In-memory stores (persists across sessions during process uptime)
# OTP store: user_id -> {"code": "123456", "expires_at": float, "attempts": int}
_otp_store: Dict[int, Dict[str, Any]] = {}

# Session store: token -> {"user_id": int, "user": dict, "expires_at": float}
_sessions: Dict[str, Dict[str, Any]] = {}

# IP Rate-limit / lockout store: ip_address -> {"failures": int, "locked_until": float}
_ip_lockouts: Dict[str, Dict[str, Any]] = {}

# Revoked tokens set
_revoked_tokens: set[str] = set()

# Constants
OTP_EXPIRY_SECONDS = 300  # 5 minutes
SESSION_EXPIRY_SECONDS = 86400 * 7  # 7 days
MAX_FAILED_ATTEMPTS = 5
LOCKOUT_DURATION_SECONDS = 900  # 15 minutes


def get_client_ip(request: web.Request) -> str:
    """Extract real client IP considering forward headers."""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip.strip()
    peername = request.transport.get_extra_info("peername") if request.transport else None
    if peername:
        return str(peername[0])
    return "127.0.0.1"


# ----------------- IP Rate Limiter & Lockout -----------------

def record_login_attempt(ip: str, success: bool) -> None:
    """Record login attempt result for IP. Blocks IP for 15 min after 5 consecutive failures."""
    clean_ip = str(ip).strip()
    if not clean_ip:
        return

    if success:
        _ip_lockouts.pop(clean_ip, None)
        return

    now = time.time()
    record = _ip_lockouts.setdefault(clean_ip, {"failures": 0, "locked_until": 0})
    record["failures"] += 1
    if record["failures"] >= MAX_FAILED_ATTEMPTS:
        record["locked_until"] = now + LOCKOUT_DURATION_SECONDS
        logger.warning(f"IP {clean_ip} locked out until {record['locked_until']} due to repeated failures.")


def is_ip_locked(ip: str) -> bool:
    """Check if the given IP is currently locked out."""
    clean_ip = str(ip).strip()
    record = _ip_lockouts.get(clean_ip)
    if not record:
        return False
    locked_until = record.get("locked_until", 0)
    if time.time() < locked_until:
        return True
    # Lockout expired, clean up
    if locked_until > 0:
        _ip_lockouts.pop(clean_ip, None)
    return False


def record_failed_attempt(ip: str, user_id: Optional[int] = None) -> None:
    """Backward compatibility wrapper for recording failed attempt."""
    record_login_attempt(ip, success=False)


def clear_ip_attempts(ip: str) -> None:
    """Backward compatibility wrapper for clearing failed attempts."""
    record_login_attempt(ip, success=True)


# ----------------- Admin Authorization & Password -----------------

def is_admin(user_id: Optional[int]) -> bool:
    """Check whether user_id is an authorized administrator."""
    return config.is_admin(user_id)


def verify_master_password(password: str) -> bool:
    """Verify master password against ADMIN_MASTER_PASSWORD."""
    master = getattr(config, "ADMIN_MASTER_PASSWORD", "")
    if not master or not password:
        return False
    return hmac.compare_digest(str(master).strip(), str(password).strip())


# ----------------- 2FA OTP Storage -----------------

def create_otp(user_id: int) -> str:
    """Generate a cryptographically secure 6-digit OTP code valid for 5 min (max 3 attempts)."""
    code = f"{secrets.randbelow(900000) + 100000:06d}"
    _otp_store[int(user_id)] = {
        "code": code,
        "expires_at": time.time() + OTP_EXPIRY_SECONDS,
        "attempts": 0,
    }
    logger.info(f"Generated 2FA OTP for admin user {user_id} (expires in {OTP_EXPIRY_SECONDS}s)")
    return code


generate_otp = create_otp  # Backward compatibility alias


def verify_otp(user_id: int, code: str) -> bool:
    """
    Verify submitted 6-digit OTP code.
    Maximum 3 attempts permitted.
    Invalidates code on success, expiration, or reaching max attempts.
    """
    uid = int(user_id)
    record = _otp_store.get(uid)
    if not record:
        return False

    now = time.time()
    if now > record.get("expires_at", 0):
        _otp_store.pop(uid, None)
        return False

    record["attempts"] += 1
    stored_code = str(record.get("code", "")).strip()
    clean_sub = str(code).strip()

    if hmac.compare_digest(stored_code, clean_sub):
        _otp_store.pop(uid, None)
        return True

    if record["attempts"] >= 3:
        _otp_store.pop(uid, None)
        logger.warning(f"OTP attempts exceeded 3 for user {uid}; code invalidated.")

    return False


# ----------------- JWT & Session Token Lifecycle -----------------

def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def _b64url_decode(data: str) -> bytes:
    padding = len(data) % 4
    if padding != 0:
        data += "=" * (4 - padding)
    return base64.urlsafe_b64decode(data.encode("utf-8"))


def create_session_token(user_id: int, expires_in: int = SESSION_EXPIRY_SECONDS, extra_claims: Optional[Dict[str, Any]] = None) -> str:
    """Generate RFC 7519 compliant HS256 JWT session token."""
    header = {"alg": "HS256", "typ": "JWT"}
    now = int(time.time())
    payload: Dict[str, Any] = {
        "user_id": int(user_id),
        "iat": now,
        "exp": now + expires_in,
    }
    if extra_claims:
        payload.update(extra_claims)

    secret = getattr(config, "ADMIN_JWT_SECRET", "geoguru-super-secret-admin-jwt-token-key-2026")
    header_part = _b64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_part = _b64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    msg = f"{header_part}.{payload_part}".encode("utf-8")
    sig = hmac.new(secret.encode("utf-8"), msg, hashlib.sha256).digest()
    sig_part = _b64url_encode(sig)

    token = f"{header_part}.{payload_part}.{sig_part}"
    _sessions[token] = {
        "user_id": int(user_id),
        "user": payload,
        "created_at": now,
        "expires_at": now + expires_in,
    }
    return token


_revoked_tokens: set[str] = set()

def verify_session_token(token: str) -> Optional[Dict[str, Any]]:
    """Verify HS256 JWT session token or opaque session token."""
    if not token or not isinstance(token, str) or token in _revoked_tokens:
        return None

    secret = getattr(config, "ADMIN_JWT_SECRET", "geoguru-super-secret-admin-jwt-token-key-2026")
    parts = token.strip().split(".")
    if len(parts) == 3:
        header_part, payload_part, sig_part = parts
        try:
            msg = f"{header_part}.{payload_part}".encode("utf-8")
            expected_sig = hmac.new(secret.encode("utf-8"), msg, hashlib.sha256).digest()
            provided_sig = _b64url_decode(sig_part)
            if not hmac.compare_digest(expected_sig, provided_sig):
                return None

            payload_bytes = _b64url_decode(payload_part)
            payload = json.loads(payload_bytes.decode("utf-8"))
            if not isinstance(payload, dict):
                return None

            exp = payload.get("exp")
            if exp is not None and time.time() > float(exp):
                return None

            user_id = payload.get("user_id")
            if not user_id:
                return None

            return payload
        except Exception as e:
            logger.debug(f"JWT verification error: {e}")
            return None

    # Fallback to opaque token store
    session = _sessions.get(token)
    if session:
        if time.time() > session.get("expires_at", 0):
            _sessions.pop(token, None)
            return None
        return session.get("user") or {"user_id": session.get("user_id")}

    return None


def create_session(user_id: int, user_data: Optional[Dict[str, Any]] = None) -> str:
    """Generate session token and record user claims."""
    return create_session_token(user_id, extra_claims=user_data)


def validate_session(token: Optional[str]) -> Optional[Dict[str, Any]]:
    """Validate token and return session data if still active."""
    if not token or token in _revoked_tokens:
        return None
    session_data = verify_session_token(token)
    if session_data:
        return {
            "user_id": session_data.get("user_id"),
            "user": session_data,
            "expires_at": session_data.get("exp", 0)
        }
    return None


def delete_session(token: Optional[str]) -> None:
    """Remove session from store and mark as revoked."""
    if token:
        _sessions.pop(token, None)
        _revoked_tokens.add(token)


# ----------------- Telegram WebApp HMAC-SHA256 Validator -----------------

def validate_telegram_init_data(init_data: str, bot_token: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Validate Telegram Mini App initData signature using HMAC-SHA256 according to Telegram spec.
    Returns parsed dictionary of parameters (with user parsed as dict and user fields accessible) if valid, else None.
    """
    token = bot_token or config.BOT_TOKEN
    if not init_data or not token:
        return None

    try:
        parsed_items = dict(parse_qsl(init_data, keep_blank_values=True))
        received_hash = parsed_items.pop("hash", None)
        if not received_hash:
            return None

        # Build data check string from sorted key-value pairs separated by \n
        data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed_items.items()))

        # Secret key: HMAC-SHA256 of bot_token with key "WebAppData"
        secret_key = hmac.new(b"WebAppData", token.strip().encode("utf-8"), hashlib.sha256).digest()
        calculated_hash = hmac.new(secret_key, data_check_string.encode("utf-8"), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(calculated_hash, received_hash):
            return None

        result = dict(parsed_items)
        raw_user = parsed_items.get("user")
        if raw_user:
            try:
                user_obj = json.loads(unquote(raw_user)) if isinstance(raw_user, str) else raw_user
                result["user"] = user_obj
                if isinstance(user_obj, dict):
                    for k, v in user_obj.items():
                        if k not in result:
                            result[k] = v
            except Exception:
                pass
        return result
    except Exception as exc:
        logger.warning(f"Failed to validate Telegram WebApp initData: {exc}")
        return None


verify_telegram_webapp = validate_telegram_init_data  # Backward compatibility alias



# ----------------- Bot OTP Dispatch Helper -----------------

async def send_admin_otp(bot, admin_id: int, otp_code: str) -> bool:
    """Send 2FA OTP to admin's Telegram chat."""
    text = (
        "🔐 <b>GeoGuru Admin 2FA Verification Code</b>\n\n"
        f"Your one-time code: <code>{otp_code}</code>\n"
        "⏳ Expires in: 5 minutes.\n\n"
        "⚠️ Do not share this code with anyone!"
    )
    if bot:
        try:
            await bot.send_message(chat_id=admin_id, text=text, parse_mode="HTML")
            return True
        except Exception as exc:
            logger.warning(f"Could not send OTP via bot to {admin_id}: {exc}")

    # Fallback direct telegram API call
    if config.BOT_TOKEN and ":" in config.BOT_TOKEN:
        try:
            import aiohttp
            url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"
            payload = {"chat_id": admin_id, "text": text, "parse_mode": "HTML"}
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, timeout=5) as resp:
                    data = await resp.json()
                    return bool(data.get("ok"))
        except Exception as e:
            logger.warning(f"Direct bot API send failed: {e}")
    return False


# ----------------- Route Middleware / Decorator -----------------

def check_request_admin_auth(request: Optional[web.Request]) -> Optional[Dict[str, Any]]:
    """
    Check whether request has valid admin credentials from cookie, Authorization header, or query.
    Returns session_data dict (augmented with user_id and token) if authorized, otherwise None.
    """
    if request is None:
        return None

    token = request.cookies.get("admin_session")
    if not token:
        token = request.cookies.get("session_token")
    if not token:
        token = request.cookies.get("token")
    if not token:
        auth_header = request.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:].strip()
        elif auth_header:
            token = auth_header.strip()
    if not token:
        token = request.query.get("token")

    if not token:
        return None

    session_data = verify_session_token(token)
    if not session_data:
        legacy_session = validate_session(token)
        if legacy_session:
            session_data = legacy_session.get("user") or {"user_id": legacy_session.get("user_id")}

    user_id = None
    if isinstance(session_data, dict):
        user_id = session_data.get("user_id")
        if not user_id and "user" in session_data and isinstance(session_data["user"], dict):
            user_id = session_data["user"].get("user_id") or session_data["user"].get("id")

    if not session_data or not user_id:
        return None

    if not config.is_admin(user_id):
        return None

    result = dict(session_data)
    result["user_id"] = int(user_id)
    result["_token"] = token
    return result


def require_admin(handler: Callable):
    """
    Route decorator ensuring request has valid admin credentials.
    Checks session cookie, Authorization header Bearer <token>, and ?token query parameter.
    Injects request['admin_user'] and request['admin_token'] on success.
    """
    @wraps(handler)
    async def wrapper(*args, **kwargs):
        request: Optional[web.Request] = None
        for arg in args:
            if isinstance(arg, web.Request):
                request = arg
                break
        if request is None and "request" in kwargs:
            request = kwargs["request"]
        if request is None and len(args) > 0 and hasattr(args[0], "headers"):
            request = args[0]

        if request is None:
            return web.json_response(
                {"ok": False, "error": "Internal error: Request context missing."},
                status=500
            )

        token = request.cookies.get("admin_session")
        if not token:
            token = request.cookies.get("session_token")
        if not token:
            token = request.cookies.get("token")
        if not token:
            auth_header = request.headers.get("Authorization", "")
            if auth_header.startswith("Bearer "):
                token = auth_header[7:].strip()
            elif auth_header:
                token = auth_header.strip()
        if not token:
            token = request.query.get("token")

        if not token:
            return web.json_response(
                {"ok": False, "error": "Unauthorized: Missing authentication token."},
                status=401
            )

        session_data = verify_session_token(token)
        if not session_data:
            legacy_session = validate_session(token)
            if legacy_session:
                session_data = legacy_session.get("user") or {"user_id": legacy_session.get("user_id")}

        user_id = None
        if isinstance(session_data, dict):
            user_id = session_data.get("user_id")
            if not user_id and "user" in session_data and isinstance(session_data["user"], dict):
                user_id = session_data["user"].get("user_id") or session_data["user"].get("id")

        if not session_data or not user_id:
            return web.json_response(
                {"ok": False, "error": "Unauthorized: Admin authentication required."},
                status=401
            )

        if not config.is_admin(user_id):
            return web.json_response(
                {"ok": False, "error": "Forbidden: Admin privileges required."},
                status=403
            )

        request["admin_user"] = session_data
        request["admin_token"] = token
        request["admin_user_id"] = user_id
        return await handler(*args, **kwargs)

    return wrapper


def reset_ip_lockouts() -> None:
    """Clear all IP lockout records (useful for test isolation)."""
    _ip_lockouts.clear()


def reset_otp_store() -> None:
    """Clear all OTP records (useful for test isolation)."""
    _otp_store.clear()


def reset_session_store() -> None:
    """Clear all session records (useful for test isolation)."""
    _sessions.clear()
    _revoked_tokens.clear()

