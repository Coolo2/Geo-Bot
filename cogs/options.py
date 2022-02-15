from optparse import OptionGroup
import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import commands
from resources import client, lang , errors, vars

class option(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    options = commands.SlashCommandGroup("options", "Options for the bot")

    @options.command(name="guild", description="Guild-specific options")
    async def _guild(
        self, 
        ctx : discord.Interaction, 
        language : commands.Option(str, required=False, description="The language for public messages in the guild", choices=[l.fullName for l in lang.supported_languages])
    ):
        optGuild = self.bot.client.options.get_guild(ctx.guild)
        optionChanged = False
        lp = lang.private_command(ctx)

        if language != None:
            if not ctx.user.guild_permissions.manage_guild:
                return await ctx.response.send_message(lp.With("MANAGE_SERVER").missingPermissions, ephemeral=True)

            language_code = None

            for l in lang.supported_languages:
                if l.fullName == language:
                    language_code = l.shortName
            
            optGuild.language = language_code 
            await optGuild.save_json()

            optionChanged = True
        
        if optionChanged == True:
            lp = lang.public_command(self.bot.client, ctx)
        
        embed = discord.Embed(title=lp.serverOptions, description=lp.allOptionsForServer, color=vars.embed)
        embed.add_field(name=lp.language, value=lang.get_language(optGuild.language).fullName)


        return await ctx.response.send_message(embed=embed, ephemeral=not optionChanged)



def setup(bot):
    bot.add_cog(option(bot))