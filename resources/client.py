import discord 
import requests
import datetime 
import json

from resources import vars, economy, games, images, color, geography, options, http


class Client():
    def __init__(self, bot : discord.Bot):
        self.bot = bot 
        self.economy = economy.Economy(self)
        self.options = options.Options(self)
        self.http = http.http(self)

        self.countries = []
        self.countries_raw = {}

        self.games = games.Games()

        self._get_countries()
        

    def _get_countries(self):
        print("Getting country data...")
        time_started = datetime.datetime.now()

        r = requests.get("https://restcountries.com/v3.1/all")
        self.countries_raw = r.json()
        #with open("resources/countries.json", encoding="utf8") as f:
        #    self.countries_raw = json.load(f)

        print(f"Got ({(datetime.datetime.now() - time_started).total_seconds()}s)")

        for country in self.countries_raw:
            
            if "independent" in country and country["independent"]:
                self.countries.append(
                    geography.Country(
                        country
                        
                    )
                )
    
    def get_country(self, countryName : str, ignoreCaps=False):
        for country in self.countries:
            if ignoreCaps and country.name.lower() == countryName.lower():
                return country 
            if not ignoreCaps and country.name == countryName:
                return country 
        
        return None


