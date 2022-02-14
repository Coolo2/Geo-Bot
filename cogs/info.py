import discord
import random
import datetime

from discord.ext import commands as cmds
from discord import commands
from resources import client, vars, images, errors, geography, lang
from resources.command_functions import info_user

async def country_autocomplete(ctx : discord.AutocompleteContext):
    countries = []
    for country in ctx.bot.client.countries:
        if not ctx.focused or ctx.value.lower() in country.name.lower():
            countries.append(country.name)
    return countries


class info(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    info_commands = commands.SlashCommandGroup("info", "All information commands. Balance, userinfo etc")

    @info_commands.command(name="user", description="Get your balances, wins, losses and stats")
    async def _user(self, ctx : discord.Interaction, user : discord.Option(discord.User, "The user to get information for", required=False)):

        if user == None:
            user = ctx.author
        
        language = lang.public_command(self.bot.client, ctx)

        return await ctx.respond(embed=await info_user.get_stats_embed(self.bot.client, user, language))
    
    @info_commands.command(name="country", description="Get information about a country")
    async def _country(self, ctx : discord.ApplicationContext, country : discord.Option(str, description="The country to get information on", autocomplete=country_autocomplete)):

        country : geography.Country = self.bot.client.get_country(country, ignoreCaps=True)

        if not country:
            raise errors.MildErr("Country does not exist.")
        
        flag_average_color = await country.get_flag_average_colour()

        embed = discord.Embed(title=f"Information about {country.name}", description=f"[Location (map)]({country.map_url})", color=flag_average_color)

        embed.add_field(
            name="Official " + ("language" if len(country.languages) == 1 else "languages"), 
            value=(", ".join(country.languages)), 
            inline=False
        )
        embed.add_field(
            name="Capital " + ("city" if len(country.capitals) == 1 else "cities"), 
            value=(", ".join(country.capitals)), 
            inline=False
        )
        embed.add_field(
            name="Currency" if len(country.capitals) == 1 else "Currencies", 
            value=(", ".join(f"{currency.name} (`{currency.symbol}`)" for currency in country.currencies)), 
            inline=False
        )
        embed.add_field(name="Continent", value=f"{country.continent_name} ({country.subregion})", inline=False)
        embed.add_field(name="Population", value=f"{country.population:,d} (Rank `#{country.get_population_rank(self.bot.client)}`)")

        if len(country.domains) > 0:
            embed.add_field(name="Domains", value="`" + ("`".join(country.domains)) + "`", inline=False)
        
        embed.set_thumbnail(url=country.flag_url)

        return await ctx.respond(embed=embed)
        


    
def setup(bot):
    bot.add_cog(info(bot))