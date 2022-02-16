import discord 
from resources import client, config, geography

async def get_city_info_embed(client : client.Client, city : geography.City, lp):

    city.get_country(client.countries)

    flag_average_color = await city.country.get_flag_average_colour() if city.country else config.embed

    embed = discord.Embed(title=lp.With(city.name).informationAbout, color=flag_average_color)

    embed.add_field(name=lp.country, value=f"{city.country.name if city.country else None} ({city.country.continent_name if city.country else None})", inline=False)
    embed.add_field(name=lp.population, value=f"{city.population:,d} ({lp.With(city.get_population_rank(client.cities)).rank})")
    
    if city.country:
        embed.set_thumbnail(url=city.country.flag_url)

    return embed
