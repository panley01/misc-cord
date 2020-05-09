"""Utilities for working with Discord snowflakes."""

from datetime import datetime
from typing import Union

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


def get_worker_id(snowflake: int) -> int:
    """Fetch a Discord snowflake's worker ID."""
    return (snowflake & 0x3E0000) >> 17


def get_process_id(snowflake: int) -> int:
    """Fetch a Discord snowflake's process ID."""
    return (snowflake & 0x1F000) >> 12


def get_increment(snowflake: int) -> int:
    """Fetch a Discord snowflake's increment ID."""
    return snowflake & 0xFFF


class SlicedSnowflake:
    """
    Information stored in a Discord snowflake.

    Represents the values that form a Discord snowflake as a
    class with attributes representing each value.

    Attributes
    -----------
    snowflake: :class:`int`
        The snowflake repesentation used to construct the class.

    datetime: :class:`datetime`
        A datetime UTC timestamp of snowflake creation.

    unix: :class:`int`
        A UNIX_EPOCH integer of snowflake creation.

    unix_ms: :class:`int`
        A UNIX_EPOCH integer of snowflake creation in milliseconds.

    worker_id: :class:`int`
        The Discord internal worker ID that created the snowflake.

    process_id: :class:`int`
        The Discord internal process ID that created the snowflake.

    increment: :class:`int`
        Incremented for every created snowflake on the snowflake's
        process ID.

    """

    def __init__(self, snowflake: Union[str, int]) -> None:
        """
        Construct a new SlicedSnowflake with a snowflake.

        :param snowflake: The snowflake from Discord
        :type snowflake: int, str
        """
        if isinstance(snowflake, str):
            snowflake = int(snowflake)

        self.snowflake = snowflake
        self.datetime = to_datetime(snowflake)
        self.unix = to_unix(snowflake)
        self.unix_ms = to_unix_ms(snowflake)
        self.worker_id = get_worker_id(snowflake)
        self.process_id = get_process_id(snowflake)
        self.increment = get_increment(snowflake)
