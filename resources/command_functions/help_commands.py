
from resources import client, config
import discord

async def get_commands_embed(client : client.Client, language):

    bot_commands = {}

    for command in client.bot.application_commands:
        for subcommand in command.subcommands:
            if hasattr(subcommand, "subcommands"):
                for sc in subcommand.subcommands:

                    bot_commands[str(sc)] = sc
            else:
                bot_commands[str(subcommand)] = subcommand

    cmdsStr = ""
    for cmdName, cmd in bot_commands.items():
        cmdsStr += f"`/{cmd.qualified_name}` - {cmd.description}\n"
    
    embed = discord.Embed(title=language.myCommands, description=language.belowIsAListOfCommands, color=config.embed)

    embed.add_field(name=language.commands, value=cmdsStr)

    return embed