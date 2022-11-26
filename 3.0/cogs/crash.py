from datetime import datetime
from math import floor
from random import randint
import cloudscraper, requests
import json
import threading
import asyncio

import discord
from discord.ext import commands

class Crash(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guild_ids=[1007651484789383269])
    async def crash(self, ctx):
        user = ctx.author
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        games = scraper.get("http://rest-bf.blox.land/games/crash").json()
        if ctx.author.id:
            ok = await ctx.respond(embed=discord.Embed(description="Checking the API", color=discord.Color.purple()))

            def lol():
                r = scraper.get(
                    "http://rest-bf.blox.land/games/crash").json()["history"]
                yield [
                    r[0]["crashPoint"],
                    [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]
                ]

            for game in lol():
                games = game[1]
                avg = sum(games) / len(games)
                chance = 1
                for game in games:
                    chance = chance = 95 / game
                    prediction = (1 / (1 - (chance)) + avg) / 2
                    if float(prediction) > 2:
                        color = 0xe81a1a
                    else:
                        color = 0xe81a1a

                    if float(prediction) < 1:
                        if float(prediction) < -3:
                            await ok.edit_original_message(embed=discord.Embed(description="Unable to Predict a result",
                                                                               color=discord.Color.purple()))
                        elif float(prediction) > -3:
                            crash = prediction + 2


                    else:
                        crash = prediction

                    title = f"Hound Predictor"
                    thumbnail = f"{user.display_avatar.url}"
                    desc = f"**Crash**\n```{crash:.2f}x```\n**Accuracy**\n```{chance:.2f}%```"
                    em = discord.Embed(description=desc, color=color, title=title)
                    await ok.edit_original_message(embed=em)


def setup(bot):
    bot.add_cog(Crash(bot))