from datetime import datetime
staff = 1
partner = 1<<1
hypesquad = 1<<2
bug_hunter = 1<<3
unknown_4 = 1<<4
unknown_5 = 1<<5
hypesquad_bravery = 1<<6
hypesquad_brilliance = 1<<7
hypesquad_balance = 1<<8
early_supporter = 1<<9
team_user = 1<<10
unknown_11 = 1<<11
system = 1<<12
unknown_13 = 1<<13
bug_hunter_2 = 1<<14
unknown_15 = 1<<15
verified_bot = 1<<16
verified_developer = 1<<17
UNIX_EPOCH = datetime(1970, 1, 1)
DISCORD_EPOCH = 1420070400000
class flags():
    """
    Represents the flags returned from the various methods to return flags, or a supported list of flags.

    Attributes
    -----------
    list: :class:`list`
        A python list object of all flags the user has.
    """
    def __init__(self,flags):
        self.list = flags
    def staff(self):
        if "Staff" in self.list:
            return True
        else:
            return False
    def partner(self):
        if "Partner" in self.list:
            return True
        else:
            return False
    def hs_events(self):
        if "Hypesquad Events" in self.list:
            return True
        else:
            return False
    def bug_hunter(self):
        if "Bug hunter" in self.list:
            return True
        else:
            return False
    def hs_bravery(self):
        if "Hypesquad bravery" in self.list:
            return True
        else:
            return False
    def hs_brilliance(self):
        if "Hypesquad brilliance" in self.list:
            return True
        else:
            return False
    def hs_balance(self):
        if "Hypesquad balance" in self.list:
            return True
        else:
            return False
    def early_nitro(self):
        if "Early nitro" in self.list:
            return True
        else:
            return False
    def team_user(self):
        if "Team user" in self.list:
            return True
        else:
            return False
    def system(self):
        if "System" in self.list:
            return True
        else:
            return False
    def bug_hunter_2(self):
        if "Bug hunter lvl2" in self.list:
            return True
        else:
            return False
    def verified_bot(self):
        if "Verified Bot" in self.list:
            return True
        else:
            return False
    def verified_developer(self):
        if "Verified Developer" in self.list:
            return True
        else:
            return False
def flagsfromint(flags):
    """
    Iterates over all known Discord flag bitwise values with an integer flag value
    """
    if (isinstance(flags, int)):
        pass
    elif flags.isnumeric():
        flags = int(flags)
    else:
        return False
    flaglist=[]
    if (flags & staff) == staff:
        flaglist.append("Staff")
    if (flags & partner) == partner:
        flaglist.append("Partner")
    if (flags & hypesquad) == hypesquad:
        flaglist.append("Hypesquad Events")
    if (flags & bug_hunter) == bug_hunter:
        flaglist.append("Bug hunter")
    if (flags & unknown_4) == unknown_4:
        flaglist.append("MFA_SMS")
    if (flags & unknown_5) == unknown_5:
        flaglist.append("PREMIUM_PROMO_DISMISSED")
    if (flags & hypesquad_bravery) == hypesquad_bravery:
        flaglist.append("Hypesquad bravery")
    if (flags & hypesquad_brilliance) == hypesquad_brilliance:
        flaglist.append("Hypesquad brilliance")
    if (flags & hypesquad_balance) == hypesquad_balance:
        flaglist.append("Hypesquad balance")
    if (flags & early_supporter) == early_supporter:
        flaglist.append("Early nitro")
    if (flags & team_user) == team_user:
        flaglist.append("Team user")
    if (flags & unknown_11) == unknown_11:
        flaglist.append("Unused")
    if (flags & system) == system:
        flaglist.append("System")
    if (flags & unknown_13) == unknown_13:
        flaglist.append("Unread urgent system message ")
    if (flags & bug_hunter_2) == bug_hunter_2:
        flaglist.append("Bug hunter lvl2")
    if (flags & unknown_15) == unknown_15:
        flaglist.append("UNDERAGE_DELETED")
    if (flags & verified_bot) == verified_bot:
        flaglist.append("Verified Bot")
    if (flags & verified_developer) == verified_developer:
        flaglist.append("Verified Developer")
    return flaglist
def flagsfromjson(user_json):
    """
    Gets the flag parameters returned from the Discord HTTP REST API and returns a misccord.flags object with the user's flags.
    user_json = the JSON response from the Discord API.
    """
    flags = []
    if "flags" in user_json:
        flags += flagsfromint(user_json["flags"])
    if "public_flags" in user_json:
        flags += flagsfromint(user_json["public_flags"])
    return flags(flags)
async def flagsfromdpy(user):
    """
    Gets the flag parameters from a discord.py user object and returns a misccord.flags object with the user's flags.
    user = the discord.py user object. This MUST be a user and not a member!
    """
    import asyncio, discord
    user_json=await user._state.http.get_user(user.id)
    return flagsfromjson(user_json)
def flagsfromdisco(user):
    """
    Gets the flag parameters from a disco user object and returns a misccord.flags object with the user's flags.
    user = the disco user object.
    """
    import disco
    return flagsfromjson(user.to_dict())
def sf_to_datetime(snowflake):
    """
    Converts a Discord snowflake to a UTC datetime.
    """
    return datetime.utcfromtimestamp(sf_to_unix(snowflake))
def sf_to_unix(snowflake):
    """
    Converts a Discord snowflake to a UNIX_EPOCH time integer.
    """
    return sf_to_unix_ms(snowflake) / 1000
def sf_to_unix_ms(snowflake):
    """
    Converts a Discord snowflake to a UNIX_EPOCH time integer in milliseconds.
    """
    return (int(snowflake) >> 22) + DISCORD_EPOCH
