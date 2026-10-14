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
    """
    try:
        body = await request.json()
        user_id = body.get("user_id")
        score = int(body.get("score", 0))
        rounds = int(body.get("rounds", 5))
        
        db = request.app.get("db")
        if db and user_id:
            # Grant XP proportional to score (e.g. 100 XP per 5,000 score, max 500 XP)
            xp_to_add = min(500, max(25, int(score / 50)))
            await db.add_user_xp(int(user_id), xp_to_add)
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
