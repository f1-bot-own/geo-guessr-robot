"""
EventBus module for real-time application and admin streaming.
Allows decoupled components (game engine, bot handlers, web API) to publish events
and streaming clients (like SSE admin live-stream) to consume them.
"""

import asyncio
import time
import logging
from datetime import datetime, timezone
from typing import Dict, Any, List, Set, Optional

logger = logging.getLogger("EventBus")


class EventBus:
    """Asynchronous in-memory publish-subscribe event bus with history buffer."""

    def __init__(self, max_history: int = 100):
        self.subscribers: Set[asyncio.Queue] = set()
        self.history: List[Dict[str, Any]] = []
        self.max_history = max_history
        self._lock = asyncio.Lock()

    def subscribe(self) -> asyncio.Queue:
        """Register a new subscriber and return its queue."""
        q: asyncio.Queue = asyncio.Queue(maxsize=1000)
        self.subscribers.add(q)
        logger.debug(f"EventBus subscriber added. Total subscribers: {len(self.subscribers)}")
        return q

    def unsubscribe(self, q: asyncio.Queue) -> None:
        """Unregister a subscriber queue."""
        self.subscribers.discard(q)
        logger.debug(f"EventBus subscriber removed. Remaining: {len(self.subscribers)}")

    def publish(self, event_type: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Publish an event to all subscribers and record in history.
        Non-blocking: drops queue if client is too slow.
        """
        now = time.time()
        iso_str = datetime.now(timezone.utc).isoformat()
        payload = {
            "type": event_type,
            "data": data or {},
            "timestamp": now,
            "iso_time": iso_str,
        }

        # Keep history bounded
        self.history.append(payload)
        if len(self.history) > self.max_history:
            self.history.pop(0)

        # Distribute to all queues
        dead_queues = []
        for q in list(self.subscribers):
            try:
                q.put_nowait(payload)
            except asyncio.QueueFull:
                logger.warning("Subscriber queue is full; dropping event for this subscriber.")
            except Exception as e:
                logger.debug(f"Subscriber error: {e}")
                dead_queues.append(q)

        for dq in dead_queues:
            self.subscribers.discard(dq)

        return payload

    async def emit(self, event_type: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Coroutine wrapper for publish."""
        return self.publish(event_type, data)

    def get_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Return the most recent events up to limit."""
        return self.history[-limit:] if limit > 0 else []


# Global singleton EventBus instance
event_bus = EventBus()

def subscribe() -> asyncio.Queue:
    """Subscribe to global event bus."""
    return event_bus.subscribe()

def unsubscribe(queue: asyncio.Queue) -> None:
    """Unsubscribe queue from global event bus."""
    event_bus.unsubscribe(queue)

def publish(event_type: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Publish event to global event bus."""
    return event_bus.publish(event_type, data)

__all__ = ["EventBus", "event_bus", "subscribe", "unsubscribe", "publish"]
