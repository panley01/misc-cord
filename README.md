# misc-cord
Miscellanious utilities for Discord, written in Python with functions compatible with discord.py and disco

To install, you will have to manually clone this repo and import the relevant scripts you wish to use.
PIP soontm

## Currently supports:
- Extracting user objects from discord.py
- Extracting user objects from disco
- Transforming user JSON into a flags class, containing a list of flags
- Checking for individual flags via the flags class
- Discord Snowflake to datetime timestamps and unix timestamps
## Planned features
- Permissions calculator/translator for easy permissions creation
- Oauth permissions caluclator
- Snowflake Internal Worker ID, Internal Process ID and Increment parser
- Markdown parsing/translation for messages
- Tweetmoji/emoji code to unicode character conversion (and visa versa)

## Examples:
Using misc-cord to check a user returned from the Discord HTTP REST API
```python
import requests
from misccord import flags
headers = {
  "Content-Type":"application/json",
  "Authorization":"Bot loremipsum123",
  "User-Agent":"DiscordBot"
  }
r = requests.get("https://discordapp.com/api/v6/users/@me",headers=headers)
r.raise_for_status()
if (flags.flagsfromjson(r.json)).verified_bot():
  print("Current bot user is a verified bot")
else:
  print("Current bot user is NOT a verified bot")
```
Using misc-cord to get a users flags from a discord.py user object
```python
import discord
from misccord import flags
ctx = discord.Client()
@ctx.event
async def on_ready():
  flags = flags.flagsfromdpy(ctx.ClientUser)
  for x in flags.list:
    print(x)
```
