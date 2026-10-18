"""
Re-export of EventBus for webapp module compatibility.
Provides access to global event_bus, subscribe, unsubscribe, and publish functions.
"""
from events.bus import EventBus, event_bus, subscribe, unsubscribe, publish

__all__ = ["EventBus", "event_bus", "subscribe", "unsubscribe", "publish"]
