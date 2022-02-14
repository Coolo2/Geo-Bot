
import discord 
import json



class Options():

    def __init__(self, client):
        self.client = client 
    
    def get_guild(self, guild : discord.Guild):
        return GuildOptions(self, guild)

class GuildOptions():

    def __init__(self, options : Options, guild : discord.Guild):
        self.guild = guild 
        self._options = options

        self._from_json(
            self._options.client.http.get_file_sync("data/options.json")
        )
    
    def _from_json(self, data : dict):
        if str(self.guild.id) in data:
            self.language = data[str(self.guild.id)]["language"]
        else:
            self.language = "en"
    
    def to_json(self):
        return {"language":self.language}

    async def save_json(self):
        dt = self._options.client.http.get_file_sync("data/options.json")

        dt[str(self.guild.id)] = self.to_json()
        return await self._options.client.http.save_to_file("data/options.json", dt)
