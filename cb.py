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
        wordIII=[
            "get",
            "destroy",
            "kill",
            "buy you a",
            "paint your face green, print a toothbrush, record a video with it and make a toast for"
        ]
        wordIIII=[
            "Donald Trump",
            "You",
            "Me",
            "it",
            "a video card",
            "your Video card",
            "my energy drink",
            "**__~~*E*~~__**"
        ]
        await self.client.say(random.choice(wordI)+" "+random.choice(wordII)+" "+random.choice(wordIII)+" "+random.choice(wordIIII))
        
def setup(client):
    client.add_cog(rds(client))
