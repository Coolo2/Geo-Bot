
import discord

from discord.ext import commands as cmds
from discord import commands
from resources import errors, geography, lang
from resources.command_functions import info_user, info_country, info_city

async def country_autocomplete(ctx : discord.AutocompleteContext):
    countries = []
    for country in ctx.bot.client.all_countries:
        if not ctx.focused or ctx.value.lower() in country.name.lower():
            countries.append(country.name)
    return countries[:25]

async def city_autocomplete(ctx : discord.AutocompleteContext):
    cities = []
    for city in ctx.bot.client.cities:
        if not ctx.focused or ctx.value.lower() in city.name.lower():
            cities.append(f"{city.name}, {city.country_code}")
    return cities[:25]


class info(cmds.Cog):
    def __init__(self, bot):
        self.bot= bot

    info_commands = commands.SlashCommandGroup("info", "All information commands. Balance, userinfo etc")

    @info_commands.command(name="user", description="Get your balances, wins, losses and stats")
    async def _user(self, ctx : discord.ApplicationContext, user : discord.Option(discord.User, "The user to get information for", required=False)):
        await self.bot.client.options.get_guild(ctx.guild).init(ctx)

        if user == None:
            user = ctx.author
        
        language = lang.private_command(self.bot.client, ctx)

        return await ctx.respond(embed=await info_user.get_stats_embed(self.bot.client, user, language))
    
    @info_commands.command(name="country", description="Get information about a country")
    async def _country(self, ctx : discord.ApplicationContext, country : discord.Option(str, description="The country to get information on", autocomplete=country_autocomplete)):
        await self.bot.client.options.get_guild(ctx.guild).init(ctx)

        lp = lang.private_command(self.bot.client, ctx)

        country : geography.Country = self.bot.client.get_country(country, ignoreCaps=True)

        if not country:
            raise errors.MildErr(lp.countryDoesNotExist)
        
        view = discord.ui.View()
        view.add_item(info_country.ToggleFlagButton(country))

        view.message = await ctx.respond(embed=await info_country.get_country_info_embed(self.bot.client, country, lp), view=view)
    
    @info_commands.command(name="city", description="Get information about a city")
    async def _city(self, ctx : discord.ApplicationContext, city : discord.Option(str, description="The city to get information on", autocomplete=city_autocomplete)):
        await self.bot.client.options.get_guild(ctx.guild).init(ctx)

        lp = lang.private_command(self.bot.client, ctx)

        country_code = None
        if ", " in city:
            country_code = city.split(", ")[1]
            city = city.split(", ")[0]
            

        city : geography.City = self.bot.client.get_city(city, countryCode=country_code, ignoreCaps=True)

        if not city:
            raise errors.MildErr(lp.cityDoesNotExist)

        await ctx.respond(embed=await info_city.get_city_info_embed(self.bot.client, city, lp))
        


    
def setup(bot):
    bot.add_cog(info(bot))
    