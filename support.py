import discord
from discord.ext import commands

class sport():
    def __init__(self, client):
        self.client = client




        @commands.command()
        async def support(self):
          await self.client.say("join my support Server : https://discord.gg/Te6g5XF")
def setup(client):
    client.add_cog(sport(client))
