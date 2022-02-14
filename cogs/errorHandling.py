import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import ApplicationCommandError, commands
from resources import client, vars, images, errors

from EasyConversion import textformat 

class errorHandling(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    @cmds.Cog.listener()
    async def on_application_command_error(self, ctx : discord.ApplicationContext, error : ApplicationCommandError):
        
        msgMild = random.choice(["Uh oh!", "Oops!", "Oh no!"])
        msgUnkown = random.choice(["You've ran into an unknown error!", "You've ran into an error!"])
        
        if isinstance(error, cmds.CommandOnCooldown):
            embed = discord.Embed(title=msgMild, description=f"{error}", colour=vars.embedFail)
            return await ctx.respond(embed=embed)
        if isinstance(error, cmds.CommandNotFound):
            pass

        if isinstance(error, commands.errors.ApplicationCommandInvokeError):
            if isinstance(error.original, cmds.MemberNotFound):
                embed = discord.Embed(title=msgMild, description=f"```{str(error.original)}```", colour=vars.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed)
            if isinstance(error.original, cmds.MissingPermissions):
                embed = discord.Embed(title=msgMild, description=f"```{error.original}```", colour=vars.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed)
            if isinstance(error.original, cmds.BotMissingPermissions):
                embed = discord.Embed(title=msgMild, 
                description=f"```{error.original}\n\nEnsure that I have the above permissions and my role is high enough to use /{ctx.command.name}```", 
                colour=vars.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed)
            if isinstance(error.original, commands.errors.CheckFailure):
                embed = discord.Embed(title=msgMild, description=f"t", colour=vars.embedFail)
                return await ctx.respond(embed=embed)

            # Custom errors
            if isinstance(error.original, errors.UnknownError):
                embed = discord.Embed(title=msgMild, description=f"```{error.original}```", colour=vars.embedFail, timestamp=datetime.datetime.now())
                return await ctx.respond(embed=embed)
            if isinstance(error.original, errors.MildErr):
                embed = discord.Embed(title=msgMild, description=f"{error.original}", colour=vars.embedFail)
                return await ctx.respond(embed=embed)

        print(f"{textformat.color.red}{error.__class__.__name__}{textformat.color.end} + {error}")
        embed = discord.Embed(title=msgUnkown, description=f"```{error}```", colour=vars.embedFail, timestamp=datetime.datetime.now())
        await ctx.respond(embed=embed)
            
        


    
def setup(bot):
    bot.add_cog(errorHandling(bot))