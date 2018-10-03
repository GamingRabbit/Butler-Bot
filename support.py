import discord
from discord.ext import commands

class support():
    def __init__(self, client):
        self.client = client




        @commands.command()
        async def support(self):
          await client.say("join my support Server : https://discord.gg/Te6g5XF")
def setup(client):
    client.add_cog(support(client))
