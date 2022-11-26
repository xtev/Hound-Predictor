import cloudscraper
import discord
from pymongo import MongoClient


class profile(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print("Profile Loaded")

    @discord.slash_command()
    async def createprofile(self, ctx, bloxflip_token):
        userid = ctx.author.id
        ok = await ctx.respond(embed=discord.Embed(description="Connecting to API", color=discord.Color.yellow()))
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
        fuckery = scraper.get(f'https://api.bloxflip.com/user', headers={'x-auth-token': bloxflip_token}).json()
        fucker = fuckery['success']
        if fucker is True:
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            if check is None:
                insert = {
                    "id": userid, "mines": 0, "crash": 0, "roulette": 0, "token": bloxflip_token
                }
                user = fuckery['user']
                username = user['robloxUsername']
                wallet = user['wallet']
                gameswon = user['gamesWon']
                gameslost = user['gamesLost']
                gamesplay = user['gamesPlayed']
                print(username)
                title = f"Hound Predictor"
                color = 0xe81a1a
                desc = f"**User**\n```{username}```\n**Balance**\n```{wallet}```\n**Games Won**\n```{gameswon}```\n**Games Lost**\n```{gameslost}```\n**Games Played**\n```{gamesplay}```"
                em = discord.Embed(description=desc, color=color, title=title)
                em.set_footer(text=f"discord.gg/houndpredictor")
                em.set_thumbnail(
                    url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
                await ok.edit_original_message(embed=em)
                print(userid)
                cursor.insert_one(insert)
            else:
                await ok.edit_original_message(embed=discord.Embed(description=f"Already created", color=discord.Color.red()))
        elif fucker is False:
            await ok.edit_original_message(
                embed=discord.Embed(description=f"Invalid bloxflip token", color=discord.Color.red()))

    @discord.slash_command()
    async def profile(self, ctx):
        userid = ctx.author.id
        ok = await ctx.respond(embed=discord.Embed(description="Connecting to API", color=discord.Color.yellow()))
        dbuser = cluster["users"]
        cursor = dbuser[f"{userid}"]
        check = cursor.find_one({"id": userid})
        if check is None:
            await ok.edit_original_message(
                embed=discord.Embed(description=f"No Account", color=discord.Color.red()))
        else:
            scraper = cloudscraper.create_scraper(browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            })
            token = check['token']
            fuckery = scraper.get(f'https://api.bloxflip.com/user', headers={'x-auth-token': token}).json()
            user = fuckery['user']
            username = user['robloxUsername']
            wallet = user['wallet']
            gameswon = user['gamesWon']
            gameslost = user['gamesLost']
            gamesplay = user['gamesPlayed']
            print(username)
            title = f"Hound Predictor"
            color = 0xe81a1a
            desc = f"**User**\n```{username}```\n**Balance**\n```{wallet}```\n**Games Won**\n```{gameswon}```\n**Games Lost**\n```{gameslost}```\n**Games Played**\n```{gamesplay}```"
            em = discord.Embed(description=desc, color=color, title=title)
            em.set_footer(text=f"discord.gg/houndpredictor")
            em.set_thumbnail(
                url="https://media.discordapp.net/attachments/1015372298863267931/1016369890048880731/unknown.png")
            await ok.edit_original_message(embed=em)


cluster = MongoClient(['mongodb+srv://'])


def setup(bot):
    bot.add_cog(profile(bot))
