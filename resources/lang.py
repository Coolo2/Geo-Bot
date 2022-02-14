import discord

from resources import client



class en:
    fullName = "English"
    shortName = "en"

    def wonTheGameCountryWas(user:str, country:str):
        return f"{user} won the game! The country was **{country}**"
    
    def userLostNowOn(user:str, nowOn:str):
        return f"{user} lost. They are now on {nowOn}"
    
    def gameFinished(totalGuesses:str, user:str, time:str):
        return f"**__Game Finished!__**\nGuesses: **{totalGuesses}**\nCorrect Guesser: {user}\nTime: **{time}**"
    
    def gotFlagIncorrect(user:str, guess:str):
        return f"{user} got the flag incorrect. (guess {guess}/2)"
    
    def flagGameTitle(guesses:str):
        return f"Use the buttons below to guess the flag's country\nGuesses: **{guesses}**"
    
    def gotCapitalIncorrect(user:str, guess:str):
        return f"{user} got the capital incorrect. (guess {guess}/2)"
    
    def capitalGameTitle(capital:str, guesses:str):
        return f"Use the buttons below to guess the capital's country\n__**{capital}**__\nGuesses: **{guesses}**"
    
    class With:
        def __init__(self, user:str = None, number:str = None):
            self.usersStats = f"{user}'s stats"
            self.usersBalance = f"{user} is on **{number}** credits"
            self.usersWins = f"{user} has **{number}** wins"
            self.usersLosses = f"{user} has **{number}** losses"
    
    wins = "Wins"
    balance = "Balance"
    
    alreadyUsedGuesses = "You have already used all 2 guesses!"
    flagButtonLabel = "Guess Flag Country"
    flagModalTitle = "Guess the country of the flag"
    flagModalLabel = "Country Name"
    flagModalPlaceholder = f"{flagModalLabel} (case insensitive)"

    capitalButtonLabel = "Guess Capital's Country"
    capitalModalTitle = "Guess the Capital City's country"
    capitalModalLabel = "Country Name"
    capitalModalPlaceholder = f"{capitalModalLabel} (case insensitive)"

    startNewGame = "Start New Game"
    startNewGameUsed = f"{startNewGame} (used)"

    endGame = "End Game"
    getStats = "Get Stats"

    losses = "Losses"
    gameEnded = "Game Ended"



class es:
    fullName = "Español"
    shortName = "es"

    def wonTheGameCountryWas(user:str, country:str):
        return f"¡{user} ganó el juego! El pais era **{country}**"
    
    def userLostNowOn(user:str, nowOn:str):
        return f"{user} perdido. Ellas han perdido {nowOn} veces"
    
    def gameFinished(totalGuesses:str, user:str, time:str):
        return f"**__Juego Terminado!__**\nSuposiciones: **{totalGuesses}**\nAdivinador correcto: {user}\nDuración: **{time}**"
    
    def gotFlagIncorrect(user:str, guess:str):
        return f"{user} adivinó la bandera incorrectamente. (intento {guess}/2)"
    
    def flagGameTitle(guesses:str):
        return f"Usa los botones de abajo para adivinar el país de la bandera\nSuposiciones: **{guesses}**"
    
    def gotCapitalIncorrect(user:str, guess:str):
        return f"{user} adivinó incorrectamente. (intento {guess}/2)"
    
    def capitalGameTitle(capital:str, guesses:str):
        return f"Usa los botones de abajo para adivinar el país de la ciudad capital\n__**{capital}**__\nSuposiciones: **{guesses}**"
    
    class With:
        def __init__(self, user:str = None, number:str = None):
            self.usersStats = f"Estadisticas de {user}"
            self.usersBalance = f"{user} tiene **{number}** creditos"
            self.usersWins = f"{user} tiene **{number}** victorias"
            self.usersLosses = f"{user} ha perdido **{number}** veces"
    
    wins = "Cantidad de ganancias"
    balance = "Saldo bancario"
    
    alreadyUsedGuesses = "¡Has usado los dos intentos!"
    flagButtonLabel = "Adivina el pais de la bandera"
    flagModalTitle = "Adivina el pais de la bandera"
    flagModalLabel = "Nombre del País"
    flagModalPlaceholder = f"{flagModalLabel}"

    capitalButtonLabel = "Adivina el país de la ciudad capital"
    capitalModalTitle = "Adivina el país de la ciudad capital"
    capitalModalLabel = "Nombre del País"
    capitalModalPlaceholder = f"{capitalModalLabel}"

    startNewGame = "Empieza un juego nuevo"
    startNewGameUsed = f"{startNewGame} (usado)"

    endGame = "Terminar el juego"
    getStats = "Obtener estadísticas"

    losses = "Pérdidas"
    gameEnded = "El juego termino"

default = en
supported_languages = [en, es]

def public_command(client : client.Client, interaction : discord.Interaction):
    optGuild = client.options.get_guild(interaction.guild)
    print(optGuild.language)

    if "en" in optGuild.language:
        return en
    elif "es" in optGuild.language:
        return es
    else:
        return default

def private_command(interaction : discord.Interaction):
    if "en" in interaction.locale:
        return en
    elif "es" in interaction.locale:
        return es
    else:
        return default