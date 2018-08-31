import discord
from discord.ext import commands

class Thanks():
    def __init__(self, client):
        self.client = client

    @commands.command(name="thanks",
                    aliases = ["Thanks"],
                    pass_context= True)
    async def tanks(self, ctx):
        tanks = discord.Embed(name = "Special thanks to:", description = "Adytzu96#3030 , \n everyone who is using this Bot!")
        await client.say(embed = tanks)

    
def setup(client):
    client.add_cog(Thanks(client))
