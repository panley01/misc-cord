# misc-cord
Miscellanious utilities for Discord, written in Python with functions compatible with discord.py and disco

To install, you will have to manually clone this repo and import the relevant scripts you wish to use.
PIP soontm

## Currently supports:
- Extracting user objects from discord.py
- Extracting user objects from disco **_public_flags has not been merged to disco yet, please use [this fork.](https://github.com/elderlabs/disco/tree/rowboat)_**
- Transforming user JSON into a flags class, containing a list of flags
- Checking for individual flags via the flags class
- Discord Snowflake splicing to extract Datetime and Unix epoch timestamps
- Discord Snowflake splicing to extract its worker ID, process ID and increment
## Planned features
- Permissions calculator/translator for easy permissions creation
- Oauth permissions caluclator
- Markdown parsing/translation for messages
- Tweetmoji/emoji code to unicode character conversion (and visa versa)

## Examples:
Using misc-cord to check a user returned from the Discord HTTP REST API

```python
import requests
from misccord import flags

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bot loremipsum123",
  "User-Agent": "DiscordBot"
}

r = requests.get("https://discordapp.com/api/v6/users/@me", headers=headers)
r.raise_for_status()

if flags.flags_from_json(r.json()).verified_bot:
  print("Current bot user is a verified bot")
else:
  print("Current bot user is NOT a verified bot")
```

Using misc-cord to get a users flags from a discord.py user object
```python
import discord
from misccord import flags

class MyBot(discord.Client):
    async def on_ready(self):
        user_flags = await flags.discord_py(self.user)

        if user_flags.verified_bot:
            print("Logged in as a verified bot!")
        else:
            print("Not a verified bot :(")

bot = MyBot()
bot.run("token")
```

Using misc-cord to add a command to your discord.py bot for fetching a users hypesquad house:
```python
from discord.ext.commands import Bot, command
from misccord import flags

bot = Bot(command_prefix="!")

@bot.command()
async def hypesquad_house(ctx):
    """Fetch a users hypesquad house."""
    user_flags = await flags.discord_py(ctx.author)

    hypesquad_house = user_flags.hypesquad_house.value
    mention = ctx.author.mention

    await ctx.send(f"{mention}: You are in {hypesquad_house.title()}")

bot.run("token")
```

Using misc-cord to add a command to your disco bot for listing all flags a user has:
```python
from disco.bot import Bot, Plugin
from misccord import flags

class SimplePlugin(Plugin):
    @Plugin.command('my_flags')
    def on_my_flags_commmand(self, event):
        user_flags = flags.disco(event.msg.author)

        output_msg = "__Your flags:__\n"
        for enabled_flag in user_flags:
            output_msg += enabled_flag.replace("_", " ").title() + "\n"

        event.msg.reply(output_msg)
```
