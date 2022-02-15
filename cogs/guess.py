import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import commands
from resources import client, games

from resources.command_functions import guess_flags_input, guess_capital_input, guess_flags_multiple_choice, guess_capital_multiple_choice

class guess(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    guessing_games = commands.SlashCommandGroup("guess", "All guessing games")

    multiple_choice = guessing_games.create_subgroup("multiple_choice", "All multiple choice guessing games")
    input_games = guessing_games.create_subgroup("input", "Guessing games without choices")


    # COmmands


    @multiple_choice.command(name="flags", description="Guess a country from a flag (multiple choice)")
    async def _flags_multiple_choice(self, ctx : commands.ApplicationContext):
        await guess_flags_multiple_choice.start_game(self.bot.client, ctx, ctx.author)
        
    
    @input_games.command(name="flags", description="Guess a country from a flag (text input)")
    async def _flags_input(self, ctx : commands.ApplicationContext):
        await guess_flags_input.start_game(self.bot.client, ctx, ctx.author)

    
    @input_games.command(name="capitals", description="Guess a country from its capital city (text input)")
    async def _capitals_input(self, ctx : commands.ApplicationContext):
        await guess_capital_input.start_game(self.bot.client, ctx, ctx.author)

    
    @multiple_choice.command(name="capitals", description="Guess a country from its capital city (multiple choice)")
    async def _capitals_multiple_choice(self, ctx : commands.ApplicationContext):
        await guess_capital_multiple_choice.start_game(self.bot.client, ctx, ctx.author)
    
def setup(bot):
    bot.add_cog(guess(bot))