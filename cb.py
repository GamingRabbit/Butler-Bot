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
            "She",
            "Donald Trump",
            "A toast"
        ]
        wordII=[
            "will",
            "wont"]
        wordIII=[
            "get",
            "destroy",
            "kill",
            "buy you a",
            "buy you",
            "sell",
            "paint your face green, print a toothbrush, record a video with it and make a toast for",
            "take",
            "hack",
            "cook",
            "bake"
        ]
        wordIIII=[
            "Donald Trump",
            "Donald Duck",
            "Donald Truck",
            "Thomas the tank engine",
            "you",
            "me",
            "it",
            "a video card",
            "your Video card",
            "my energy drink",
            "**__~~*E*~~__**",
            "Germany",
            "Russia",
            "USA",
            "China",
            "Fallout 76",
            "a bot",
            "Butter Bot",
            "Butler Bot",
            "Battlefield V"
        ]
        await self.client.say(random.choice(wordI)+" "+random.choice(wordII)+" "+random.choice(wordIII)+" "+random.choice(wordIIII))
        
def setup(client):
    client.add_cog(rds(client))
