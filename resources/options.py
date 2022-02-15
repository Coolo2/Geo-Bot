
import discord 

from resources import lang

class Options():

    def __init__(self, client):
        self.client = client 
    
    def get_guild(self, guild : discord.Guild):
        return GuildOptions(self, guild)

class GuildOptions():

    def __init__(self, options : Options, guild : discord.Guild):
        self.guild = guild 
        self._options = options
        self.data = None

        self._from_json(
            self._options.client.http.get_file_sync("data/options.json")
        )
    
    async def init(self, interaction : discord.Interaction):
        if "guilds" not in self.data or str(interaction.guild.id) not in self.data["guilds"] or "language" not in self.data["guilds"][str(interaction.guild.id)]:
            
            self.language = lang.private_command(interaction).shortName 

            await self.save_json()

        return self.language
    
    def _from_json(self, data : dict):
        self.data = data 

        if "guilds" in data and str(self.guild.id) in data["guilds"]:
            self.language = data["guilds"][str(self.guild.id)]["language"]
        else:
            self.language = "en"
    
    def to_json(self):
        return {"language":self.language}

    async def save_json(self):
        dt = self._options.client.http.get_file_sync("data/options.json")

        if "guilds" not in dt:
            dt["guilds"] = {}

        dt["guilds"][str(self.guild.id)] = self.to_json()
        print(dt)
        return await self._options.client.http.save_to_file("data/options.json", dt)
