"""
Backward-compatibility proxy for gamedata.
Note: For production deployments where /app/data is mounted as a persistent volume,
code should always import from 'gamedata' directly.
"""
try:
    from gamedata import countries, landmarks, streetviews, fun_facts
except ImportError:
    pass

__all__ = ["countries", "landmarks", "streetviews", "fun_facts"]
