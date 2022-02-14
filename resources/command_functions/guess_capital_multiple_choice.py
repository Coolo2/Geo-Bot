from typing import List
import discord 
import datetime 
import random

from resources import client, vars, geography, games, lang

from resources.command_functions import guess_common

class CapitalDropdown(discord.ui.Select):
    def __init__(self, client : client.Client, answer : geography.Country, country_choices : List[geography.Country], game : games.CountryGuessGame, *args, **kwargs):
        self.answer = answer
        self.game = game
        self.client = client
        self.country_choices = country_choices

        options = []

        for country in self.country_choices:
            options.append(discord.SelectOption(label=country.name))
        
        super().__init__(
            placeholder="Choose the country of this capital city",
            min_values=1,
            max_values=1,
            options=options
        )
    
    async def callback(self, interaction : discord.Interaction):
        lp = lang.public_command(self.client, interaction)

        value = self.values[0]

        if str(interaction.user.id) not in self.game.guesses:
            self.game.guesses[str(interaction.user.id)] = 0

        if self.game.guesses[str(interaction.user.id)] >= 2:
            return await interaction.response.send_message(lp.alreadyUsedGuesses, ephemeral=True)

        self.game.guesses[str(interaction.user.id)] += 1

        totalGuesses = 0
        for userID in self.game.guesses:
            totalGuesses += self.game.guesses[userID]

        if value.lower() == self.answer.name.lower():
            self.placeholder = f"ANSWER: {self.answer.name}"

            await guess_common.end_game(self.client, self.answer, interaction, self.game, self.view, interaction.user, start_game)
        else:
            lpr= lang.private_command(interaction)
            await interaction.response.send_message(
                lpr.gotCapitalIncorrect(interaction.user.mention, self.game.guesses[str(interaction.user.id)]),
                ephemeral=True
            )

            await interaction.message.edit(content=lp.flagGameTitle(totalGuesses))

async def start_game(client : client.Client, interaction : discord.Interaction, requestor : discord.Member):
    answer : geography.Country = random.choice(client.countries)
    game = client.games.create_country_game(interaction.user)
    lp = lang.public_command(client, interaction)
    country_choices = []

    print(answer.name)

    choices_view = discord.ui.View()

    for i in range(10):
        country_random : geography.Country = random.choice(client.countries)
        while country_random in country_choices:
            country_random = random.choice(client.countries)
        country_choices.append(country_random)
    
    countryIndex = random.randint(0, len(country_choices)-1)
    country_choices[countryIndex] = answer
        
    dropdown = CapitalDropdown(client, answer, country_choices, game, title=lp.flagModalTitle)

    choices_view.add_item(dropdown)
    choices_view.add_item(guess_common.EndButton(client, game, answer, start_game))

    return await interaction.response.send_message(
        lp.capitalGameTitle(answer.capitals[0], 0), 
        view=choices_view
    )