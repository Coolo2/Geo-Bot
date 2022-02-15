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
    async def _user(self, ctx : discord.ApplicationContext, user : discord.Option(discord.User, "The user to get information for", required=False)):
        await self.bot.client.options.get_guild(ctx.guild).init(ctx)

        if user == None:
            user = ctx.author
        
        language = lang.private_command(ctx)

        return await ctx.respond(embed=await info_user.get_stats_embed(self.bot.client, user, language))
    
    @info_commands.command(name="country", description="Get information about a country")
    async def _country(self, ctx : discord.ApplicationContext, country : discord.Option(str, description="The country to get information on", autocomplete=country_autocomplete)):
        await self.bot.client.options.get_guild(ctx.guild).init(ctx)

        lp = lang.private_command(ctx)

        country : geography.Country = self.bot.client.get_country(country, ignoreCaps=True)

        if not country:
            raise errors.MildErr(lp.countryDoesNotExist)
        
        flag_average_color = await country.get_flag_average_colour()

        embed = discord.Embed(title=lp.With(country.name).informationAboutCountry, description=f"[{lp.locationMap}]({country.map_url})", color=flag_average_color)

        embed.add_field(
            name=lp.officialLanguage if len(country.languages) == 1 else lp.officialLanguages, 
            value=(", ".join(country.languages)), 
            inline=False
        )
        embed.add_field(
            name=lp.capitalCity if len(country.capitals) == 1 else lp.capitalCities, 
            value=(", ".join(country.capitals)), 
            inline=False
        )
        embed.add_field(
            name=lp.currency if len(country.capitals) == 1 else lp.currencies, 
            value=(", ".join(f"{currency.name} (`{currency.symbol}`)" for currency in country.currencies)), 
            inline=False
        )
        embed.add_field(name=lp.continent, value=f"{country.continent_name} ({country.subregion})", inline=False)
        embed.add_field(name=lp.population, value=f"{country.population:,d} ({lp.With(country.get_population_rank(self.bot.client)).rank})")

        if len(country.domains) > 0:
            embed.add_field(name=lp.domains, value="`" + ("`".join(country.domains)) + "`", inline=False)
        
        embed.set_thumbnail(url=country.flag_url)

        return await ctx.respond(embed=embed)
        


    
def setup(bot):
    bot.add_cog(info(bot))