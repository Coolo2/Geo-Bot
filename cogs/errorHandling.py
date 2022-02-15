import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import ApplicationCommandError, commands
from resources import config, errors, lang, color

class errorHandling(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    
    @cmds.Cog.listener()
    async def on_application_command_error(self, ctx : discord.ApplicationContext, error : ApplicationCommandError):

        lp = lang.private_command(ctx)
        
        msgMild = random.choice([lp.oops, lp.ohNo])
        msgUnkown = lp.ranIntoError
        
        if isinstance(error, cmds.CommandOnCooldown):
            embed = discord.Embed(title=msgMild, description=f"{error}", colour=config.embedFail)
            return await ctx.respond(embed=embed)
        if isinstance(error, cmds.CommandNotFound):
            pass

        if isinstance(error, commands.errors.ApplicationCommandInvokeError):
            if isinstance(error.original, cmds.MemberNotFound):
                embed = discord.Embed(title=msgMild, description=f"```{str(error.original)}```", colour=config.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed, ephemeral=True)
            if isinstance(error.original, cmds.MissingPermissions):
                embed = discord.Embed(title=msgMild, description=f"```{error.original}```", colour=config.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed, ephemeral=True)
            if isinstance(error.original, cmds.BotMissingPermissions):
                embed = discord.Embed(title=msgMild, 
                description=f"```{error.original}\n\nEnsure that I have the above permissions and my role is high enough to use /{ctx.command.name}```", 
                colour=config.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed, ephemeral=True)
            if isinstance(error.original, commands.errors.CheckFailure):
                embed = discord.Embed(title=msgMild, description=f"t", colour=config.embedFail)
                return await ctx.respond(embed=embed, ephemeral=True)

            # Custom errors
            if isinstance(error.original, errors.UnknownError):
                embed = discord.Embed(title=msgMild, description=f"```{error.original}```", colour=config.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed, ephemeral=True)
            if isinstance(error.original, errors.MildErr):
                embed = discord.Embed(title=msgMild, description=f"{error.original}", colour=config.embedFail)
                return await ctx.respond(embed=embed, ephemeral=True)

        print(f"{color.red}{error.__class__.__name__}{color.end} + {error}")
        embed = discord.Embed(title=msgUnkown, description=f"```{error}```", colour=config.embedFail, timestamp=datetime.datetime.now())
        await ctx.respond(embed=embed, ephemeral=True)
            
        


    
def setup(bot):
    bot.add_cog(errorHandling(bot))
    