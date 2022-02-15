import discord 
import os
import logging 

from resources import client 
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

bot.load_extension("cogs.guess")
bot.load_extension("cogs.info")
bot.load_extension("cogs.errorHandling")
bot.load_extension("cogs.options")
bot.load_extension("cogs.events")

webserver.webserver_run(bot)
bot.run(os.getenv("token"))