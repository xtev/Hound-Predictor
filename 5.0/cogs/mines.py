import cloudscraper
import discord
from pymongo import MongoClient

cluster = MongoClient(['mongodb+srv://'])
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)


class Start(discord.ui.View):
    def __init__(self, user, auth):
        self.user = user
        self.auth = auth
        super().__init__(timeout=None)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def green(self, button, interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 0
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="p")
    async def gren(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 1
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="pe")
    async def gre(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 2
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="pee")
    async def gr(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 3
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="peee")
    async def g(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 4
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="peeee")
    async def ge(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 5
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="peeeee")
    async def gee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 6
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary, custom_id="peeeeee")
    async def geee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 7
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 8
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 9
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 10
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 11
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 12
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 13
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 14
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 15
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 16
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction, ):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 17
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 18
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 19
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 20
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 21
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 22
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 23
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.secondary)
    async def geeeeeeeeeeeeeeeeeee(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user.id:
            userid = self.user.id
            dbuser = cluster["users"]
            cursor = dbuser[f"{userid}"]
            check = cursor.find_one({"id": userid})
            spot = 24
            token = check['token']
            start = scraper.post(f'https://rest-bf.blox.land/games/mines/action',
                                 headers={'x-auth-token': token},
                                 json={'cashout': False, 'mine': spot}).json()

            if start['exploded'] == True:
                button.disabled = True
                button.label = "💥"
                for child in self.children:
                    child.disabled = True
                desc = f"**Round ID**\n```{start['game']['uuid']}```\n**Bombs**\n```{start['game']['minesAmount']}```\n**Client Seed**\n```{start['game']['clientSeed']}```\n**Loss**\n```{start['game']['betAmount']}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
            else:
                button.disabled = True
                button.label = "🟩"
                gamedata = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
                profit = gamedata['game']['betAmount'] * gamedata['multiplier'] - gamedata['game']['betAmount']
                desc = f"**Round ID**\n```{gamedata['game']['uuid']}```\n**Bombs**\n```{gamedata['game']['minesAmount']}```\n**Client Seed**\n```{gamedata['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.response.edit_message(embed=em, view=self)
        else:
            desc = f"```Sorry this is not your game {interaction.user} ```"
            color = 0xe81a1a
            em = discord.Embed(description=desc, color=color)
            await interaction.response.defer()
            await interaction.followup.send(embed=em, ephemeral=True)


class Mines(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print("Self Loaded")

    @discord.slash_command()
    async def play(self, interaction: discord.Interaction, robux: int, bombs: int):
        userid = interaction.user.id
        dbuser = cluster["users"]
        cursor = dbuser[f"{userid}"]
        check = cursor.find_one({"id": userid})
        if check is None:
            await interaction.respond(embed=discord.Embed(description=f"```No Account```", color=0xe81a1a))
        else:
            scraper = cloudscraper.create_scraper(browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            })
            token = check['token']
            fuckery = scraper.get(f'https://rest-bf.blox.land/user', headers={'x-auth-token': token}).json()
            user = fuckery['user']
            wallet = user['wallet']
            if float(robux) > wallet:
                await interaction.respond(
                    embed=discord.Embed(description=f"```Sorry you don't have enough robux```", color=0xe81a1a))
            else:
                if float(bombs) > 24:
                    await interaction.respond(
                        embed=discord.Embed(description=f"```Sorry you cannot go above 24 bombs```", color=0xe81a1a))
                else:
                    start = scraper.post(f'https://rest-bf.blox.land/games/mines/create',
                                         headers={'x-auth-token': token},
                                         json={'betAmount': robux, 'mines': bombs}).json()
                    if start['success'] == True:
                        desc = f"**Round ID**\n```{start['uuid']}```\n**Bombs**\n```{bombs}```\n**Server Hash**\n```{start['game']['serverHash']}```\n**Profit**\n```0```"
                        color = 0xe81a1a
                        em = discord.Embed(description=desc, color=color)
                        await interaction.send(embed=em, view=Start(interaction.user, token),
                                               reference=interaction.message)
                    else:
                        desc = f"```{start['error']}```"
                        color = 0xe81a1a
                        em = discord.Embed(description=desc, color=color)
                        await interaction.send(embed=em)

    @discord.slash_command()
    async def cashout(self, interaction: discord.Interaction):
        userid = interaction.user.id
        dbuser = cluster["users"]
        cursor = dbuser[f"{userid}"]
        check = cursor.find_one({"id": userid})
        if check is None:
            await interaction.respond(embed=discord.Embed(description=f"```No Account```", color=0xe81a1a))
        else:
            scraper = cloudscraper.create_scraper(browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            })
            token = check['token']
            fuckery = scraper.get(f'https://rest-bf.blox.land/games/mines', headers={'x-auth-token': token}).json()
            if fuckery['hasGame'] == True:
                game = scraper.post('https://rest-bf.blox.land/games/mines/action', headers={'x-auth-token': token},
                                    json={'cashout': True}).json()
                mine0, mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
                uncover = game['game']['uncoveredLocations']
                mines = game['game']['mineLocations']
                a = uncover
                if 0 in a:
                    mine0 = "🟩"
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
                    mine24 = "🟩"

                if 0 in mines:
                    mine0 = "💣"
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
                    mine24 = "💣"

                one = mine0 + mine1 + mine2 + mine3 + mine4
                two = mine5 + mine6 + mine7 + mine8 + mine9
                three = mine10 + mine11 + mine12 + mine13 + mine14
                four = mine15 + mine16 + mine17 + mine18 + mine19
                five = mine20 + mine21 + mine22 + mine23 + mine24
                profite = game['winnings'] - game['game']['betAmount']
                profit = round(profite, 2)
                desc = f"**Grid**\n```{one}\n{two}\n{three}\n{four}\n{five}```\n**Round ID**\n```{game['game']['uuid']}```\n**Client Seed**\n```{game['game']['clientSeed']}```\n**Profit**\n```{profit}```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.respond(embed=em)
            else:
                desc = f"```No active game```"
                color = 0xe81a1a
                em = discord.Embed(description=desc, color=color)
                await interaction.send(embed=em)


def setup(bot):
    bot.add_cog(Mines(bot))
