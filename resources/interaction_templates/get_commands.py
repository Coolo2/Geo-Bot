import discord 
from resources import client, lang
from resources.command_functions import help_commands

class GetCommandsButton(discord.ui.Button):
    def __init__(self, client : client.Client, language):
        self.client = client 
        self.language = language

        super().__init__(
            style=discord.ButtonStyle.primary,
            label = language.showCommandList
        )
    
    async def callback(self, interaction : discord.Interaction):

        await interaction.response.send_message(embed = await help_commands.get_commands_embed(self.client, self.language), ephemeral=True)
