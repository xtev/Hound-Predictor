import io
import json
import time
from pathlib import Path
from math import floor
import random

from numpy import unicode
from pymongo import MongoClient

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
from discord import Option
from js2py.constructors.jsmath import Math
import discord
from discord.ext import commands


class Mines(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def mines(self, ctx, round_id, tiles: int):
        round_id = str(round_id)
        round_length = len(round_id)
        minescount = int(tiles)
        if round_length < 36 or round_length > 36:
            await ctx.respond(
                embed=discord.Embed(description=f"Invalid Round ID\n```{round_id}```", color=discord.Color.red()))
        elif round_length == 36:
            if '-' in round_id:
                dashcount = round_id.count("-")
                if float(dashcount) == 4:
                    path_to_file = f'/home/container/mines/{round_id}.json'
                    path = Path(path_to_file)

                    if path.is_file():

                        async def get_round_data():
                            with open(f"/home/container/mines/{round_id}.json", "r", encoding='utf8') as f:
                                round = json.load(f)

                            return round

                        ok = await ctx.respond(
                            embed=discord.Embed(description="Checking the API", color=discord.Color.yellow()))
                        userid = ctx.author.id
                        dbuser = cluster["usersfree"]
                        cursor = dbuser[f"{userid}"]
                        check = cursor.find_one({"id": userid})
                        if check is None:
                            insert = {
                                "id": userid, "mines": 1, "crash": 0
                            }
                            cursor.insert_one(insert)
                            title = f"Hound Predictor"
                            color = 0xe81a1a
                            roundtype = await get_round_data()
                            one1 = roundtype["one"]
                            two2 = roundtype["two"]
                            three3 = roundtype["three"]
                            four4 = roundtype["four"]
                            five5 = roundtype["five"]
                            chance1 = roundtype["chance"]
                            mines1 = roundtype["minescount"]

                            desc = f"**Prediction**\n```{one1}\n{two2}\n{three3}\n{four4}\n{five5}```\n**Accuracy**\n```{chance1}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{mines1}```"
                            em = discord.Embed(description=desc, color=color, title=title)
                            em.set_footer(text=f"discord.gg/houndpredictor")
                            em.set_thumbnail(
                                url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                            await ok.edit_original_message(embed=em)
                        else:
                            addmines = check['mines'] + 1
                            cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
                            title = f"Hound Predictor"
                            color = 0xe81a1a
                            roundtype = await get_round_data()
                            one1 = roundtype["one"]
                            two2 = roundtype["two"]
                            three3 = roundtype["three"]
                            four4 = roundtype["four"]
                            five5 = roundtype["five"]
                            chance1 = roundtype["chance"]
                            mines1 = roundtype["minescount"]

                            desc = f"**Prediction**\n```{one1}\n{two2}\n{three3}\n{four4}\n{five5}```\n**Accuracy**\n```{chance1}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{mines1}```"
                            em = discord.Embed(description=desc, color=color, title=title)
                            em.set_footer(text=f"discord.gg/houndpredictor")
                            em.set_thumbnail(
                                url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                            await ok.edit_original_message(embed=em)
                    else:
                        if float(minescount) <= 0 or minescount > 4:
                            await ctx.respond(
                                embed=discord.Embed(description=f"Invalid Mines Count\n```{minescount}```",
                                                    color=discord.Color.red()))
                        elif float(minescount) > 2:
                            await ctx.respond(
                                embed=discord.Embed(description=f"Sorry, Free is 1 - 2",
                                                    color=discord.Color.red()))

                        elif float(minescount) == 1:

                            guildid = ctx.guild.id
                            dbguild = cluster["guilds"]
                            cur = dbguild[f"{guildid}"]
                            guildcheck = cur.find_one({"id": guildid})
                            if guildcheck is None:
                                input = {
                                    "id": guildid, "mines": 1, "crash": 0
                                }
                                cur.insert_one(input)
                                userid = ctx.author.id
                                dbuser = cluster["usersfree"]
                                cursor = dbuser[f"{userid}"]
                                check = cursor.find_one({"id": userid})
                                if check is None:
                                    insert = {
                                        "id": userid, "mines": 1, "crash": 0
                                    }
                                    cursor.insert_one(insert)
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 25)
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
                                    elif a == 12:
                                        mine22 = "🟩"
                                    elif a == 23:
                                        mine23 = "🟩"
                                    elif a == 24:
                                        mine21 = "🟩"
                                    elif a == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)

                                else:
                                    addmines = check['mines'] + 1
                                    cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 25)
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
                                    elif a == 12:
                                        mine22 = "🟩"
                                    elif a == 23:
                                        mine23 = "🟩"
                                    elif a == 24:
                                        mine21 = "🟩"
                                    elif a == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)
                            else:
                                userid = ctx.author.id
                                dbuser = cluster["usersfree"]
                                cursor = dbuser[f"{userid}"]
                                check = cursor.find_one({"id": userid})
                                if check is None:
                                    insert = {
                                        "id": userid, "mines": 1, "crash": 0
                                    }
                                    cursor.insert_one(insert)
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 25)
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
                                    elif a == 12:
                                        mine22 = "🟩"
                                    elif a == 23:
                                        mine23 = "🟩"
                                    elif a == 24:
                                        mine21 = "🟩"
                                    elif a == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)

                                else:
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 25)
                                    addmines = check['mines'] + 1
                                    cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
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
                                    elif a == 12:
                                        mine22 = "🟩"
                                    elif a == 23:
                                        mine23 = "🟩"
                                    elif a == 24:
                                        mine21 = "🟩"
                                    elif a == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)



                        elif float(minescount) == 2:

                            guildid = ctx.guild.id
                            dbguild = cluster["guilds"]
                            cur = dbguild[f"{guildid}"]
                            guildcheck = cur.find_one({"id": guildid})
                            if guildcheck is None:
                                input = {
                                    "id": guildid, "mines": 1, "crash": 0
                                }
                                cur.insert_one(input)
                                userid = ctx.author.id
                                dbuser = cluster["usersfree"]
                                cursor = dbuser[f"{userid}"]
                                check = cursor.find_one({"id": userid})
                                if check is None:
                                    insert = {
                                        "id": userid, "mines": 1, "crash": 0
                                    }
                                    cursor.insert_one(insert)
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 11)
                                    b = random.randint(12, 25)
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

                                    if b == 12:
                                        mine12 = "🟩"
                                    elif b == 13:
                                        mine13 = "🟩"
                                    elif b == 14:
                                        mine14 = "🟩"
                                    elif b == 15:
                                        mine15 = "🟩"
                                    elif b == 16:
                                        mine16 = "🟩"
                                    elif b == 17:
                                        mine17 = "🟩"
                                    elif b == 18:
                                        mine18 = "🟩"
                                    elif b == 19:
                                        mine19 = "🟩"
                                    elif b == 20:
                                        mine20 = "🟩"
                                    elif b == 21:
                                        mine21 = "🟩"
                                    elif b == 12:
                                        mine22 = "🟩"
                                    elif b == 23:
                                        mine23 = "🟩"
                                    elif b == 24:
                                        mine21 = "🟩"
                                    elif b == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)

                                else:
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 11)
                                    b = random.randint(12, 25)
                                    addmines = check['mines'] + 1
                                    cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
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

                                    if b == 12:
                                        mine12 = "🟩"
                                    elif b == 13:
                                        mine13 = "🟩"
                                    elif b == 14:
                                        mine14 = "🟩"
                                    elif b == 15:
                                        mine15 = "🟩"
                                    elif b == 16:
                                        mine16 = "🟩"
                                    elif b == 17:
                                        mine17 = "🟩"
                                    elif b == 18:
                                        mine18 = "🟩"
                                    elif b == 19:
                                        mine19 = "🟩"
                                    elif b == 20:
                                        mine20 = "🟩"
                                    elif b == 21:
                                        mine21 = "🟩"
                                    elif b == 12:
                                        mine22 = "🟩"
                                    elif b == 23:
                                        mine23 = "🟩"
                                    elif b == 24:
                                        mine21 = "🟩"
                                    elif b == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)
                            else:
                                userid = ctx.author.id
                                dbuser = cluster["usersfree"]
                                cursor = dbuser[f"{userid}"]
                                check = cursor.find_one({"id": userid})
                                if check is None:
                                    insert = {
                                        "id": userid, "mines": 1, "crash": 0
                                    }
                                    cursor.insert_one(insert)
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 11)
                                    b = random.randint(12, 25)
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

                                    if b == 12:
                                        mine12 = "🟩"
                                    elif b == 13:
                                        mine13 = "🟩"
                                    elif b == 14:
                                        mine14 = "🟩"
                                    elif b == 15:
                                        mine15 = "🟩"
                                    elif b == 16:
                                        mine16 = "🟩"
                                    elif b == 17:
                                        mine17 = "🟩"
                                    elif b == 18:
                                        mine18 = "🟩"
                                    elif b == 19:
                                        mine19 = "🟩"
                                    elif b == 20:
                                        mine20 = "🟩"
                                    elif b == 21:
                                        mine21 = "🟩"
                                    elif b == 12:
                                        mine22 = "🟩"
                                    elif b == 23:
                                        mine23 = "🟩"
                                    elif b == 24:
                                        mine21 = "🟩"
                                    elif b == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)

                                else:
                                    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥', '🟥'
                                    a = random.randint(1, 11)
                                    b = random.randint(12, 25)
                                    addmines = check['mines'] + 1
                                    cursor.update_one({"id": userid}, {"$set": {"mines": addmines}})
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

                                    if b == 12:
                                        mine12 = "🟩"
                                    elif b == 13:
                                        mine13 = "🟩"
                                    elif b == 14:
                                        mine14 = "🟩"
                                    elif b == 15:
                                        mine15 = "🟩"
                                    elif b == 16:
                                        mine16 = "🟩"
                                    elif b == 17:
                                        mine17 = "🟩"
                                    elif b == 18:
                                        mine18 = "🟩"
                                    elif b == 19:
                                        mine19 = "🟩"
                                    elif b == 20:
                                        mine20 = "🟩"
                                    elif b == 21:
                                        mine21 = "🟩"
                                    elif b == 12:
                                        mine22 = "🟩"
                                    elif b == 23:
                                        mine23 = "🟩"
                                    elif b == 24:
                                        mine21 = "🟩"
                                    elif b == 25:
                                        mine25 = "🟩"

                                    one = mine1 + mine2 + mine3 + mine4 + mine5
                                    two = mine6 + mine7 + mine8 + mine9 + mine10
                                    three = mine11 + mine12 + mine13 + mine14 + mine15
                                    four = mine16 + mine17 + mine18 + mine19 + mine20
                                    five = mine21 + mine22 + mine23 + mine24 + mine25

                                    ok = await ctx.respond(
                                        embed=discord.Embed(description="Checking the API",
                                                            color=discord.Color.yellow()))
                                    time.sleep(2)
                                    user = ctx.author
                                    title = f"Hound Predictor"
                                    chance = random.randint(27, 65)
                                    color = 0xe81a1a
                                    data = {'one': f'{one}',
                                            'two': f'{two}',
                                            'three': f'{three}',
                                            'four': f'{four}',
                                            'five': f'{five}',
                                            'chance': f'{chance}',
                                            'minescount': f'{minescount}',
                                            }
                                    # Write JSON file
                                    with io.open(f'/home/container/mines/{round_id}.json', 'w',
                                                 encoding='utf8') as outfile:
                                        str_ = json.dumps(data,
                                                          indent=4, sort_keys=True,
                                                          separators=(',', ': '), ensure_ascii=False)
                                        outfile.write(to_unicode(str_))

                                    desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```\n**Tiles**\n```{minescount}```"
                                    em = discord.Embed(description=desc, color=color, title=title)
                                    em.set_footer(text=f"discord.gg/houndpredictor")
                                    em.set_thumbnail(
                                        url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                                    await ok.edit_original_message(embed=em)

                elif float(dashcount) < 4:
                    await ctx.respond(
                        embed=discord.Embed(description=f"Invalid Round ID\n```{round_id}```",
                                            color=discord.Color.red()))
            else:
                await ctx.respond(
                    embed=discord.Embed(description=f"Invalid Round ID\n```{round_id}```", color=discord.Color.red()))


cluster = MongoClient([''])


def setup(bot):
    bot.add_cog(Mines(bot))
