import discord
from discord.ext import commands
import random
class rg():
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def gg(self, message):
        x = random.randint(1,3)
        if message == x:
            await self.client.say("You've Won  and guessed the number, here is your reward: a nice :cookie:")
        else:
            await self.client.say("Nope, wrong number")
def setup(client):
    client.add_cog(rg(client))
