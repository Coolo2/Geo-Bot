import discord 
import json

from resources import economy, games, geography, options, http


class Client():
    def __init__(self, bot : discord.Bot):
        self.bot = bot 
        self.economy = economy.Economy(self)
        self.options = options.Options(self)
        self.http = http.http(self)

        self.countries = []
        self.all_countries = []

        self.cities = []

        self.games = games.Games()

        self._get_countries()
        self._get_cities()
        

    def _get_countries(self):
        print("Getting country data...")

        with open("resources/json/countries.json", encoding="utf8") as f:
            countries_raw = json.load(f)

        for country in countries_raw:
            if "independent" in country and country["independent"]:
                self.countries.append(
                    geography.Country(
                        country
                        
                    )
                )
            self.all_countries.append(
                geography.Country(
                    country
                        
                )
            )
    
    def _get_cities(self):
        print("Getting city data...")
        with open("resources/json/cities.json", encoding="utf8") as f:
            cities = json.load(f)
        
        for city in cities:
            self.cities.append(geography.City(city[0], city[1], city[2]))
    
    def get_country(self, countryName : str, ignoreCaps=False):
        for country in self.all_countries:
            if ignoreCaps and country.name.lower() == countryName.lower():
                return country 
            if not ignoreCaps and country.name == countryName:
                return country 
        
        return None
    
    def get_city(self, cityName : str, countryCode : str = None, ignoreCaps=False):
        for city in self.cities:
            if ignoreCaps and city.name.lower() == cityName.lower() and (countryCode == None or countryCode == city.country_code):
                return city 
            if not ignoreCaps and city.name == cityName and (countryCode == None or countryCode == city.country_code):
                return city 
        
        return None


