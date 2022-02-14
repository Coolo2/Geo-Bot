from resources import client, images, vars, lang
import discord 


async def get_stats_embed(client : client.Client, user : discord.User, language):
    economyUser = await client.economy.get_user(user)
    lp = language

    color = vars.embed 
    if user.avatar:
        color = images.get_average_color(images.get_image_from_data(await images.get_image_data(user.avatar.with_size(64).url)))

    embed = discord.Embed(title=lp.With(user=user).usersStats, color=color)

    w = lp.With(user=user, number=economyUser.balance)

    embed.add_field(name=lp.balance, value=w.usersBalance, inline=False)
    embed.add_field(name=lp.wins, value=w.usersWins, inline=False)
    embed.add_field(name=lp.losses, value=w.usersLosses, inline=False)
    if user.avatar:
        embed.set_thumbnail(url=user.avatar.url)

    return embed
    