"""Utilities for working with Discord snowflakes."""

from datetime import datetime

UNIX_EPOCH = datetime(1970, 1, 1)
DISCORD_EPOCH = 1420070400000


def to_datetime(snowflake: int) -> datetime:
    """Convert a Discord snowflake to a UTC datetime."""
    return datetime.utcfromtimestamp(to_unix(snowflake))


def to_unix(snowflake: int) -> int:
    """Convert a Discord snowflake to a UNIX_EPOCH time integer."""
    return to_unix_ms(snowflake) / 1000


def to_unix_ms(snowflake: int) -> int:
    """Convert a Discord snowflake to unix timestamp in milliseconds."""
    return (int(snowflake) >> 22) + DISCORD_EPOCH
