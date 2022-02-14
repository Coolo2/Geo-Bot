
import discord
import json


class EconomyUser():
    def __init__(self, client, user : discord.User, balance : int, wins : int, losses : int):
        self.client = client
        self.user = user

        self.balance = balance 
        self.wins = wins
        self.losses = losses
    
    async def add(self, balance : int = 0, wins : int = 0, losses : int = 0):
        self.balance += balance 
        self.wins += wins 
        self.losses += losses

        final_user = await self.client.economy._set_user(self)
        return final_user
    
    def to_json(self):
        return {"wins":self.wins, "losses":self.losses, "balance":self.balance}

class Economy():
    def __init__(self, client):
        self.client = client

    async def _get_economy(self):
        return await self.client.http.get_file("data/economy.json")
    
    async def _save_economy(self, data : json):
        await self.client.http.save_to_file("data/economy.json", data)
    
    async def _set_user(self, user : EconomyUser):
        data = await self._get_economy()

        data[str(user.user.id)] = user.to_json()

        await self._save_economy(data)

        return user

    async def get_user(self, user = None, id = None) -> EconomyUser:
        data = await self._get_economy()

        user_id : int = None 
        if user != None:
            user_id = user.id 
        else:
            user_id = int(id)

        user = self.client.bot.get_user(int(user_id))
        if not user:
            user = await self.client.bot.fetch_user(int(user_id))
            
        
        if str(user_id) in data:
            return EconomyUser(
                client = self.client,
                user = user,
                balance = data[str(user_id)]["balance"],
                wins=data[str(user_id)]["wins"],
                losses=data[str(user_id)]["losses"]
            )
        else:
            return EconomyUser(
                self.client, 
                user,
                0,
                0,
                0
            )

