import datetime 
import random
import discord

class CountryGuessGame():
    def __init__(self, starter : discord.User, id : int):
        self.id = id
        self.guesses = {}
        self.started = datetime.datetime.now()
        self.starter = starter

class Games():
    def __init__(self):
        self.games = {}
    
    def create_country_game(self, starter : discord.User):
        gameID = random.randint(1_000_000_000, 9_999_999_999)

        self.games[str(gameID)] = CountryGuessGame(starter, gameID)

        return self.games[str(gameID)]

    def get_game(self, gameID : int) -> CountryGuessGame:
        return self.games[str(gameID)] if str(gameID) in self.games else None
    
    def end_game(self, gameID : int):
        game = self.games[str(gameID)]
        del self.games[str(gameID)]
        return game

