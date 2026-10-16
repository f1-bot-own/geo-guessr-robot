"""
Embedded Web Server for GeoGuessr Telegram Mini App.
Serves static WebApp files and provides REST API endpoints.
Runs seamlessly alongside aiogram bot polling.
"""

import os
import json
import logging
from pathlib import Path
from typing import Optional
from aiohttp import web

logger = logging.getLogger("WebAppServer")

STATIC_DIR = Path(__file__).resolve().parent

MAX_MINIAPP_SCORE = 25000

async def index_handler(request: web.Request) -> web.Response:
    """Serve the Mini App main HTML entry point."""
    html_file = STATIC_DIR / "index.html"
    if html_file.is_file():
        return web.FileResponse(html_file)
    return web.Response(text="GeoGuessr Mini App index.html not found", status=404)

async def health_handler(request: web.Request) -> web.Response:
    """Health check endpoint for Railway / Cloud deployment monitoring."""
    return web.json_response({
        "status": "healthy",
        "app": "GeoGuessr Telegram Mini App",
        "version": "2.0.0"
    })

async def score_api_handler(request: web.Request) -> web.Response:
    """
    Handle score submissions from WebApp client.
    Optionally updates user stats in SQLite database if user_id is provided.
    Strictly validates score (0 to 25000), user_id (positive int), and rounds (1 to 50).
    """
    try:
        try:
            body = await request.json()
        except Exception:
            return web.json_response({"ok": False, "error": "Invalid or missing JSON payload"}, status=400)

        if not isinstance(body, dict):
            return web.json_response({"ok": False, "error": "Payload must be a JSON object"}, status=400)

        # Validate score
        raw_score = body.get("score")
        if raw_score is None:
            return web.json_response({"ok": False, "error": "Missing required field: score"}, status=400)
        try:
            score = int(raw_score)
        except (ValueError, TypeError):
            return web.json_response({"ok": False, "error": "Score must be an integer"}, status=400)

        if score < 0 or score > MAX_MINIAPP_SCORE:
            return web.json_response(
                {"ok": False, "error": f"Score must be between 0 and {MAX_MINIAPP_SCORE}"},
                status=400
            )

        # Validate rounds (optional, default 5)
        raw_rounds = body.get("rounds", 5)
        try:
            rounds = int(raw_rounds)
            if rounds <= 0 or rounds > 50:
                return web.json_response({"ok": False, "error": "Rounds must be between 1 and 50"}, status=400)
        except (ValueError, TypeError):
            return web.json_response({"ok": False, "error": "Rounds must be an integer"}, status=400)

        # Validate user_id (optional)
        raw_user_id = body.get("user_id")
        user_id = None
        if raw_user_id is not None:
            try:
                user_id = int(raw_user_id)
                if user_id <= 0:
                    return web.json_response({"ok": False, "error": "user_id must be a positive integer"}, status=400)
            except (ValueError, TypeError):
                return web.json_response({"ok": False, "error": "user_id must be an integer"}, status=400)

        db = request.app.get("db")
        if db and user_id:
            # Grant XP proportional to score (e.g. 100 XP per 5,000 score, max 500 XP)
            xp_to_add = min(500, max(25, int(score / 50))) if score > 0 else 0
            if hasattr(db, "add_user_xp"):
                await db.add_user_xp(int(user_id), xp_to_add)
            elif hasattr(db, "record_score_event"):
                await db.record_score_event(int(user_id), points=score, xp=xp_to_add)
            logger.info(f"Recorded Mini App score: user {user_id}, score {score}, added {xp_to_add} XP")

        return web.json_response({"ok": True, "score": score})
    except Exception as exc:
        logger.warning(f"Error processing score submission: {exc}")
        return web.json_response({"ok": False, "error": str(exc)}, status=400)


def create_web_app(db=None) -> web.Application:
    """Create and configure aiohttp Web Application."""
    app = web.Application()
    app["db"] = db

    # Routes
    app.router.add_get("/", index_handler)
    app.router.add_get("/miniapp", index_handler)
    app.router.add_get("/health", health_handler)
    app.router.add_post("/api/miniapp/score", score_api_handler)

    # Static file routes for CSS, JS, Assets
    app.router.add_static("/", path=STATIC_DIR, name="static")

    return app


async def start_web_server(port: int = 8080, host: str = "0.0.0.0", db=None):
    """
    Start the embedded web server.
    Binds to target port and fallback port 8080 if different, ensuring Railway's
    public domain proxy always finds an active listener.
    """
    app = create_web_app(db=db)
    runner = web.AppRunner(app)
    await runner.setup()

    sites = []
    site1 = web.TCPSite(runner, host, port)
    await site1.start()
    sites.append(site1)
    logger.info(f"GeoGuessr Mini App web server running at http://{host}:{port}")

    if port != 8080:
        try:
            site2 = web.TCPSite(runner, host, 8080)
            await site2.start()
            sites.append(site2)
            logger.info(f"GeoGuessr Mini App dual-listener also running at http://{host}:8080")
        except Exception as e:
            logger.info(f"Fallback port 8080 note: {e}")

    return runner, sites
