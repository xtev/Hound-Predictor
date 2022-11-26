import io
import json
import time
from pathlib import Path
from math import floor
from random import choice, random

from numpy import unicode

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
from discord import Option
import discord
from discord.ext import commands

class Mines(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @discord.slash_command(guild_ids=[1007651484789383269])
    async def mines(self, ctx, round_id):
        round_id = str(round_id)
        round_length = len(round_id)
        if round_length <36 or round_length > 36:
            await ctx.respond(embed=discord.Embed(description=f"Invalid Round ID\n```{round_id}```", color=discord.Color.red()))
        elif round_length == 36:
            path_to_file = f'/home/container/round/{round_id}.json'
            path = Path(path_to_file)

            if path.is_file():

                async def get_round_data():
                    with open(f"/home/container/round/{round_id}.json", "r", encoding='utf8') as f:
                        round = json.load(f)

                    return round

                ok = await ctx.respond(
                    embed=discord.Embed(description="Checking the API", color=discord.Color.yellow()))
                time.sleep(2)
                user = ctx.author
                title = f"Hound Predictor"
                chance = floor((random() * 50) + 50)
                color = 0xe81a1a
                roundtype = await get_round_data()
                one1 = roundtype["one"]
                two2 = roundtype["two"]
                three3 = roundtype["three"]
                four4 = roundtype["four"]
                five5 = roundtype["five"]
                chance1 = roundtype["chance"]

                desc = f"**Prediction**\n```{one1}\n{two2}\n{three3}\n{four4}\n{five5}```\n**Accuracy**\n```{chance1}%```\n**RoundID**\n```{round_id}```"
                em = discord.Embed(description=desc, color=color, title=title)
                await ok.edit_original_message(embed=em)
            else:
                async def get_data_data():
                    with open(f"/home/container/data.json", "r", encoding='utf8') as f:
                        data = json.load(f)

                    return data
                WORDS = (
                    "🟩🟥🟥🟥🟥",
                    "🟥🟩🟥🟥🟥",
                    "🟥🟥🟩🟥🟥",
                    "🟥🟥🟥🟩🟥",
                    "🟥🟥🟥🟥🟩",
                    "🟥🟥🟩🟥🟥",
                    "🟩🟥🟥🟥🟥",
                    "🟥🟩🟥🟥🟥",
                    "🟥🟥🟩🟥🟥",
                    "🟥🟥🟥🟩🟥",
                    "🟥🟥🟥🟥🟩",
                    "🟥🟥🟥🟩🟥",
                    "🟥🟥🟥🟥🟥",
                    "🟥🟥🟩🟥🟥",
                    "🟥🟥🟥🟥🟥",
                    "🟥🟥🟥🟥🟥",
                )
                one = choice(WORDS)
                two = choice(WORDS)
                three = choice(WORDS)
                four = choice(WORDS)
                five = choice(WORDS)

                ok = await ctx.respond(embed=discord.Embed(description="Checking the API", color=discord.Color.yellow()))
                time.sleep(2)
                user = ctx.author
                title = f"Hound Predictor"
                chance = floor((random() * 50) + 50)
                color = 0xe81a1a
                datatype = await get_data_data()
                uses = datatype["minesuse"]
                fuck = int(uses) + int(1)
                usess = uses + str(1)
                data = {'one': f'{one}',
                        'two': f'{two}',
                        'three': f'{three}',
                        'four': f'{four}',
                        'five': f'{five}',
                        'chance': f'{chance}',
                        }
                with io.open(f'/home/container/round/{round_id}.json', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(data,
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(str_))

                desc = f"**Prediction**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Accuracy**\n```{chance}%```\n**RoundID**\n```{round_id}```"
                em = discord.Embed(description=desc, color=color, title=title)
                await ok.edit_original_message(embed=em)


def setup(bot):
    bot.add_cog(Mines(bot))