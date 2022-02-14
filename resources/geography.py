
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

        self.capitals = country_data["capital"]
        self.continent_name = country_data["region"]
        self.subregion = country_data["subregion"]

        self.domains = country_data["tld"]
        self.population = country_data["population"]

        self.languages = list(country_data["languages"].values())

        self.currencies = [Currency(currency["symbol"] if "symbol" in currency else None, currency["name"]) for currency in country_data["currencies"].values()]

        #self.raw = country_data
    
    async def get_image(self):
        return await images.get_image_data(self.flag_url)
    
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


