import time
import random

import cloudscraper
from numpy import unicode
from pymongo import MongoClient

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
import discord
from discord.ext import commands

scraper = cloudscraper.create_scraper(browser={
    'browser': 'firefox',
    'platform': 'windows',
    'mobile': False
})


class Mines(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def mines(self, ctx: commands.Context, robux, bombs, spots):
        ok = await ctx.respond(embed=discord.Embed(description="Connecting to API", color=discord.Color.yellow()))
        userid = ctx.author.id
        dbuser = cluster["users"]
        cursor = dbuser[f"{userid}"]
        check = cursor.find_one({"id": userid})

        if check is None:
            await ok.edit_original_message(
                embed=discord.Embed(description=f"No Account", color=0xe81a1a))
        else:
            token = check['token']
            fuckery = scraper.get(f'https://api.bloxflip.com/user', headers={'x-auth-token': token}).json()
            user = fuckery['user']
            wallet = user['wallet']
            if float(robux) > wallet:
                await ok.edit_original_message(
                    embed=discord.Embed(description=f"Sorry you don't have enough robux", color=0xe81a1a))
            elif float(robux) <= wallet:
                if float(bombs) == 1 and float(spots) == 1:
                    await ok.edit_original_message(
                        embed=discord.Embed(description=f"Error", color=0xe81a1a))
                else:
                    start = scraper.post(f'https://api.bloxflip.com/games/mines/create',
                                         headers={'x-auth-token': token},
                                         json={'betAmount': robux, 'mines': bombs}).json()
                    checker = start['success']
                    if checker == True:
                        if float(spots) == 1:
                            spot = random.choice(list(range(0, 24)))
                            cashfalse = "false"
                            placemine = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                     headers={'x-auth-token': token},
                                                     json={'cashout': False, 'mine': spot}).json()

                            explosion = placemine['exploded']
                            if explosion == True:
                                end = placemine
                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                   headers={'x-auth-token': token}).json()
                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                game = end['game']
                                uncover = game['uncoveredLocations']
                                badmine = game['badMineUncovered']
                                mines = game['mineLocations']

                                b = badmine
                                a = uncover
                                if a == 1:
                                    mine1 = "🟩"
                                elif a == 2:
                                    mine2 = "🟩"
                                elif a == 3:
                                    mine3 = "🟩"
                                elif a == 4:
                                    mine4 = "🟩"
                                elif a == 5:
                                    mine5 = "🟩"
                                elif a == 6:
                                    mine6 = "🟩"
                                elif a == 7:
                                    mine7 = "🟩"
                                elif a == 8:
                                    mine8 = "🟩"
                                elif a == 9:
                                    mine9 = "🟩"
                                elif a == 10:
                                    mine10 = "🟩"
                                elif a == 11:
                                    mine11 = "🟩"
                                elif a == 12:
                                    mine12 = "🟩"
                                elif a == 13:
                                    mine13 = "🟩"
                                elif a == 14:
                                    mine14 = "🟩"
                                elif a == 15:
                                    mine15 = "🟩"
                                elif a == 16:
                                    mine16 = "🟩"
                                elif a == 17:
                                    mine17 = "🟩"
                                elif a == 18:
                                    mine18 = "🟩"
                                elif a == 19:
                                    mine19 = "🟩"
                                elif a == 20:
                                    mine20 = "🟩"
                                elif a == 21:
                                    mine21 = "🟩"
                                elif a == 22:
                                    mine22 = "🟩"
                                elif a == 23:
                                    mine23 = "🟩"
                                elif a == 24:
                                    mine21 = "🟩"
                                elif a == 25:
                                    mine25 = "🟩"
                                elif a == 0:
                                    mine1 = "🟩"

                                if 1 in mines:
                                    mine1 = "💣"
                                if 2 in mines:
                                    mine2 = "💣"
                                if 3 in mines:
                                    mine3 = "💣"
                                if 4 in mines:
                                    mine4 = "💣"
                                if 5 in mines:
                                    mine5 = "💣"
                                if 6 in mines:
                                    mine6 = "💣"
                                if 7 in mines:
                                    mine7 = "💣"
                                if 8 in mines:
                                    mine8 = "💣"
                                if 9 in mines:
                                    mine9 = "💣"
                                if 10 in mines:
                                    mine10 = "💣"
                                if 11 in mines:
                                    mine11 = "💣"
                                if 12 in mines:
                                    mine12 = "💣"
                                if 13 in mines:
                                    mine13 = "💣"
                                if 14 in mines:
                                    mine14 = "💣"
                                if 15 in mines:
                                    mine15 = "💣"
                                if 16 in mines:
                                    mine16 = "💣"
                                if 17 in mines:
                                    mine17 = "💣"
                                if 18 in mines:
                                    mine18 = "💣"
                                if 19 in mines:
                                    mine19 = "💣"
                                if 20 in mines:
                                    mine20 = "💣"
                                if 21 in mines:
                                    mine21 = "💣"
                                if 22 in mines:
                                    mine22 = "💣"
                                if 23 in mines:
                                    mine23 = "💣"
                                if 24 in mines:
                                    mine21 = "💣"
                                if 25 in mines:
                                    mine25 = "💣"
                                if 0 in mines:
                                    mine1 = "💣"

                                if b == 1:
                                    mine1 = "💥"
                                elif b == 2:
                                    mine2 = "💥"
                                elif b == 3:
                                    mine3 = "💥"
                                elif b == 4:
                                    mine4 = "💥"
                                elif b == 5:
                                    mine5 = "💥"
                                elif b == 6:
                                    mine6 = "💥"
                                elif b == 7:
                                    mine7 = "💥"
                                elif b == 8:
                                    mine8 = "💥"
                                elif b == 9:
                                    mine9 = "💥"
                                elif b == 10:
                                    mine10 = "💥"
                                elif b == 11:
                                    mine11 = "💥"
                                elif b == 12:
                                    mine12 = "💥"
                                elif b == 13:
                                    mine13 = "💥"
                                elif b == 14:
                                    mine14 = "💥"
                                elif b == 15:
                                    mine15 = "💥"
                                elif b == 16:
                                    mine16 = "💥"
                                elif b == 17:
                                    mine17 = "💥"
                                elif b == 18:
                                    mine18 = "💥"
                                elif b == 19:
                                    mine19 = "💥"
                                elif b == 20:
                                    mine20 = "💥"
                                elif b == 21:
                                    mine21 = "💥"
                                elif b == 22:
                                    mine22 = "💥"
                                elif b == 23:
                                    mine23 = "💥"
                                elif b == 24:
                                    mine21 = "💥"
                                elif b == 25:
                                    mine25 = "💥"
                                elif b == 0:
                                    mine1 = "💥"

                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                subuser = user['user']
                                wallet = subuser['wallet']
                                wallett = round(wallet, 2)
                                amount = game['betAmount']
                                title = f"Hound Predictor"
                                mines = game['minesAmount']
                                roundid = game['clientSeed']
                                color = 0xe81a1a
                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                em = discord.Embed(description=desc, color=color, title=title)
                                em.set_thumbnail(
                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                em.set_footer(text=f"discord.gg/houndpredictor")
                                await ok.edit_original_message(embed=em)
                            else:
                                end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                   headers={'x-auth-token': token},
                                                   json={'cashout': True}).json()
                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                   headers={'x-auth-token': token}).json()
                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                game = end['game']
                                uncover = game['uncoveredLocations']
                                mines = game['mineLocations']
                                mines.sort()
                                a = uncover[0]
                                if a == 1:
                                    mine1 = "🟩"
                                elif a == 2:
                                    mine2 = "🟩"
                                elif a == 3:
                                    mine3 = "🟩"
                                elif a == 4:
                                    mine4 = "🟩"
                                elif a == 5:
                                    mine5 = "🟩"
                                elif a == 6:
                                    mine6 = "🟩"
                                elif a == 7:
                                    mine7 = "🟩"
                                elif a == 8:
                                    mine8 = "🟩"
                                elif a == 9:
                                    mine9 = "🟩"
                                elif a == 10:
                                    mine10 = "🟩"
                                elif a == 11:
                                    mine11 = "🟩"
                                elif a == 12:
                                    mine12 = "🟩"
                                elif a == 13:
                                    mine13 = "🟩"
                                elif a == 14:
                                    mine14 = "🟩"
                                elif a == 15:
                                    mine15 = "🟩"
                                elif a == 16:
                                    mine16 = "🟩"
                                elif a == 17:
                                    mine17 = "🟩"
                                elif a == 18:
                                    mine18 = "🟩"
                                elif a == 19:
                                    mine19 = "🟩"
                                elif a == 20:
                                    mine20 = "🟩"
                                elif a == 21:
                                    mine21 = "🟩"
                                elif a == 22:
                                    mine22 = "🟩"
                                elif a == 23:
                                    mine23 = "🟩"
                                elif a == 24:
                                    mine21 = "🟩"
                                elif a == 25:
                                    mine25 = "🟩"
                                elif a == 0:
                                    mine1 = "🟩"

                                if 1 in mines:
                                    mine1 = "💣"
                                if 2 in mines:
                                    mine2 = "💣"
                                if 3 in mines:
                                    mine3 = "💣"
                                if 4 in mines:
                                    mine4 = "💣"
                                if 5 in mines:
                                    mine5 = "💣"
                                if 6 in mines:
                                    mine6 = "💣"
                                if 7 in mines:
                                    mine7 = "💣"
                                if 8 in mines:
                                    mine8 = "💣"
                                if 9 in mines:
                                    mine9 = "💣"
                                if 10 in mines:
                                    mine10 = "💣"
                                if 11 in mines:
                                    mine11 = "💣"
                                if 12 in mines:
                                    mine12 = "💣"
                                if 13 in mines:
                                    mine13 = "💣"
                                if 14 in mines:
                                    mine14 = "💣"
                                if 15 in mines:
                                    mine15 = "💣"
                                if 16 in mines:
                                    mine16 = "💣"
                                if 17 in mines:
                                    mine17 = "💣"
                                if 18 in mines:
                                    mine18 = "💣"
                                if 19 in mines:
                                    mine19 = "💣"
                                if 20 in mines:
                                    mine20 = "💣"
                                if 21 in mines:
                                    mine21 = "💣"
                                if 22 in mines:
                                    mine22 = "💣"
                                if 23 in mines:
                                    mine23 = "💣"
                                if 24 in mines:
                                    mine21 = "💣"
                                if 25 in mines:
                                    mine25 = "💣"
                                if 0 in mines:
                                    mine1 = "💣"

                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                subuser = user['user']
                                wallet = subuser['wallet']
                                wallett = round(wallet, 2)
                                winnings = end['winnings']
                                amount = game['betAmount']
                                idk = winnings - amount
                                profit = round(idk, 2)
                                title = f"Hound Predictor"
                                mines = game['minesAmount']
                                roundid = game['clientSeed']
                                color = 0xe81a1a
                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                em = discord.Embed(description=desc, color=color, title=title)
                                em.set_thumbnail(
                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                em.set_footer(text=f"discord.gg/houndpredictor")
                                await ok.edit_original_message(embed=em)
                        if float(spots) == 2:
                            spot = random.choice(list(range(0, 24)))
                            spot1 = random.choice(list(range(0, 24)))
                            cashfalse = "false"
                            placemine = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                     headers={'x-auth-token': token},
                                                     json={'cashout': False, 'mine': spot}).json()
                            time.sleep(0.5)

                            explosion = placemine['exploded']
                            if explosion == True:
                                end = placemine
                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                   headers={'x-auth-token': token}).json()
                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                game = end['game']
                                uncover = game['uncoveredLocations']
                                badmine = game['badMineUncovered']
                                mines = game['mineLocations']
                                b = badmine
                                a = uncover
                                if a == 1:
                                    mine1 = "🟩"
                                elif a == 2:
                                    mine2 = "🟩"
                                elif a == 3:
                                    mine3 = "🟩"
                                elif a == 4:
                                    mine4 = "🟩"
                                elif a == 5:
                                    mine5 = "🟩"
                                elif a == 6:
                                    mine6 = "🟩"
                                elif a == 7:
                                    mine7 = "🟩"
                                elif a == 8:
                                    mine8 = "🟩"
                                elif a == 9:
                                    mine9 = "🟩"
                                elif a == 10:
                                    mine10 = "🟩"
                                elif a == 11:
                                    mine11 = "🟩"
                                elif a == 12:
                                    mine12 = "🟩"
                                elif a == 13:
                                    mine13 = "🟩"
                                elif a == 14:
                                    mine14 = "🟩"
                                elif a == 15:
                                    mine15 = "🟩"
                                elif a == 16:
                                    mine16 = "🟩"
                                elif a == 17:
                                    mine17 = "🟩"
                                elif a == 18:
                                    mine18 = "🟩"
                                elif a == 19:
                                    mine19 = "🟩"
                                elif a == 20:
                                    mine20 = "🟩"
                                elif a == 21:
                                    mine21 = "🟩"
                                elif a == 22:
                                    mine22 = "🟩"
                                elif a == 23:
                                    mine23 = "🟩"
                                elif a == 24:
                                    mine21 = "🟩"
                                elif a == 25:
                                    mine25 = "🟩"
                                elif a == 0:
                                    mine1 = "🟩"

                                if 1 in mines:
                                    mine1 = "💣"
                                if 2 in mines:
                                    mine2 = "💣"
                                if 3 in mines:
                                    mine3 = "💣"
                                if 4 in mines:
                                    mine4 = "💣"
                                if 5 in mines:
                                    mine5 = "💣"
                                if 6 in mines:
                                    mine6 = "💣"
                                if 7 in mines:
                                    mine7 = "💣"
                                if 8 in mines:
                                    mine8 = "💣"
                                if 9 in mines:
                                    mine9 = "💣"
                                if 10 in mines:
                                    mine10 = "💣"
                                if 11 in mines:
                                    mine11 = "💣"
                                if 12 in mines:
                                    mine12 = "💣"
                                if 13 in mines:
                                    mine13 = "💣"
                                if 14 in mines:
                                    mine14 = "💣"
                                if 15 in mines:
                                    mine15 = "💣"
                                if 16 in mines:
                                    mine16 = "💣"
                                if 17 in mines:
                                    mine17 = "💣"
                                if 18 in mines:
                                    mine18 = "💣"
                                if 19 in mines:
                                    mine19 = "💣"
                                if 20 in mines:
                                    mine20 = "💣"
                                if 21 in mines:
                                    mine21 = "💣"
                                if 22 in mines:
                                    mine22 = "💣"
                                if 23 in mines:
                                    mine23 = "💣"
                                if 24 in mines:
                                    mine21 = "💣"
                                if 25 in mines:
                                    mine25 = "💣"
                                if 0 in mines:
                                    mine1 = "💣"

                                if b == 1:
                                    mine1 = "💥"
                                elif b == 2:
                                    mine2 = "💥"
                                elif b == 3:
                                    mine3 = "💥"
                                elif b == 4:
                                    mine4 = "💥"
                                elif b == 5:
                                    mine5 = "💥"
                                elif b == 6:
                                    mine6 = "💥"
                                elif b == 7:
                                    mine7 = "💥"
                                elif b == 8:
                                    mine8 = "💥"
                                elif b == 9:
                                    mine9 = "💥"
                                elif b == 10:
                                    mine10 = "💥"
                                elif b == 11:
                                    mine11 = "💥"
                                elif b == 12:
                                    mine12 = "💥"
                                elif b == 13:
                                    mine13 = "💥"
                                elif b == 14:
                                    mine14 = "💥"
                                elif b == 15:
                                    mine15 = "💥"
                                elif b == 16:
                                    mine16 = "💥"
                                elif b == 17:
                                    mine17 = "💥"
                                elif b == 18:
                                    mine18 = "💥"
                                elif b == 19:
                                    mine19 = "💥"
                                elif b == 20:
                                    mine20 = "💥"
                                elif b == 21:
                                    mine21 = "💥"
                                elif b == 22:
                                    mine22 = "💥"
                                elif b == 23:
                                    mine23 = "💥"
                                elif b == 24:
                                    mine21 = "💥"
                                elif b == 25:
                                    mine25 = "💥"
                                elif b == 0:
                                    mine1 = "💥"

                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                subuser = user['user']
                                wallet = subuser['wallet']
                                wallett = round(wallet, 2)
                                amount = game['betAmount']
                                title = f"Hound Predictor"
                                mines = game['minesAmount']
                                roundid = game['clientSeed']
                                color = 0xe81a1a
                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                em = discord.Embed(description=desc, color=color, title=title)
                                em.set_thumbnail(
                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                em.set_footer(text=f"discord.gg/houndpredictor")
                                await ok.edit_original_message(embed=em)

                            else:
                                if float(spot1) == spot:
                                    spot1 = random.choice(list(range(0, 24)))
                                    placemine1 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                              headers={'x-auth-token': token},
                                                              json={'cashout': False, 'mine': spot1}).json()
                                    explosion1 = placemine1['exploded']
                                    if explosion1 == True:
                                        end = placemine1
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        badmine = game['badMineUncovered']
                                        mines = game['mineLocations']
                                        b = badmine
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        if b == 1:
                                            mine1 = "💥"
                                        elif b == 2:
                                            mine2 = "💥"
                                        elif b == 3:
                                            mine3 = "💥"
                                        elif b == 4:
                                            mine4 = "💥"
                                        elif b == 5:
                                            mine5 = "💥"
                                        elif b == 6:
                                            mine6 = "💥"
                                        elif b == 7:
                                            mine7 = "💥"
                                        elif b == 8:
                                            mine8 = "💥"
                                        elif b == 9:
                                            mine9 = "💥"
                                        elif b == 10:
                                            mine10 = "💥"
                                        elif b == 11:
                                            mine11 = "💥"
                                        elif b == 12:
                                            mine12 = "💥"
                                        elif b == 13:
                                            mine13 = "💥"
                                        elif b == 14:
                                            mine14 = "💥"
                                        elif b == 15:
                                            mine15 = "💥"
                                        elif b == 16:
                                            mine16 = "💥"
                                        elif b == 17:
                                            mine17 = "💥"
                                        elif b == 18:
                                            mine18 = "💥"
                                        elif b == 19:
                                            mine19 = "💥"
                                        elif b == 20:
                                            mine20 = "💥"
                                        elif b == 21:
                                            mine21 = "💥"
                                        elif b == 22:
                                            mine22 = "💥"
                                        elif b == 23:
                                            mine23 = "💥"
                                        elif b == 24:
                                            mine21 = "💥"
                                        elif b == 25:
                                            mine25 = "💥"
                                        elif b == 0:
                                            mine1 = "💥"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        amount = game['betAmount']
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                                    else:
                                        end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                           headers={'x-auth-token': token},
                                                           json={'cashout': True}).json()
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        mines = game['mineLocations']
                                        mines.sort()
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        winnings = end['winnings']
                                        amount = game['betAmount']
                                        idk = winnings - amount
                                        profit = round(idk, 2)
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                                else:
                                    placemine1 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                              headers={'x-auth-token': token},
                                                              json={'cashout': False, 'mine': spot1}).json()
                                    explosion1 = placemine1['exploded']
                                    if explosion1 == True:
                                        end = placemine1
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        badmine = game['badMineUncovered']
                                        mines = game['mineLocations']
                                        b = badmine
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        if b == 1:
                                            mine1 = "💥"
                                        elif b == 2:
                                            mine2 = "💥"
                                        elif b == 3:
                                            mine3 = "💥"
                                        elif b == 4:
                                            mine4 = "💥"
                                        elif b == 5:
                                            mine5 = "💥"
                                        elif b == 6:
                                            mine6 = "💥"
                                        elif b == 7:
                                            mine7 = "💥"
                                        elif b == 8:
                                            mine8 = "💥"
                                        elif b == 9:
                                            mine9 = "💥"
                                        elif b == 10:
                                            mine10 = "💥"
                                        elif b == 11:
                                            mine11 = "💥"
                                        elif b == 12:
                                            mine12 = "💥"
                                        elif b == 13:
                                            mine13 = "💥"
                                        elif b == 14:
                                            mine14 = "💥"
                                        elif b == 15:
                                            mine15 = "💥"
                                        elif b == 16:
                                            mine16 = "💥"
                                        elif b == 17:
                                            mine17 = "💥"
                                        elif b == 18:
                                            mine18 = "💥"
                                        elif b == 19:
                                            mine19 = "💥"
                                        elif b == 20:
                                            mine20 = "💥"
                                        elif b == 21:
                                            mine21 = "💥"
                                        elif b == 22:
                                            mine22 = "💥"
                                        elif b == 23:
                                            mine23 = "💥"
                                        elif b == 24:
                                            mine21 = "💥"
                                        elif b == 25:
                                            mine25 = "💥"
                                        elif b == 0:
                                            mine1 = "💥"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        amount = game['betAmount']
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                                    else:
                                        end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                           headers={'x-auth-token': token},
                                                           json={'cashout': True}).json()
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        mines = game['mineLocations']
                                        mines.sort()
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        winnings = end['winnings']
                                        amount = game['betAmount']
                                        idk = winnings - amount
                                        profit = round(idk, 2)
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                        if float(spots) == 3:
                            spot = random.choice(list(range(0, 24)))
                            spot1 = random.choice(list(range(0, 24)))
                            spot2 = random.choice(list(range(0, 24)))
                            cashfalse = "false"
                            placemine = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                     headers={'x-auth-token': token},
                                                     json={'cashout': False, 'mine': spot}).json()
                            time.sleep(0.5)

                            explosion = placemine['exploded']
                            if explosion == True:
                                end = placemine
                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                   headers={'x-auth-token': token}).json()
                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                game = end['game']
                                uncover = game['uncoveredLocations']
                                badmine = game['badMineUncovered']
                                mines = game['mineLocations']
                                b = badmine
                                a = uncover
                                if a == 1:
                                    mine1 = "🟩"
                                elif a == 2:
                                    mine2 = "🟩"
                                elif a == 3:
                                    mine3 = "🟩"
                                elif a == 4:
                                    mine4 = "🟩"
                                elif a == 5:
                                    mine5 = "🟩"
                                elif a == 6:
                                    mine6 = "🟩"
                                elif a == 7:
                                    mine7 = "🟩"
                                elif a == 8:
                                    mine8 = "🟩"
                                elif a == 9:
                                    mine9 = "🟩"
                                elif a == 10:
                                    mine10 = "🟩"
                                elif a == 11:
                                    mine11 = "🟩"
                                elif a == 12:
                                    mine12 = "🟩"
                                elif a == 13:
                                    mine13 = "🟩"
                                elif a == 14:
                                    mine14 = "🟩"
                                elif a == 15:
                                    mine15 = "🟩"
                                elif a == 16:
                                    mine16 = "🟩"
                                elif a == 17:
                                    mine17 = "🟩"
                                elif a == 18:
                                    mine18 = "🟩"
                                elif a == 19:
                                    mine19 = "🟩"
                                elif a == 20:
                                    mine20 = "🟩"
                                elif a == 21:
                                    mine21 = "🟩"
                                elif a == 22:
                                    mine22 = "🟩"
                                elif a == 23:
                                    mine23 = "🟩"
                                elif a == 24:
                                    mine21 = "🟩"
                                elif a == 25:
                                    mine25 = "🟩"
                                elif a == 0:
                                    mine1 = "🟩"

                                if 1 in mines:
                                    mine1 = "💣"
                                if 2 in mines:
                                    mine2 = "💣"
                                if 3 in mines:
                                    mine3 = "💣"
                                if 4 in mines:
                                    mine4 = "💣"
                                if 5 in mines:
                                    mine5 = "💣"
                                if 6 in mines:
                                    mine6 = "💣"
                                if 7 in mines:
                                    mine7 = "💣"
                                if 8 in mines:
                                    mine8 = "💣"
                                if 9 in mines:
                                    mine9 = "💣"
                                if 10 in mines:
                                    mine10 = "💣"
                                if 11 in mines:
                                    mine11 = "💣"
                                if 12 in mines:
                                    mine12 = "💣"
                                if 13 in mines:
                                    mine13 = "💣"
                                if 14 in mines:
                                    mine14 = "💣"
                                if 15 in mines:
                                    mine15 = "💣"
                                if 16 in mines:
                                    mine16 = "💣"
                                if 17 in mines:
                                    mine17 = "💣"
                                if 18 in mines:
                                    mine18 = "💣"
                                if 19 in mines:
                                    mine19 = "💣"
                                if 20 in mines:
                                    mine20 = "💣"
                                if 21 in mines:
                                    mine21 = "💣"
                                if 22 in mines:
                                    mine22 = "💣"
                                if 23 in mines:
                                    mine23 = "💣"
                                if 24 in mines:
                                    mine21 = "💣"
                                if 25 in mines:
                                    mine25 = "💣"
                                if 0 in mines:
                                    mine1 = "💣"

                                if b == 1:
                                    mine1 = "💥"
                                elif b == 2:
                                    mine2 = "💥"
                                elif b == 3:
                                    mine3 = "💥"
                                elif b == 4:
                                    mine4 = "💥"
                                elif b == 5:
                                    mine5 = "💥"
                                elif b == 6:
                                    mine6 = "💥"
                                elif b == 7:
                                    mine7 = "💥"
                                elif b == 8:
                                    mine8 = "💥"
                                elif b == 9:
                                    mine9 = "💥"
                                elif b == 10:
                                    mine10 = "💥"
                                elif b == 11:
                                    mine11 = "💥"
                                elif b == 12:
                                    mine12 = "💥"
                                elif b == 13:
                                    mine13 = "💥"
                                elif b == 14:
                                    mine14 = "💥"
                                elif b == 15:
                                    mine15 = "💥"
                                elif b == 16:
                                    mine16 = "💥"
                                elif b == 17:
                                    mine17 = "💥"
                                elif b == 18:
                                    mine18 = "💥"
                                elif b == 19:
                                    mine19 = "💥"
                                elif b == 20:
                                    mine20 = "💥"
                                elif b == 21:
                                    mine21 = "💥"
                                elif b == 22:
                                    mine22 = "💥"
                                elif b == 23:
                                    mine23 = "💥"
                                elif b == 24:
                                    mine21 = "💥"
                                elif b == 25:
                                    mine25 = "💥"
                                elif b == 0:
                                    mine1 = "💥"

                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                subuser = user['user']
                                wallet = subuser['wallet']
                                wallett = round(wallet, 2)
                                amount = game['betAmount']
                                title = f"Hound Predictor"
                                mines = game['minesAmount']
                                roundid = game['clientSeed']
                                color = 0xe81a1a
                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                em = discord.Embed(description=desc, color=color, title=title)
                                em.set_thumbnail(
                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                em.set_footer(text=f"discord.gg/houndpredictor")
                                await ok.edit_original_message(embed=em)

                            else:
                                if float(spot1) == spot:
                                    spot1 = random.choice(list(range(0, 24)))
                                    placemine1 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                              headers={'x-auth-token': token},
                                                              json={'cashout': False, 'mine': spot1}).json()
                                    explosion1 = placemine1['exploded']
                                    if explosion1 == True:
                                        end = placemine1
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        badmine = game['badMineUncovered']
                                        mines = game['mineLocations']
                                        b = badmine
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        if b == 1:
                                            mine1 = "💥"
                                        elif b == 2:
                                            mine2 = "💥"
                                        elif b == 3:
                                            mine3 = "💥"
                                        elif b == 4:
                                            mine4 = "💥"
                                        elif b == 5:
                                            mine5 = "💥"
                                        elif b == 6:
                                            mine6 = "💥"
                                        elif b == 7:
                                            mine7 = "💥"
                                        elif b == 8:
                                            mine8 = "💥"
                                        elif b == 9:
                                            mine9 = "💥"
                                        elif b == 10:
                                            mine10 = "💥"
                                        elif b == 11:
                                            mine11 = "💥"
                                        elif b == 12:
                                            mine12 = "💥"
                                        elif b == 13:
                                            mine13 = "💥"
                                        elif b == 14:
                                            mine14 = "💥"
                                        elif b == 15:
                                            mine15 = "💥"
                                        elif b == 16:
                                            mine16 = "💥"
                                        elif b == 17:
                                            mine17 = "💥"
                                        elif b == 18:
                                            mine18 = "💥"
                                        elif b == 19:
                                            mine19 = "💥"
                                        elif b == 20:
                                            mine20 = "💥"
                                        elif b == 21:
                                            mine21 = "💥"
                                        elif b == 22:
                                            mine22 = "💥"
                                        elif b == 23:
                                            mine23 = "💥"
                                        elif b == 24:
                                            mine21 = "💥"
                                        elif b == 25:
                                            mine25 = "💥"
                                        elif b == 0:
                                            mine1 = "💥"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        amount = game['betAmount']
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                                    else:
                                        if float(spot) == spot2 or float(spot2) == spot1:
                                            spot2 = random.choice(list(range(0, 24)))
                                            placemine2 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                                      headers={'x-auth-token': token},
                                                                      json={'cashout': False, 'mine': spot2}).json()
                                            explosion2 = placemine2['exploded']
                                            if explosion2 == True:
                                                end = placemine2
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                badmine = game['badMineUncovered']
                                                mines = game['mineLocations']
                                                b = badmine
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                if b == 1:
                                                    mine1 = "💥"
                                                elif b == 2:
                                                    mine2 = "💥"
                                                elif b == 3:
                                                    mine3 = "💥"
                                                elif b == 4:
                                                    mine4 = "💥"
                                                elif b == 5:
                                                    mine5 = "💥"
                                                elif b == 6:
                                                    mine6 = "💥"
                                                elif b == 7:
                                                    mine7 = "💥"
                                                elif b == 8:
                                                    mine8 = "💥"
                                                elif b == 9:
                                                    mine9 = "💥"
                                                elif b == 10:
                                                    mine10 = "💥"
                                                elif b == 11:
                                                    mine11 = "💥"
                                                elif b == 12:
                                                    mine12 = "💥"
                                                elif b == 13:
                                                    mine13 = "💥"
                                                elif b == 14:
                                                    mine14 = "💥"
                                                elif b == 15:
                                                    mine15 = "💥"
                                                elif b == 16:
                                                    mine16 = "💥"
                                                elif b == 17:
                                                    mine17 = "💥"
                                                elif b == 18:
                                                    mine18 = "💥"
                                                elif b == 19:
                                                    mine19 = "💥"
                                                elif b == 20:
                                                    mine20 = "💥"
                                                elif b == 21:
                                                    mine21 = "💥"
                                                elif b == 22:
                                                    mine22 = "💥"
                                                elif b == 23:
                                                    mine23 = "💥"
                                                elif b == 24:
                                                    mine21 = "💥"
                                                elif b == 25:
                                                    mine25 = "💥"
                                                elif b == 0:
                                                    mine1 = "💥"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                amount = game['betAmount']
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)
                                            else:
                                                end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                                   headers={'x-auth-token': token},
                                                                   json={'cashout': True}).json()
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                mines = game['mineLocations']
                                                mines.sort()
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                winnings = end['winnings']
                                                amount = game['betAmount']
                                                idk = winnings - amount
                                                profit = round(idk, 2)
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)


                                else:
                                    placemine1 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                              headers={'x-auth-token': token},
                                                              json={'cashout': False, 'mine': spot1}).json()
                                    explosion1 = placemine1['exploded']
                                    if explosion1 == True:
                                        end = placemine1
                                        user = scraper.get(f'https://api.bloxflip.com/user',
                                                           headers={'x-auth-token': token}).json()
                                        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                        game = end['game']
                                        uncover = game['uncoveredLocations']
                                        badmine = game['badMineUncovered']
                                        mines = game['mineLocations']
                                        b = badmine
                                        a = uncover
                                        if 1 in a:
                                            mine1 = "🟩"
                                        if 2 in a:
                                            mine2 = "🟩"
                                        if 3 in a:
                                            mine3 = "🟩"
                                        if 4 in a:
                                            mine4 = "🟩"
                                        if 5 in a:
                                            mine5 = "🟩"
                                        if 6 in a:
                                            mine6 = "🟩"
                                        if 7 in a:
                                            mine7 = "🟩"
                                        if 8 in a:
                                            mine8 = "🟩"
                                        if 9 in a:
                                            mine9 = "🟩"
                                        if 10 in a:
                                            mine10 = "🟩"
                                        if 11 in a:
                                            mine11 = "🟩"
                                        if 12 in a:
                                            mine12 = "🟩"
                                        if 13 in a:
                                            mine13 = "🟩"
                                        if 14 in a:
                                            mine14 = "🟩"
                                        if 15 in a:
                                            mine15 = "🟩"
                                        if 16 in a:
                                            mine16 = "🟩"
                                        if 17 in a:
                                            mine17 = "🟩"
                                        if 18 in a:
                                            mine18 = "🟩"
                                        if 19 in a:
                                            mine19 = "🟩"
                                        if 20 in a:
                                            mine20 = "🟩"
                                        if 21 in a:
                                            mine21 = "🟩"
                                        if 22 in a:
                                            mine22 = "🟩"
                                        if 23 in a:
                                            mine23 = "🟩"
                                        if 24 in a:
                                            mine21 = "🟩"
                                        if 25 in a:
                                            mine25 = "🟩"
                                        if 0 in a:
                                            mine1 = "🟩"

                                        if 1 in mines:
                                            mine1 = "💣"
                                        if 2 in mines:
                                            mine2 = "💣"
                                        if 3 in mines:
                                            mine3 = "💣"
                                        if 4 in mines:
                                            mine4 = "💣"
                                        if 5 in mines:
                                            mine5 = "💣"
                                        if 6 in mines:
                                            mine6 = "💣"
                                        if 7 in mines:
                                            mine7 = "💣"
                                        if 8 in mines:
                                            mine8 = "💣"
                                        if 9 in mines:
                                            mine9 = "💣"
                                        if 10 in mines:
                                            mine10 = "💣"
                                        if 11 in mines:
                                            mine11 = "💣"
                                        if 12 in mines:
                                            mine12 = "💣"
                                        if 13 in mines:
                                            mine13 = "💣"
                                        if 14 in mines:
                                            mine14 = "💣"
                                        if 15 in mines:
                                            mine15 = "💣"
                                        if 16 in mines:
                                            mine16 = "💣"
                                        if 17 in mines:
                                            mine17 = "💣"
                                        if 18 in mines:
                                            mine18 = "💣"
                                        if 19 in mines:
                                            mine19 = "💣"
                                        if 20 in mines:
                                            mine20 = "💣"
                                        if 21 in mines:
                                            mine21 = "💣"
                                        if 22 in mines:
                                            mine22 = "💣"
                                        if 23 in mines:
                                            mine23 = "💣"
                                        if 24 in mines:
                                            mine21 = "💣"
                                        if 25 in mines:
                                            mine25 = "💣"
                                        if 0 in mines:
                                            mine1 = "💣"

                                        if b == 1:
                                            mine1 = "💥"
                                        elif b == 2:
                                            mine2 = "💥"
                                        elif b == 3:
                                            mine3 = "💥"
                                        elif b == 4:
                                            mine4 = "💥"
                                        elif b == 5:
                                            mine5 = "💥"
                                        elif b == 6:
                                            mine6 = "💥"
                                        elif b == 7:
                                            mine7 = "💥"
                                        elif b == 8:
                                            mine8 = "💥"
                                        elif b == 9:
                                            mine9 = "💥"
                                        elif b == 10:
                                            mine10 = "💥"
                                        elif b == 11:
                                            mine11 = "💥"
                                        elif b == 12:
                                            mine12 = "💥"
                                        elif b == 13:
                                            mine13 = "💥"
                                        elif b == 14:
                                            mine14 = "💥"
                                        elif b == 15:
                                            mine15 = "💥"
                                        elif b == 16:
                                            mine16 = "💥"
                                        elif b == 17:
                                            mine17 = "💥"
                                        elif b == 18:
                                            mine18 = "💥"
                                        elif b == 19:
                                            mine19 = "💥"
                                        elif b == 20:
                                            mine20 = "💥"
                                        elif b == 21:
                                            mine21 = "💥"
                                        elif b == 22:
                                            mine22 = "💥"
                                        elif b == 23:
                                            mine23 = "💥"
                                        elif b == 24:
                                            mine21 = "💥"
                                        elif b == 25:
                                            mine25 = "💥"
                                        elif b == 0:
                                            mine1 = "💥"

                                        one = mine1 + mine2 + mine3 + mine4 + mine5
                                        two = mine6 + mine7 + mine8 + mine9 + mine10
                                        three = mine11 + mine12 + mine13 + mine14 + mine15
                                        four = mine16 + mine17 + mine18 + mine19 + mine20
                                        five = mine21 + mine22 + mine23 + mine24 + mine25
                                        subuser = user['user']
                                        wallet = subuser['wallet']
                                        wallett = round(wallet, 2)
                                        amount = game['betAmount']
                                        title = f"Hound Predictor"
                                        mines = game['minesAmount']
                                        roundid = game['clientSeed']
                                        color = 0xe81a1a
                                        desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                        em = discord.Embed(description=desc, color=color, title=title)
                                        em.set_thumbnail(
                                            url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                        em.set_footer(text=f"discord.gg/houndpredictor")
                                        await ok.edit_original_message(embed=em)
                                    else:
                                        if float(spot) == spot2 or float(spot2) == spot1:
                                            spot2 = random.choice(list(range(0, 24)))
                                            placemine2 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                                      headers={'x-auth-token': token},
                                                                      json={'cashout': False, 'mine': spot2}).json()
                                            explosion2 = placemine2['exploded']
                                            if explosion2 == True:
                                                end = placemine2
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                badmine = game['badMineUncovered']
                                                mines = game['mineLocations']
                                                b = badmine
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                if b == 1:
                                                    mine1 = "💥"
                                                elif b == 2:
                                                    mine2 = "💥"
                                                elif b == 3:
                                                    mine3 = "💥"
                                                elif b == 4:
                                                    mine4 = "💥"
                                                elif b == 5:
                                                    mine5 = "💥"
                                                elif b == 6:
                                                    mine6 = "💥"
                                                elif b == 7:
                                                    mine7 = "💥"
                                                elif b == 8:
                                                    mine8 = "💥"
                                                elif b == 9:
                                                    mine9 = "💥"
                                                elif b == 10:
                                                    mine10 = "💥"
                                                elif b == 11:
                                                    mine11 = "💥"
                                                elif b == 12:
                                                    mine12 = "💥"
                                                elif b == 13:
                                                    mine13 = "💥"
                                                elif b == 14:
                                                    mine14 = "💥"
                                                elif b == 15:
                                                    mine15 = "💥"
                                                elif b == 16:
                                                    mine16 = "💥"
                                                elif b == 17:
                                                    mine17 = "💥"
                                                elif b == 18:
                                                    mine18 = "💥"
                                                elif b == 19:
                                                    mine19 = "💥"
                                                elif b == 20:
                                                    mine20 = "💥"
                                                elif b == 21:
                                                    mine21 = "💥"
                                                elif b == 22:
                                                    mine22 = "💥"
                                                elif b == 23:
                                                    mine23 = "💥"
                                                elif b == 24:
                                                    mine21 = "💥"
                                                elif b == 25:
                                                    mine25 = "💥"
                                                elif b == 0:
                                                    mine1 = "💥"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                amount = game['betAmount']
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)
                                            else:
                                                end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                                   headers={'x-auth-token': token},
                                                                   json={'cashout': True}).json()
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                mines = game['mineLocations']
                                                mines.sort()
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                winnings = end['winnings']
                                                amount = game['betAmount']
                                                idk = winnings - amount
                                                profit = round(idk, 2)
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)
                                        else:
                                            placemine2 = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                                                      headers={'x-auth-token': token},
                                                                      json={'cashout': False, 'mine': spot2}).json()
                                            explosion2 = placemine2['exploded']
                                            if explosion2 == True:
                                                end = placemine2
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                badmine = game['badMineUncovered']
                                                mines = game['mineLocations']

                                                b = badmine
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                if b == 1:
                                                    mine1 = "💥"
                                                elif b == 2:
                                                    mine2 = "💥"
                                                elif b == 3:
                                                    mine3 = "💥"
                                                elif b == 4:
                                                    mine4 = "💥"
                                                elif b == 5:
                                                    mine5 = "💥"
                                                elif b == 6:
                                                    mine6 = "💥"
                                                elif b == 7:
                                                    mine7 = "💥"
                                                elif b == 8:
                                                    mine8 = "💥"
                                                elif b == 9:
                                                    mine9 = "💥"
                                                elif b == 10:
                                                    mine10 = "💥"
                                                elif b == 11:
                                                    mine11 = "💥"
                                                elif b == 12:
                                                    mine12 = "💥"
                                                elif b == 13:
                                                    mine13 = "💥"
                                                elif b == 14:
                                                    mine14 = "💥"
                                                elif b == 15:
                                                    mine15 = "💥"
                                                elif b == 16:
                                                    mine16 = "💥"
                                                elif b == 17:
                                                    mine17 = "💥"
                                                elif b == 18:
                                                    mine18 = "💥"
                                                elif b == 19:
                                                    mine19 = "💥"
                                                elif b == 20:
                                                    mine20 = "💥"
                                                elif b == 21:
                                                    mine21 = "💥"
                                                elif b == 22:
                                                    mine22 = "💥"
                                                elif b == 23:
                                                    mine23 = "💥"
                                                elif b == 24:
                                                    mine21 = "💥"
                                                elif b == 25:
                                                    mine25 = "💥"
                                                elif b == 0:
                                                    mine1 = "💥"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                amount = game['betAmount']
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Loss**\n```{amount}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)
                                            else:
                                                end = scraper.post(f'https://api.bloxflip.com/games/mines/action',
                                                                   headers={'x-auth-token': token},
                                                                   json={'cashout': True}).json()
                                                user = scraper.get(f'https://api.bloxflip.com/user',
                                                                   headers={'x-auth-token': token}).json()
                                                mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                                                game = end['game']
                                                uncover = game['uncoveredLocations']
                                                mines = game['mineLocations']
                                                mines.sort()
                                                a = uncover
                                                if 1 in a:
                                                    mine1 = "🟩"
                                                if 2 in a:
                                                    mine2 = "🟩"
                                                if 3 in a:
                                                    mine3 = "🟩"
                                                if 4 in a:
                                                    mine4 = "🟩"
                                                if 5 in a:
                                                    mine5 = "🟩"
                                                if 6 in a:
                                                    mine6 = "🟩"
                                                if 7 in a:
                                                    mine7 = "🟩"
                                                if 8 in a:
                                                    mine8 = "🟩"
                                                if 9 in a:
                                                    mine9 = "🟩"
                                                if 10 in a:
                                                    mine10 = "🟩"
                                                if 11 in a:
                                                    mine11 = "🟩"
                                                if 12 in a:
                                                    mine12 = "🟩"
                                                if 13 in a:
                                                    mine13 = "🟩"
                                                if 14 in a:
                                                    mine14 = "🟩"
                                                if 15 in a:
                                                    mine15 = "🟩"
                                                if 16 in a:
                                                    mine16 = "🟩"
                                                if 17 in a:
                                                    mine17 = "🟩"
                                                if 18 in a:
                                                    mine18 = "🟩"
                                                if 19 in a:
                                                    mine19 = "🟩"
                                                if 20 in a:
                                                    mine20 = "🟩"
                                                if 21 in a:
                                                    mine21 = "🟩"
                                                if 22 in a:
                                                    mine22 = "🟩"
                                                if 23 in a:
                                                    mine23 = "🟩"
                                                if 24 in a:
                                                    mine21 = "🟩"
                                                if 25 in a:
                                                    mine25 = "🟩"
                                                if 0 in a:
                                                    mine1 = "🟩"

                                                if 1 in mines:
                                                    mine1 = "💣"
                                                if 2 in mines:
                                                    mine2 = "💣"
                                                if 3 in mines:
                                                    mine3 = "💣"
                                                if 4 in mines:
                                                    mine4 = "💣"
                                                if 5 in mines:
                                                    mine5 = "💣"
                                                if 6 in mines:
                                                    mine6 = "💣"
                                                if 7 in mines:
                                                    mine7 = "💣"
                                                if 8 in mines:
                                                    mine8 = "💣"
                                                if 9 in mines:
                                                    mine9 = "💣"
                                                if 10 in mines:
                                                    mine10 = "💣"
                                                if 11 in mines:
                                                    mine11 = "💣"
                                                if 12 in mines:
                                                    mine12 = "💣"
                                                if 13 in mines:
                                                    mine13 = "💣"
                                                if 14 in mines:
                                                    mine14 = "💣"
                                                if 15 in mines:
                                                    mine15 = "💣"
                                                if 16 in mines:
                                                    mine16 = "💣"
                                                if 17 in mines:
                                                    mine17 = "💣"
                                                if 18 in mines:
                                                    mine18 = "💣"
                                                if 19 in mines:
                                                    mine19 = "💣"
                                                if 20 in mines:
                                                    mine20 = "💣"
                                                if 21 in mines:
                                                    mine21 = "💣"
                                                if 22 in mines:
                                                    mine22 = "💣"
                                                if 23 in mines:
                                                    mine23 = "💣"
                                                if 24 in mines:
                                                    mine21 = "💣"
                                                if 25 in mines:
                                                    mine25 = "💣"
                                                if 0 in mines:
                                                    mine1 = "💣"

                                                one = mine1 + mine2 + mine3 + mine4 + mine5
                                                two = mine6 + mine7 + mine8 + mine9 + mine10
                                                three = mine11 + mine12 + mine13 + mine14 + mine15
                                                four = mine16 + mine17 + mine18 + mine19 + mine20
                                                five = mine21 + mine22 + mine23 + mine24 + mine25
                                                subuser = user['user']
                                                wallet = subuser['wallet']
                                                wallett = round(wallet, 2)
                                                winnings = end['winnings']
                                                amount = game['betAmount']
                                                idk = winnings - amount
                                                profit = round(idk, 2)
                                                title = f"Hound Predictor"
                                                mines = game['minesAmount']
                                                roundid = game['clientSeed']
                                                color = 0xe81a1a
                                                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n **Profit**\n```{profit}```\n**Balance**\n```{wallett}```\n**Mines**\n```{mines}```\n**Round ID**\n```{roundid}```"
                                                em = discord.Embed(description=desc, color=color, title=title)
                                                em.set_thumbnail(
                                                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                                em.set_footer(text=f"discord.gg/houndpredictor")
                                                await ok.edit_original_message(embed=em)


                    else:
                        error = start['error']
                        await ok.edit_original_message(
                            embed=discord.Embed(description=f"{error}", color=0xe81a1a))


cluster = MongoClient("mongo")


def setup(bot):
    bot.add_cog(Mines(bot))
