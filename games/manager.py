"""
Game Manager for Tracking Active Chat Sessions and Solo Sessions.
"""

from typing import Dict, Optional
from .session import GameSession
from .solo_session import SoloGameSession
from .daily_session import DailyChallengeSession

class GameManager:
    def __init__(self):
        self.sessions: Dict[int, GameSession] = {}
        self.solo_sessions: Dict[int, SoloGameSession] = {}
        self.daily_sessions: Dict[int, DailyChallengeSession] = {}
        self.duel_invites: Dict[int, dict] = {}
        self.solo_setup_states: Dict[int, dict] = {}

    def get_solo_setup_state(self, user_id: int) -> dict:
        """Get or initialize solo setup state."""
        return self.solo_setup_states.get(user_id, {"input_mode": "both", "mode": "mix", "round_time": 30})

    def set_solo_setup_state(self, user_id: int, state: dict):
        """Update solo setup state."""
        current = self.get_solo_setup_state(user_id)
        current.update(state)
        self.solo_setup_states[user_id] = current

    def get_session(self, chat_id: int) -> Optional[GameSession]:
        """Get active group session for chat."""
        return self.sessions.get(chat_id)

    def set_session(self, chat_id: int, session: GameSession):
        """Register active group session."""
        self.sessions[chat_id] = session

    def remove_session(self, chat_id: int):
        """Remove and stop active group session."""
        session = self.sessions.pop(chat_id, None)
        if session:
            session.stop()

    def get_solo_session(self, user_id: int) -> Optional[SoloGameSession]:
        """Get active solo session for user."""
        return self.solo_sessions.get(user_id)

    def set_solo_session(self, user_id: int, session: SoloGameSession):
        """Register solo session."""
        self.solo_sessions[user_id] = session

    def remove_solo_session(self, user_id: int):
        """Remove solo session."""
        self.solo_sessions.pop(user_id, None)

    def get_daily_session(self, user_id: int) -> Optional[DailyChallengeSession]:
        """Get active daily challenge session for user."""
        return self.daily_sessions.get(user_id)

    def set_daily_session(self, user_id: int, session: DailyChallengeSession):
        """Register daily challenge session."""
        self.daily_sessions[user_id] = session

    def remove_daily_session(self, user_id: int):
        """Remove daily challenge session."""
        self.daily_sessions.pop(user_id, None)

    def set_duel_invite(self, chat_id: int, invite_data: dict):
        """Set pending duel challenge."""
        self.duel_invites[chat_id] = invite_data

    def get_duel_invite(self, chat_id: int) -> Optional[dict]:
        """Get pending duel challenge."""
        return self.duel_invites.get(chat_id)

    def remove_duel_invite(self, chat_id: int):
        """Clear duel challenge."""
        self.duel_invites.pop(chat_id, None)

# Global singleton
game_manager = GameManager()
