import discord

from resources import client



class en:
    fullName = "English"
    shortName = "en"
    
    class With:
        def __init__(self, arg1 = None, arg2 = None, arg3=None, arg4=None, arg5=None):
            self.usersStats = f"{arg1}'s stats"
            self.usersBalance = f"{arg1} is on **{arg2}** credits"
            self.usersWins = f"{arg1} has **{arg2}** wins"
            self.usersLosses = f"{arg1} has **{arg2}** losses"

            self.wonTheGameCountryWas = f"{arg1} won the game! The country was **{arg2}**"
            self.userLostNowOn = f"{arg1} lost. They are now on {arg2}"
            self.gameFinished = f"**__Game Finished!__**\nGuesses: **{arg1}**\nCorrect Guesser: {arg2}\nTime: **{arg3}**"
            self.gotFlagIncorrect = f"{arg1} got the flag incorrect. (guess {arg2}/2)"
            self.flagGameTitle = f"Use the buttons below to guess the flag's country\nGuesses: **{arg1}**"
            self.gotCapitalIncorrect = f"{arg1} got the capital incorrect. (guess {arg2}/2)"
            self.capitalGameTitle = f"Use the buttons below to guess the capital's country\n__**{arg1}**__\nGuesses: **{arg2}**"

            self.informationAboutCountry = f"Information about {arg1}"
            self.rank = f"Rank `#{arg1}`"

            self.setLanguage = f"Successfully set language in this server to **{arg1}**"

            self.missingPermissions = f"You are missing permissions to do this. (Required: `{arg1}`)"

    didntStartGame = "You didn't start this game, therefore cannot stop it."

    officialLanguage = "Official Language"
    officialLanguages = "Official Languages"
    capitalCity = "Capital city"
    capitalCities = "Capital cities"
    currency = "Currency"
    currencies = "Currencies"
    continent = "Continent"
    population = "Population"
    domains = "Domains"

    countryDoesNotExist = "Country does not exist."
    locationMap = "Location (map)"
    
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

    noone = "No one"

    serverOptions = "Server options"
    allOptionsForServer = "All options for the server: "
    language = "Language"
    languages = "Languages"


    ohNo = "Oh no!"
    oops = "Oops!"

    ranIntoError = "You have encountered an unknown error!"

    

class es:
    fullName = "Español"
    shortName = "es"
    
    class With:
        def __init__(self, arg1 = None, arg2 = None, arg3=None, arg4=None, arg5=None):
            self.usersStats = f"Estadisticas de {arg1}"
            self.usersBalance = f"{arg1} tiene **{arg2}** creditos"
            self.usersWins = f"{arg1} tiene **{arg2}** victorias"
            self.usersLosses = f"{arg1} ha perdido **{arg2}** veces"

            self.wonTheGameCountryWas = f"¡{arg1} ganó el juego! El pais era **{arg2}**"
            self.userLostNowOn = f"{arg1} perdido. Ellas han perdido {arg2} veces"
            self.gameFinished = f"**__Juego Terminado!__**\nSuposiciones: **{arg1}**\nAdivinador correcto: {arg2}\nDuración: **{arg3}**"
            self.gotFlagIncorrect = f"{arg1} adivinó la bandera incorrectamente. (intento {arg2}/2)"
            self.flagGameTitle = f"Usa los botones de abajo para adivinar el país de la bandera\nSuposiciones: **{arg1}**"
            self.gotCapitalIncorrect = f"{arg1} adivinó incorrectamente. (intento {arg2}/2)"
            self.capitalGameTitle = f"Usa los botones de abajo para adivinar el país de la ciudad capital\n__**{arg1}**__\nSuposiciones: **{arg2}**"

            self.informationAboutCountry = f"Informacion sobre {arg1}"
            self.rank = f"Rango `#{arg1}`"

            self.setLanguage = f"Establecer con éxito la configuración de idioma en **{arg1}**"

            self.missingPermissions = f"Usted no tiene permiso para hacer esto. Necesitas permisos de `{arg1}`"

    didntStartGame = "No comenzaste el juego, por lo tanto no puedes terminarlo"

    officialLanguage = "Idioma oficial"
    officialLanguages = "Idiomas oficiales"
    capitalCity = "Ciudad capital"
    capitalCities = "Ciudades capitales"
    currency = "Divisa"
    currencies = "Divisas"
    continent = "Continente"
    population = "Población"
    domains = "Dominios de la red"

    countryDoesNotExist = "Ese pais no existe."
    locationMap = "Ubicación en el mapa"
    
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

    noone = "No uno"

    serverOptions = "Ajustes del servidor"
    allOptionsForServer = "Todas los ajustes para el servidor: "
    language = "Idioma"
    languages = "Idiomas"

    ohNo = "¡Oh no!"
    oops = "¡Ups!"

    ranIntoError = "¡Te has encontrado con un error!"

    


default = en
supported_languages = [en, es]

def get_language(shortName : str):
    for language in supported_languages:
        if language.shortName == shortName:
            return language 
    
    return None

def public_command(client, interaction : discord.Interaction):
    optGuild = client.options.get_guild(interaction.guild)

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