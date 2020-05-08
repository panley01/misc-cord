"""Utilities for working with user flags."""

from typing import Any, Dict, List, Union

STAFF = 1
PARTNER = 1 << 1
HYPESQUAD_EVENTS = 1 << 2
BUG_HUNTER = 1 << 3
UNKNOWN_4 = 1 << 4
UNKNOWN_5 = 1 << 5
HYPESQUAD_BRAVERY = 1 << 6
HYPESQUAD_BRILLIANCE = 1 << 7
HYPESQUAD_BALANCE = 1 << 8
EARLY_SUPPORTER = 1 << 9
TEAM_USER = 1 << 10
UNKNOWN_11 = 1 << 11
SYSTEM = 1 << 12
UNKNOWN_13 = 1 << 13
BUG_HUNTER_2 = 1 << 14
UNKNOWN_15 = 1 << 15
VERIFIED_BOT = 1 << 16
VERIFIED_DEVELOPER = 1 << 17


class Flags:
    """
    Flags from a Discord user.

    Represents the flags returned from the Discord API in integer form
    as a class with attributes representing each flag.

    Attributes
    -----------
    list: :class:`list`
        A python list object of all flags the user has.

    """

    def __init__(self, flags: List[str]) -> None:
        """Create a new Flags instance."""
        if not isinstance(flags, list):
            raise ValueError("Flags must be passed a list of user flags.")

        self.list = flags

    @property
    def staff(self) -> bool:
        """Discord staff."""
        return "Staff" in self.list

    @property
    def partner(self) -> bool:
        """Discord Partner."""
        return "Partner" in self.list

    @property
    def hs_events(self) -> bool:
        """Hypesquad events."""
        return "Hypesquad Events" in self.list

    @property
    def bug_hunter(self) -> bool:
        """Bug Hunter (Level 1)."""
        return "Bug hunter" in self.list

    @property
    def hs_bravery(self) -> bool:
        """Hypesquad Bravery."""
        return "Hypesquad bravery" in self.list

    @property
    def hs_brilliance(self) -> bool:
        """Hypesquad Brilliance."""
        return "Hypesquad brilliance" in self.list

    @property
    def hs_balance(self) -> bool:
        """Hypesquad Balance."""
        return "Hypesquad balance" in self.list

    @property
    def early_nitro(self) -> bool:
        """Early supporter."""
        return "Early nitro" in self.list

    @property
    def team_user(self) -> bool:
        """Team user."""
        return "Team user" in self.list

    @property
    def system(self) -> bool:
        """System user."""
        return "System" in self.list

    @property
    def bug_hunter_2(self) -> bool:
        """Bug Hunter (Level 2)."""
        return "Bug hunter lvl2" in self.list

    @property
    def verified_bot(self) -> bool:
        """Verified Bot."""  # noqa: D401
        return "Verified Bot" in self.list

    @property
    def verified_developer(self) -> bool:
        """Verified Developer."""  # noqa: D401
        return "Verified Developer" in self.list


def flags_from_int(flags: Union[str, int]) -> List[str]:
    """
    Convert a Discord flags integer into the relevant user flags.

    :param flags: The flags or public_flags value from the Discord API.
    :rtype: list[str]
    """
    if (isinstance(flags, int)):
        pass
    elif flags.isnumeric():
        flags = int(flags)
    else:
        return False

    flaglist = []

    if (flags & STAFF) == STAFF:
        flaglist.append("Staff")

    if (flags & PARTNER) == PARTNER:
        flaglist.append("Partner")

    if (flags & HYPESQUAD_EVENTS) == HYPESQUAD_EVENTS:
        flaglist.append("Hypesquad Events")

    if (flags & BUG_HUNTER) == BUG_HUNTER:
        flaglist.append("Bug hunter")

    if (flags & UNKNOWN_4) == UNKNOWN_4:
        flaglist.append("MFA_SMS")

    if (flags & UNKNOWN_5) == UNKNOWN_5:
        flaglist.append("PREMIUM_PROMO_DISMISSED")

    if (flags & HYPESQUAD_BRAVERY) == HYPESQUAD_BRAVERY:
        flaglist.append("Hypesquad bravery")

    if (flags & HYPESQUAD_BRILLIANCE) == HYPESQUAD_BRILLIANCE:
        flaglist.append("Hypesquad brilliance")

    if (flags & HYPESQUAD_BALANCE) == HYPESQUAD_BALANCE:
        flaglist.append("Hypesquad balance")

    if (flags & EARLY_SUPPORTER) == EARLY_SUPPORTER:
        flaglist.append("Early nitro")

    if (flags & TEAM_USER) == TEAM_USER:
        flaglist.append("Team user")

    if (flags & UNKNOWN_11) == UNKNOWN_11:
        flaglist.append("Unused")

    if (flags & SYSTEM) == SYSTEM:
        flaglist.append("System")

    if (flags & UNKNOWN_13) == UNKNOWN_13:
        flaglist.append("Unread urgent system message")

    if (flags & BUG_HUNTER_2) == BUG_HUNTER_2:
        flaglist.append("Bug hunter lvl2")

    if (flags & UNKNOWN_15) == UNKNOWN_15:
        flaglist.append("UNDERAGE_DELETED")

    if (flags & VERIFIED_BOT) == VERIFIED_BOT:
        flaglist.append("Verified Bot")

    if (flags & VERIFIED_DEVELOPER) == VERIFIED_DEVELOPER:
        flaglist.append("Verified Developer")

    return flaglist


def flags_from_json(user_json: Dict[str, Any]) -> Flags:
    """
    Convert a Discord API user object to a Flags instance.

    Takes in the JSON user from the Discord API response and
    searches for flags and public_flags within this.

    :param user_json: The JSON response from the Discord API.
    :type user_json: dict
    """
    flags = []

    if "flags" in user_json:
        flags += flags_from_int(user_json["flags"])

    if "public_flags" in user_json:
        flags += flags_from_int(user_json["public_flags"])

    return flags(flags)


async def discord_py(user) -> Flags:  # noqa: ANN001
    """
    Fetch the flags from a Discord.py user object.

    :param user: The user or member from discord.py
    :rtype: Flags
    """
    user_json = await user._state.http.get_user(user.id)
    return flags_from_json(user_json)


def disco(user) -> Flags:  # noqa: ANN001
    """
    Fetch the flags from a Disco user object.

    :param user: The user object from Disco
    :rtype: Flags
    """
    return flags_from_json(user.to_dict())
