import discord
from discord.ext import commands
import random

class rds():
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def rs(self):
        wordI=[
            "I",
            "You",
            "It",
            "He",
            "She"
        ]
        wordII=[
            "will",
            "wont"]
        await self.client.say(random.choice(wordI)+" "+random.choice(wordII))
        
def setup(client):
    client.add_cog(rds(client))
