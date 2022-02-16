
import discord

from discord.ext import commands as cmds
from discord import commands
from resources import config, lang

class option(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    options = commands.SlashCommandGroup("options", "Options for the bot")

    @options.command(name="guild", description="Guild-specific options")
    async def _guild(
        self, 
        ctx : discord.Interaction, 
        language : commands.Option(str, required=False, description="The language for public messages in the guild", choices=[l.fullName for l in lang.supported_languages]),
        multiple_choice_type : commands.Option(str, required=False, description="The type of input for multiple choice questions", choices=["Buttons", "Select Menues"])
    ):
        optGuild = self.bot.client.options.get_guild(ctx.guild)
        optionChanged = False
        lp = lang.private_command(self.bot.client, ctx)

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
        
        if multiple_choice_type != None:
            if not ctx.user.guild_permissions.manage_guild:
                return await ctx.response.send_message(lp.With("MANAGE_SERVER").missingPermissions, ephemeral=True)
            
            optGuild.multipleChoiceType = "button" if multiple_choice_type == "Buttons" else "select"

            await optGuild.save_json()

            optionChanged = True

        
        if optionChanged == True:
            lp = lang.public_command(self.bot.client, ctx)
        
        embed = discord.Embed(title=lp.serverOptions, description=lp.allOptionsForServer, color=config.embed)
        embed.add_field(name=lp.language, value=lang.get_language(optGuild.language).fullName)
        embed.add_field(name=lp.multipleChoiceType, value=optGuild.multipleChoiceType.title())
        embed.set_footer(text="*" + lp.guildLanguageDisclaimer)

        return await ctx.response.send_message(embed=embed, ephemeral=not optionChanged)

    @options.command(name="user", description="Use options")
    async def _user(
        self, 
        ctx : discord.ApplicationContext,
        language_overwrite : commands.Option(str, required=False, description="Language choice to overwrite your client language (default)", choices=["None (Client Default)"] + [l.fullName for l in lang.supported_languages]),
    ):
        lp = lang.private_command(self.bot.client, ctx) 
        optionChanged = False
        optUser = self.bot.client.options.get_user(ctx.author, lp)

        if language_overwrite != None:
            language_code = None

            if language_overwrite != "None (Client Default)":
                for l in lang.supported_languages:
                    if l.fullName == language_overwrite:
                        language_code = l.shortName

            
            optUser.languageOverwrite = language_code
            await optUser.save_json()

            optionChanged = True

        if optionChanged:
            lp = lang.private_command(self.bot.client, ctx) 
            optUser = self.bot.client.options.get_user(ctx.author, lp)

        embed = discord.Embed(title=lp.userOptions, description=lp.yourUserOptions, color=config.embed)
        embed.add_field(name=lp.languageOverwrite, value=optUser.languageOverwrite.fullName if optUser.languageOverwrite else "None (Client Language)")

        return await ctx.response.send_message(embed=embed, ephemeral=True)




def setup(bot):
    bot.add_cog(option(bot))
    