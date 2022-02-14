import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import commands

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.add_item(discord.ui.InputText(label="Song Link", placeholder="Song Link", style=discord.InputTextStyle.singleline))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("hi")

class MyView(discord.ui.View):
    @discord.ui.button(label="Test Modal", emoji="🙋")
    async def button_callback(self, button, interaction):
        modal = MyModal(title="Enter the song details")
        await interaction.response.send_modal(modal)

class test(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.slash_command(name="test1")
    async def _test(self, ctx):
        print("in")

        await ctx.respond("test", view=MyView())

    
def setup(bot):
    bot.add_cog(test(bot))