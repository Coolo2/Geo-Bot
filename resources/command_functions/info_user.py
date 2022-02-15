from resources import client, config, images
import discord 


async def get_stats_embed(client : client.Client, user : discord.User, language):
    economyUser = await client.economy.get_user(user)
    lp = language

    color = config.embed 
    if user.avatar:
        color = images.get_average_color(images.get_image_from_data(await images.get_image_data(user.avatar.with_size(64).url)))

    embed = discord.Embed(title=lp.With(user).usersStats, color=color)

    totalGames = (economyUser.wins + economyUser.losses)

    moreStats = f"""
{lp.winLossRatio} - **{round(economyUser.wins / economyUser.losses, 2) if economyUser.losses != 0 else 0}**
{lp.avgCreditsPerGame} - **{round(economyUser.balance / totalGames) if totalGames != 0 else 0}**
    """

    embed.add_field(name=lp.balance, value=lp.With(user, economyUser.balance, totalGames).usersBalance, inline=False)
    embed.add_field(name=lp.wins, value=lp.With(user, economyUser.wins).usersWins, inline=False)
    embed.add_field(name=lp.losses, value=lp.With(user, economyUser.losses).usersLosses, inline=False)
    embed.add_field(name=lp.more, value=moreStats, inline=True)
    if user.avatar:
        embed.set_thumbnail(url=user.avatar.url)

    return embed
    