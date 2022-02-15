from resources import client, images, vars, lang
import discord 


async def get_stats_embed(client : client.Client, user : discord.User, language):
    economyUser = await client.economy.get_user(user)
    lp = language

    color = vars.embed 
    if user.avatar:
        color = images.get_average_color(images.get_image_from_data(await images.get_image_data(user.avatar.with_size(64).url)))

    embed = discord.Embed(title=lp.With(user).usersStats, color=color)


    embed.add_field(name=lp.balance, value=lp.With(user, economyUser.balance).usersBalance, inline=False)
    embed.add_field(name=lp.wins, value=lp.With(user, economyUser.wins).usersWins, inline=False)
    embed.add_field(name=lp.losses, value=lp.With(user, economyUser.losses).usersLosses, inline=False)
    if user.avatar:
        embed.set_thumbnail(url=user.avatar.url)

    return embed
    