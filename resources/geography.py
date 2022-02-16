
from typing import List
from resources import images

class Currency():
    def __init__(self, symbol : str, name : str):
        self.symbol = symbol 
        self.name = name 

class Country():
    def __init__(self, country_data : dict):

        self.code = country_data["cca2"] 
        self.name = country_data["name"]["common"] 
        self.flag_url = country_data["flags"]["png"]
        self.flag_url_low_res = self.flag_url.replace("w320", "w40")

        self.map_url = country_data["maps"]["googleMaps"]

        self.capitals = country_data["capital"] if "capital" in country_data else []
        self.continent_name = country_data["region"]
        self.subregion = country_data["subregion"] if "subregion" in country_data else None

        self.domains = country_data["tld"] if "tld" in country_data else None
        self.population = country_data["population"]

        self.languages = list(country_data["languages"].values()) if "languages" in country_data else []

        self.currencies = [Currency(currency["symbol"] 
            if "symbol" in currency else None, currency["name"]) 
            for currency in country_data["currencies"].values()] if "currencies" in country_data else []

        self.shape_image_url = f"https://raw.githubusercontent.com/djaiss/mapsicon/master/all/{self.code.lower()}/1024.png"

        #self.raw = country_data
    
    async def get_flag_image(self):
        return await images.get_image_data(self.flag_url)
    
    async def get_shape_image(self):
        return await images.get_image_data(self.shape_image_url)
    
    async def get_flag_average_colour(self):
        return images.get_average_color(images.get_image_from_data(await images.get_image_data(self.flag_url_low_res)))
    
    def get_population_rank(self, client):
        global_populations = sorted([country.population for country in client.countries], reverse=True)
        
        self.population_rank = 0
        for country_population in global_populations:
            self.population_rank += 1
            if country_population == self.population:
                break 
        
        return self.population_rank

class City():
    def __init__(self, name : str, country_code : str, population : str):
        self.name = name 
        self.country_code = country_code
        self.population = int(population)
        self.country = None
    
    def get_country(self, countries : List[Country]) -> Country:
        for country in countries:
            if country.code.upper() == self.country_code:
                self.country = country
        
                return country
    
    def get_population_rank(self, cities : List):
        global_populations = sorted([city.population for city in cities], reverse=True)
        
        self.population_rank = 0
        for city_population in global_populations:
            self.population_rank += 1
            if city_population == self.population:
                break 
        
        return self.population_rank


