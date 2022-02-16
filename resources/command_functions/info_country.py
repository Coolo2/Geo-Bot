import discord 
from resources import client, geography

class ToggleFlagButton(discord.ui.Button):
    def __init__(self, country : geography.Country):
        self.country = country 

        super().__init__(
            style=discord.ButtonStyle.primary,
            label = "Show Map"
        )

    async def callback(self, interaction : discord.Interaction):
        
        embed = interaction.message.embeds[0]

        if embed.thumbnail.url == self.country.flag_url:
            embed.set_thumbnail(url=self.country.shape_image_url)
            self.label = "Show Flag"
        elif embed.thumbnail.url == self.country.shape_image_url:
            embed.set_thumbnail(url=self.country.flag_url)
            self.label = "Show Map"
        
        return await interaction.response.edit_message(embed=embed, view=self.view)

async def get_country_info_embed(client : client.Client, country : geography.Country, lp):
    flag_average_color = await country.get_flag_average_colour()

    embed = discord.Embed(title=lp.With(country.name).informationAbout, description=f"[{lp.locationMap}]({country.map_url})", color=flag_average_color)

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
    embed.add_field(name=lp.continent, value=f"{country.continent_name} ({country.subregion})")
    embed.add_field(name=lp.population, value=f"{country.population:,d} ({lp.With(country.get_population_rank(client)).rank})")
    embed.add_field(name=lp.area, value=f"{round(country.area):,d} km²")
    embed.add_field(name=lp.populationDensity, value=f"{round(country.population_density, 2) if country.population_density else 'Unknown '}/km²")
    embed.add_field(name=lp.averageMaleHeight, value=f"{country.avg_male_height if country.avg_male_height else 'Unknown '}cm")
    embed.add_field(name=lp.callingCode, value=f"+{country.calling_code if country.calling_code else 'Unknown'}")

    if len(country.domains) > 0:
        embed.add_field(name=lp.domains, value="`" + ("`, `".join(country.domains)) + "`", inline=False)
    
    embed.set_thumbnail(url=country.flag_url)

    

    return embed
