"""Utilities for working with Discord permissions."""
import inspect
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

# THIS SCRIPT IS CURRENTLY NOT IN A RUNNING STATE AND SHOULD NOT BE IMPORTED

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

    TEXT_CHANNEL = "text channel"
    VOICE_CHANNEL = "voice channel"
    ROLE = "role"
    USER = "user"

    def typecheck(self,permissions) -> bool:
        """
        Checks whether a permission integer is valid for the selected PermissionType
        """
        if self.TEXT_CHANNEL:
            return all(map(lambda x: (permissions & x) != x, TEXT_DENIED))
        elif self.VOICE_CHANNEL:
            return all(map(lambda x: (permissions & x) != x, VOICE_DENIED))
        elif self.ROLE or self.USER:
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
    """

    def __init__(self, allow: int, deny=0: int, permtype: PermissionType) -> None:
        """Create a new Flags instance."""
        if not (isinstance(allow, int) or isinstance(allow, int)):
            raise ValueError("permissions must be an integer from the Discord API.")
        if not isinstance(permtype, PermissionType):
            raise ValueError("permtype must be a PermissionType Object.")
        if not (permtype.typecheck(allow) or permtype.typecheck(deny)):
            raise Exception("permissions integer contains permissions invalid for the selected permtype")
        self.allow = allow
        self.deny = deny

        @property
        def set(self) -> List[Tuple[str, bool]]:
            """
            Return a list of permissions on the value.
            True if the perm is allowed, False if denied
            :rtype: list[tuple[str, bool]]
            """
            perms = []

            for name, value in inspect.getmembers(self):
                if name.startswith("_"):
                    continue

                if isinstance(value, bool):
                    perms.append(name)

            return perms
        
        @property
        def allow_list(self) -> List[Tuple[str, bool]]:
            """
            Placeholder.
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
        
        @property
        def deny_list(self) -> List[Tuple[str, bool]]:
            """
            Placeholder.
            :rtype: list[tuple[str, bool]]
            """
            perms = []

            for name, value in inspect.getmembers(self):
                if name.startswith("_"):
                    continue

                if isinstance(value, bool):
                    if not value:
                        perms.append(name)

            return perms

        # Permission bitwise checks

        @property
        def stream(self) -> bool:
            """Discord perm placeholder"""
            if (self.allow & STREAM) == STREAM:
                return True
            elif (self.deny & STREAM) == STREAM:
                return False
            else:
                return None
