import discord 
import random

from resources import client, geography, games, lang

from resources.command_functions import guess_common

class CapitalModal(discord.ui.Modal):
    def __init__(self, client : client.Client, answer : geography.Country, game : games.CountryGuessGame, view : discord.ui.View, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answer = answer
        self.game = game
        self.client = client
        self.view = view
    
    async def callback(self, interaction : discord.Interaction):
        lp = lang.public_command(self.client, interaction)

        value = self.children[0].value 

        if str(interaction.user.id) not in self.game.guesses:
            self.game.guesses[str(interaction.user.id)] = 0

        if self.game.guesses[str(interaction.user.id)] >= 2:
            return await interaction.response.send_message(lp.alreadyUsedGuesses, ephemeral=True)

        self.game.guesses[str(interaction.user.id)] += 1

        totalGuesses = 0
        for userID in self.game.guesses:
            totalGuesses += self.game.guesses[userID]

        if value.lower() == self.answer.name.lower():

            await guess_common.end_game(self.client, self.answer, interaction, self.game, self.view, interaction.user, start_game)
        else:
            lpr = lang.private_command(interaction)

            await interaction.response.send_message(
                lpr.With(self.game.guesses[str(interaction.user.id)]).gotCapitalIncorrect,
                ephemeral=True
            )

            await interaction.message.edit(content=lp.With(self.answer.capitals[0], totalGuesses).capitalGameTitle)

async def start_game(client : client.Client, interaction : discord.Interaction, requestor : discord.Member):
    answer : geography.Country = random.choice(client.countries)
    game = client.games.create_country_game(interaction.user)
    lp = lang.public_command(client, interaction)
    print(answer.name)

    choose_button = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        emoji="🗳️",
        label=lp.capitalButtonLabel
    )

    choices_view = discord.ui.View()
    choices_view.add_item(choose_button)
    choices_view.add_item(guess_common.EndButton(client, game, answer, lp, start_game))

    modal = CapitalModal(client, answer, game, choices_view, title=lp.capitalModalTitle) # "Guess the country of the flag"

    modal_input_box = discord.ui.InputText(style=discord.InputTextStyle.singleline, placeholder=lp.capitalModalPlaceholder, label=lp.capitalModalLabel)
    modal.add_item(modal_input_box)

    async def choose_button_callback(interaction : discord.Interaction):
        await interaction.response.send_modal(modal)

    choose_button.callback = choose_button_callback

    return await interaction.response.send_message(
        lp.With(answer.capitals[0], 0).capitalGameTitle, 
        view=choices_view
    )
    