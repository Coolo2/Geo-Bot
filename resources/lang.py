import discord



class en:
    fullName = "English"
    shortName = "en"
    
    class With:
        def __init__(self, arg1 = None, arg2 = None, arg3=None, arg4=None, arg5=None):
            self.usersStats = f"{arg1}'s stats"
            self.usersBalance = f"{arg1} is on **{arg2}** credits (from **{arg3}** games)"
            self.usersWins = f"{arg1} has **{arg2}** wins"
            self.usersLosses = f"{arg1} has **{arg2}** losses"

            self.wonTheGameCountryWas = f"{arg1} won the game! The country was **{arg2}**"
            self.userLostNowOn = f"{arg1} lost. They are now on {arg2}"
            self.gameFinished = f"**__Game Finished!__**\nGuesses: **{arg1}**\nCorrect Guesser: {arg2}\nTime: **{arg3}**"
            self.gotFlagIncorrect = f"You got the flag incorrect. (guess {arg1}/2)"
            self.flagGameTitle = f"Use the buttons below to guess the flag's country\nGuesses: **{arg1}**"
            self.gotShapeIncorrect = f"You got the country incorrect. (guess {arg1}/2)"
            self.shapeGameTitle = f"Use the buttons below to guess the map's country\nGuesses: **{arg1}**"
            self.gotCapitalIncorrect = f"You got the capital incorrect. (guess {arg1}/2)"
            self.capitalGameTitle = f"Use the buttons below to guess the capital's country\n__**{arg1}**__\nGuesses: **{arg2}**"

            self.informationAbout = f"Information about {arg1}"
            self.rank = f"Rank `#{arg1}`"

            self.setLanguage = f"Successfully set language in this server to **{arg1}**"

            self.missingPermissions = f"You are missing permissions to do this. (Required: `{arg1}`)"

            self.description = f"**{arg1}** is a Discord bot written in Python by {arg2} and is owned by {arg3}"

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
    country = "Country"

    countryDoesNotExist = "Country does not exist."
    cityDoesNotExist = "City does not exist."
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

    shapeButtonLabel = "Guess Map Country"
    shapeModalTitle = "Guess the country of the map"
    shapeModalLabel = "Country Name"
    shapeModalPlaceholder = f"{flagModalLabel} (case insensitive)"

    startNewGame = "Start New Game"
    startNewGameUsed = f"{startNewGame} (used)"

    endGame = "End Game"
    getStats = "Get Stats"
    getCountryInfo = "Get Country Info"

    losses = "Losses"
    gameEnded = "Game Ended"

    noone = "No one"

    serverOptions = "Server options"
    allOptionsForServer = "All options for the server: "
    language = "Language"
    languages = "Languages"
    languageOverwrite = "Language Overwrite"


    ohNo = "Oh no!"
    oops = "Oops!"

    ranIntoError = "You have encountered an unknown error!"
    guildLanguageDisclaimer = "Guild language only affects public commands (guess games). Otherwise your Discord language is used."

    avgCreditsPerGame = "Average credits per game"
    winLossRatio = "Win:Loss"
    more =  "More"

    botInformation = "Bot information"
    totalGamesPlayeed = "Total games played"
    totalBalance = "Total balance"

    myCommands = "My commands"
    belowIsAListOfCommands = "Below is a list of all my commands. Use `/help command [command]` to get more info"
    commands = "Commands"
    showCommandList = "Show command list"

    multipleChoiceType = "Multiple Choice Type"

    userOptions = "User Options"
    yourUserOptions = "Your user options"

    area = "Area"
    populationDensity = "Population Density"
    averageMaleHeight = "Average Male Height"
    callingCode = "Calling Code"
    

