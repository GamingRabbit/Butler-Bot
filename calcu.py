import discord
from discord.ext import commands

class Calculator():
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def add(self, leftn : int, rightn : int):
        await self.client.say(leftn + rightn)
        
    @commands.command()
    async def multiply(self, leftn : int, rightn : int):
        await self.client.say(leftn * rightn)
        
    @commands.command()
    async def sub(self, leftn : int, rightn : int):
        await self.client.say(leftn - rightn)
        
def setup(client):
    client.add_cog(Calculator(client))
