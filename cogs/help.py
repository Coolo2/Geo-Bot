
from typing import List
import discord

from discord.ext import commands as cmds
from discord import commands
from resources import errors, geography, lang, config
from resources.command_functions import help_commands
from resources.interaction_templates import get_commands


class help(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    help_commands = commands.SlashCommandGroup("help", "All help commands")

    @help_commands.command(name="bot", description="Information about the bot")
    async def _bot(self, ctx):

        lp = lang.private_command(ctx)

        raw_data : dict = await self.bot.client.economy._get_economy()
        total_games = 0
        total_balance = 0

        for user_id, user_data in raw_data.items():
            total_games += user_data["wins"] + user_data["losses"]
            total_balance += user_data["balance"]
        
        owner = (await self.bot.application_info()).owner

        embed = discord.Embed(
            title=lp.botInformation,
            description=lp.With(self.bot.user.name, "Coolo2#5499", owner).description,
            color=config.embed
        )
        embed.add_field(name=lp.totalGamesPlayeed, value=total_games)
        embed.add_field(name=lp.totalBalance, value=total_balance)

        view = discord.ui.View()
        view.add_item(get_commands.GetCommandsButton(self.bot.client, lp))

        return await ctx.response.send_message(embed=embed, view=view, ephemeral=True)
    
    @help_commands.command(name="commands", description="Command list")
    async def _command(self, ctx : discord.ApplicationContext):
        language = lang.private_command(ctx)
        
        await ctx.response.send_message(embed=await help_commands.get_commands_embed(self.bot.client, language), ephemeral=True)
        


    
def setup(bot):
    bot.add_cog(help(bot))
    