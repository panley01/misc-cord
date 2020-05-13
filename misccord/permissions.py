"""Utilities for working with user flags."""
import inspect
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

CREATE_INSTANT_INVITE = 1
KICK_MEMBERS = 1 << 1
BAN_MEMBERS = 1 << 2
ADMINISTRATOR = 1 << 3
MANAGE_CHANNELS = 1 << 4
MANAGE_GUILD = 1 << 5
ADD_REACTIONS = 1 << 6
VIEW_AUDIT_LOG = 1 << 7
PRIORITY_SPEAKER = 1 << 8
STREAM = 1 << 9
VIEW_CHANNEL = 1 << 10
SEND_MESSAGES = 1 << 11
SEND_TTS_MESSAGES = 1 << 12
MANAGE_MESSAGES = 1 << 13
EMBED_LINKS = 1 << 14
ATTACH_FILES = 1 << 15
READ_MESSAGE_HISTORY = 1 << 16
MENTION_EVERYONE = 1 << 17
USE_EXTERNAL_EMOTES = 1 << 18
VIEW_GUILD_INSIGHTS = 1 << 19
CONNECT = 1 << 20
SPEAK = 1 << 21
MUTE_MEMBERS = 1 << 22
DEAFEN_MEMBERS = 1 << 23
MOVE_MEMBERS = 1 << 24
USE_VAD = 1 << 25
CHANGE_NICKNAME = 1 << 26
MANAGE_NICKNAMES = 1 << 27
MANAGE_ROLES = 1 << 28
MANAGE_WEBHOOKS = 1 << 29
MANAGE_EMOJIS = 1 << 30
VOICE_DENIED = [KICK_MEMBERS,BAN_MEMBERS,ADMINISTRATOR,MANAGE_GUILD,VIEW_AUDIT_LOG,VIEW_GUILD_INSIGHTS,CHANGE_NICKNAME,MANAGE_NICKNAMES,MANAGE_EMOJIS,ADD_REACTIONS,SEND_MESSAGES,SEND_TTS_MESSAGES,MANAGE_MESSAGES,EMBED_LINKS,ATTACH_FILES,READ_MESSAGE_HISTORY,MENTION_EVERYONE,USE_EXTERNAL_EMOTES]
TEXT_DENIED = [KICK_MEMBERS,BAN_MEMBERS,ADMINISTRATOR,MANAGE_GUILD,VIEW_AUDIT_LOG,PRIORITY_SPEAKER,STREAM,VIEW_GUILD_INSIGHTS,CONNECT,SPEAK,MUTE_MEMBERS,DEAFEN_MEMBERS,MOVE_MEMBERS,USE_VAD,CHANGE_NICKNAME,MANAGE_NICKNAMES,MANAGE_EMOJIS]


class PermissionType(Enum):
    """An enum representing the 4 Discord objects that have permissions."""

    text_channel = "text channel"
    voice_channel = "voice channel"
    role = "role"
    user = "user"

    def typecheck(self,permissions) -> bool:
        """
        Checks whether a permission integer is valid for the selected PermissionType
        """
        if self.text_channel:
            return all(map(lambda x: (permissions & x) != x, TEXT_DENIED))
        elif self.voice_channel:
            return all(map(lambda x: (permissions & x) != x, VOICE_DENIED))
        elif self.role or self.user:
            return True
        else:
            raise Exception("Invalid PermissionType")


class Permissions:
    """
    Permissions from a Discord user, role or channel.
    Represents the permissions returned from the Discord API in integer form
    as a class with attributes representing each permission.
    Attributes
    -----------
    list: :class:`list`
        A python list object of all permissions enabled.
    int: :class:`int`
        A python integer of the perms value.
    """

    def __init__(self, perms: int, permtype: PermissionType) -> None:
        """Create a new Flags instance."""
        if not isinstance(perms, int):
            raise ValueError("permissions must be an integer from the Discord API.")
        if not isinstance(permtype, PermissionType):
            raise ValueError("permtype must be a PermissionType Object.")
        if not permtype.typecheck(perms):
            raise Exception("permissions integer contains permissions invalid for the selected permtype")
        self.perms = perms
        self.type = permtype

    def enabled(self) -> List[Tuple[str, bool]]:
        """
        Return a list of enabled permissions on the value.
        :rtype: list[tuple[str, bool]]
        """
        perms = []

        for name, value in inspect.getmembers(self):
            if name.startswith("_"):
                continue

            if isinstance(value, bool):
                if value:
                    perms.append(name)

        return perms

    def __iter__(self) -> List[Tuple[str, bool]]:
        """
        Return a list of enabled permissions on the value.
        Under the hood this just calls the enabled method.
        :rtype: list[tuple[str, bool]]
        """
        for perm in self.enabled():
            yield perm
    
    def __int__(self):
        """
        Return the Int value for the permissions.
        Under the hood this just calls self.perms.
        :rtype: int()
        """
        return self.perms

    # Permission bitwise checks

    @property
    def stream(self) -> bool:
        """Stream Permission | VC ONLY."""
        return (self.perms & STREAM) == STREAM

class ChannelOverwrites():
    """
    Permission overwrites from a Discord channel, targets one passed role or user.
    Represents the channel overwrites permissions returned from the Discord API
    in integer form as a class with attributes representing each permission in
    both the allow and deny fields.
    Attributes
    -----------
    list: :class:`list`
        A list of tuples from both the allowed and denied perms in the format
        (str, bool). Allowed perms are True, and denied are False.
    allow: :class:`Permissions`
        A Permissions object for the permissions int passed to it, represents allow overwrites.
    deny: :class:`Permissions`
        A Permissions object for the permissions int passed to it, represents deny overwrites.
    
    """

    def __init__(self, allow: int =0, deny: int =0, permtype: PermissionType):
        if not isinstance(allow, int):
            raise ValueError("allow must be an integer from the Discord API.")
        if not isinstance(deny, int):
            raise ValueError("deny must be an integer from the Discord API.")
        if not isinstance(permtype, PermissionType):
            raise ValueError("permtype must be a PermissionType Object.")
        if (permtype == PermissionType.user) or (permtype == PermissionType.role):
            raise Exception("permtype invalid for ChannelOverwrites. Must be PermissionType.text or PermissionType.voice.")
        if not permtype.typecheck(perms):
            raise Exception("permissions integer contains permissions invalid for the selected permtype")
        self.allow = Permissions(allow,permtype)
        self.deny = Permissions(deny,permtype)
        self.type = permtype

        def __iter__(self) -> List[Tuple[str, bool]]:
            perms = []

            for perm in list(self.allow):
                perms.append(tuple(perm, True))
            for perm in list(self.deny):
                perms.append(tuple(perm, False))
            
            return perms
