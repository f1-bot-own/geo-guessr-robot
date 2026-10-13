"""Backward-compatibility proxy for gamedata.landmarks."""
from gamedata.landmarks import *  # noqa: F401, F403
from gamedata.landmarks import LANDMARKS, LANDMARKS_BY_ID, get_landmark_by_id, get_random_landmarks, get_landmark  # noqa: F401
