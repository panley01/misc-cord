from datetime import datetime
UNIX_EPOCH = datetime(1970, 1, 1)
DISCORD_EPOCH = 1420070400000
def to_datetime(snowflake):
    """
    Converts a Discord snowflake to a UTC datetime.
    """
    return datetime.utcfromtimestamp(to_unix(snowflake))
def to_unix(snowflake):
    """
    Converts a Discord snowflake to a UNIX_EPOCH time integer.
    """
    return to_unix_ms(snowflake) / 1000
def to_unix_ms(snowflake):
    """
    Converts a Discord snowflake to a UNIX_EPOCH time integer in milliseconds.
    """
    return (int(snowflake) >> 22) + DISCORD_EPOCH
