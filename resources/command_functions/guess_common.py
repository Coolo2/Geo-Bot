from typing import Coroutine
from resources import client, geography, games, lang
import discord 
import datetime

from resources.command_functions import info_user

def calculate_guess_game_result(client: client.Client, user : discord.User, game : games.CountryGuessGame):

    userGuesses = game.guesses[str(user.id)]
    timeSinceStart : float = (datetime.datetime.now() - game.started).total_seconds()

    points_time = 0
    if timeSinceStart <= 10:
        points_time = round(10 - timeSinceStart)
    
    points_guesses = 3 - userGuesses 

    points = points_guesses + points_time 

    return points

async def end_game(
    client : client.Client, 
    answer : geography.Country, 
    interaction : discord.Interaction, 
    game : games.CountryGuessGame, 
    view : discord.ui.View,
    user : discord.User,
    start_game_callback : Coroutine
    
):
    if user == None:
        user_str = "None"
    else:
        user_str = user.mention

    lp = lang.public_command(client, interaction)

    losses = []
    timeSince = str(datetime.datetime.now() - game.started).split(".")[0]

    totalGuesses = 0
    for userID in game.guesses:
        totalGuesses += game.guesses[userID]

    for userID in game.guesses:
        if user == None or int(userID) != interaction.user.id:
            economyUser = await client.economy.get_user(id=int(userID))
            await economyUser.add(losses=1)
            losses.append(economyUser)

    embed = discord.Embed(
        title=f"{lp.gameEnded}!", 
        description=lp.wonTheGameCountryWas(user_str, answer.name), 
        colour=await answer.get_flag_average_colour()
    )

    lossesDescription = "_ _ "
    for lossEconomyUser in losses:
        lossesDescription += f"{lp.userLostNowOn(lossEconomyUser.user.mention, lossEconomyUser.losses)}\n"

    embed.set_thumbnail(url=answer.flag_url)
    embed.add_field(name=lp.losses, value=lossesDescription, inline=False)
    await interaction.response.send_message(embed=embed, view=NewGameView(client, start_game_callback)) # ADD THIS (NewGameView)

    for item in view.children:
        item.disabled = True 
    view.stop()

    await interaction.message.edit(
        content=lp.gameFinished(totalGuesses, user_str, timeSince), view=view)
    
    
    if user != None:
        economyUser = await client.economy.get_user(user=user)
        await economyUser.add(balance=calculate_guess_game_result(client, economyUser.user, game), wins=1)
    elif str(interaction.user.id) not in game.guesses:
        economyUser = await client.economy.get_user(user=interaction.user)
        await economyUser.add(losses=1)
        

class NewGameView(discord.ui.View):
    def __init__(self, client : client.Client, start_game_callback : Coroutine):
        self.client = client
        self.start_new_game = start_game_callback
        super().__init__()
    
    @discord.ui.button(style=discord.ButtonStyle.green, label=lang.en.startNewGame)
    async def start_new(self, button : discord.Button, interaction : discord.Interaction):
        lp = lang.public_command(self.client, interaction)

        button.disabled = True
        button.label =  lp.startNewGameUsed
        await interaction.message.edit(view=self)
        await self.start_new_game(self.client, interaction, interaction.user)
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label=lang.en.getStats)
    async def get_stats(self, button : discord.Button, interaction : discord.Interaction):
        lpr = lang.private_command(interaction)

        return await interaction.response.send_message(embed=await info_user.get_stats_embed(self.client, interaction.user, lpr), ephemeral=True)

class EndButton(discord.ui.Button):
    def __init__(self, client : client.Client, game : games.CountryGuessGame, answer : geography.Country, start_callback : Coroutine):
        self.answer = answer
        self.game = game
        self.client = client
        self.start_game = start_callback

        super().__init__(style=discord.ButtonStyle.red, label=lang.en.endGame)
    
    async def callback(self, interaction : discord.Interaction):
        await end_game(self.client, self.answer, interaction, self.game, self.view, None, self.start_game)
