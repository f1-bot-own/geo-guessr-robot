"""
Configuration settings for GeoGuru & GeoGuessr Telegram Bot.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Database Path
DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / "geobot.db"))

# Default Language (must be English as requested)
DEFAULT_LANGUAGE = "en"
SUPPORTED_LANGUAGES = ["en", "ru", "uz"]

# Game Defaults
DEFAULT_ROUNDS = 5
DEFAULT_ROUND_TIME = 30  # seconds (default 30s)
ROUND_TIME_OPTIONS = [30, 60]
DEFAULT_INPUT_MODE = "both"
INPUT_MODES = ["buttons", "text", "both"]
MIN_ROUNDS = 3
MAX_ROUNDS = 20
MIN_ROUND_TIME = 30
MAX_ROUND_TIME = 60

# Points configuration
POINTS_CORRECT = 100
POINTS_TIME_BONUS_MULTIPLIER = 2  # up to 2x bonus depending on remaining time
POINTS_WRONG_PENALTY = 20
XP_PER_CORRECT = 25
XP_PER_WIN = 100

# Level calculation: Level = 1 + int((XP / 200) ** 0.5)
