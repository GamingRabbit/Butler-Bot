import discord
from discord.ext import commands
import random

class rds():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rs(self):
        wordI=[
            "I",
            "You",
            "It",
            "He",
            "She"
        ]
        await self.client.say(random.choice(wordI))