class es:
    fullName = "Español"
    shortName = "es"
    
    class With:
        def __init__(self, arg1 = None, arg2 = None, arg3=None, arg4=None, arg5=None):
            self.usersStats = f"Estadisticas de {arg1}"
            self.usersBalance = f"{arg1} tiene **{arg2}** creditos (de **{arg3}** juegos)"
            self.usersWins = f"{arg1} tiene **{arg2}** victorias"
            self.usersLosses = f"{arg1} ha perdido **{arg2}** veces"

            self.wonTheGameCountryWas = f"¡{arg1} ganó el juego! El pais era **{arg2}**"
            self.userLostNowOn = f"{arg1} perdido. Ellas han perdido {arg2} veces"
            self.gameFinished = f"**__Juego Terminado!__**\nSuposiciones: **{arg1}**\nAdivinador correcto: {arg2}\nDuración: **{arg3}**"
            self.gotFlagIncorrect = f"Adivinaste la bandera incorrectamente. (intento {arg2}/2)"
            self.flagGameTitle = f"Usa los botones de abajo para adivinar el país de la bandera\nSuposiciones: **{arg1}**"
            self.gotShapeIncorrect = f"Tienes el país incorrecto. (intento {arg1}/2)"
            self.shapeGameTitle = f"Usa los botones de abajo para adivinar el país de la mapa\nSuposiciones: **{arg1}**"
            self.gotCapitalIncorrect = f"Adivinaste incorrectamente. (intento {arg2}/2)"
            self.capitalGameTitle = f"Usa los botones de abajo para adivinar el país de la ciudad capital\n__**{arg1}**__\nSuposiciones: **{arg2}**"

            self.informationAbout = f"Informacion sobre {arg1}"
            self.rank = f"Rango `#{arg1}`"

            self.setLanguage = f"Establecer con éxito la configuración de idioma en **{arg1}**"

            self.missingPermissions = f"Usted no tiene permiso para hacer esto. Necesitas permisos de `{arg1}`"
            self.description = f"**{arg1}** es un bot de Discord escrito en Python por {arg2} y es propiedad de {arg3}"

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
    country = "País"

    countryDoesNotExist = "Ese pais no existe."
    cityDoesNotExist = "Esa ciudad no existe."
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

    shapeButtonLabel = "Adivina el país de los mapas"
    shapeModalTitle = "Adivina el país de los mapas"
    shapeModalLabel = "Nombre del país"
    shapeModalPlaceholder = f"{flagModalLabel}"

    startNewGame = "Empieza un juego nuevo"
    startNewGameUsed = f"{startNewGame} (usado)"

    endGame = "Terminar el juego"
    getStats = "Obtener estadísticas"
    getCountryInfo = "Obtener información del país"

    losses = "Pérdidas"
    gameEnded = "El juego termino"

    noone = "No uno"

    serverOptions = "Ajustes del servidor"
    allOptionsForServer = "Todas los ajustes para el servidor: "
    language = "Idioma"
    languages = "Idiomas"
    languageOverwrite = "Sobrescribir idioma"

    ohNo = "¡Oh no!"
    oops = "¡Ups!"

    ranIntoError = "¡Te has encontrado con un error!"
    guildLanguageDisclaimer = "El idioma del servidor solo afecta a los comandos públicos (juegos de adivinanzas). De lo contrario, se utiliza su lenguaje Discord"

    avgCreditsPerGame = "Créditos promedio por juego"
    winLossRatio = "Victoria:Pérdida"
    more = "Más"

    botInformation = "Información del bot"
    totalGamesPlayeed = "Juegos totales jugados"
    totalBalance = "Saldo total de la cuenta"

    myCommands = "Mis comandos"
    belowIsAListOfCommands = "A continuación hay una lista de todos mis comandos. Use `/help command [command]` para obtener más información"
    commands = "Comandos"

    showCommandList = "Mostrar lista de comandos"

    multipleChoiceType = "Tipo de opción múltiple"

    userOptions = "Opciones de usuario"
    yourUserOptions = "Sus opciones de usuario"

    area = "Área"
    populationDensity = "Densidad de población"
    averageMaleHeight = "Altura media masculina"
    callingCode = "Código de llamada"



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

def private_command(client, interaction : discord.Interaction) -> en | es:
    lang = default

    if "en" in interaction.locale:
        lang = en
    elif "es" in interaction.locale:
        lang = es
    
    optUser = client.options.get_user(interaction.user, lang)

    return optUser.language
        