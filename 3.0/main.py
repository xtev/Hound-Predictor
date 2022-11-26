import asyncio
import random
from typing import List

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
bot.load_extension('cogs.crash')
bot.load_extension('cogs.mines')
bot.load_extension('cogs.profile')




@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


bot.run("token")