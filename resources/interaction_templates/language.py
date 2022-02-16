

import discord 

from resources import client, lang, errors, options

class LanguageSelector(discord.ui.Select):
    def __init__(self, bot : discord.Bot, *args, **kwargs):
        self.bot = bot 

        options = []
        languageStr = ""

        for language in lang.supported_languages:
            options.append(discord.SelectOption(label=language.fullName))
            languageStr += f"{language.language} - "
        
        super().__init__(
            placeholder=languageStr[:100],
            min_values=1,
            max_values=1,
            options=options,
            *args, 
            **kwargs
        )
    
    async def callback(self, interaction : discord.Interaction):

        lp = lang.private_command(self.bot.client, interaction)

        if not interaction.user.guild_permissions.manage_guild:
            return await interaction.response.send_message(lp.With("MANAGE_SERVER").missingPermissions, ephemeral=True)
        
        guildOpt : options.GuildOptions = self.bot.client.options.get_guild(interaction.guild)

        language_code = None
        for l in lang.supported_languages:
            if l.fullName == self.values[0]:
                language_code = l.shortName

        guildOpt.language = language_code

        await guildOpt.save_json()

        return await interaction.response.send_message(content=lp.With(self.values[0]).setLanguage, ephemeral=True)


