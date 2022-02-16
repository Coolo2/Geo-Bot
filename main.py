import discord 
import os

from resources import client, color
import webserver

intents = discord.Intents.default()
intents.members = False

bot = discord.Bot(debug_guilds=[450914634963353600, 742065869856702514])
hardResetGuildCommands = False

@bot.event 
async def on_ready():
    print(f"{bot.user} online.")

    if hardResetGuildCommands:
        for guildID in bot.debug_guilds:
            await bot.http.bulk_upsert_guild_commands(bot.user.id, guildID, [])

    bot.client = client.Client(bot)

extensions =  [f"cogs.{f.replace('.py', '')}" for f in os.listdir("./cogs") if os.path.isfile(os.path.join("./cogs", f))]

for extension in extensions:
    bot.load_extension(extension)
    print(f"{color.green}{color.underline}{extension}{color.end}{color.green} loaded{color.end}")

webserver.webserver_run(bot)
bot.run(os.getenv("token"))