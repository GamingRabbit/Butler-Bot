import discord
from discord.ext import commands

class Calculator():
    def __init__(self, client):
        self.client = client
        
    @commands.command(self)
    async def add(leftn : int, rightn : int):
        await self.client.say(leftn + rightn)
        
    @commands.command(self)
    async def multiply(leftn : int, rightn : int):
        await self.client.say(leftn * rightn)
        
    @commands.command(self)
    async def sub(leftn : int, rightn : int):
        await self.client.say(leftn - rightn)
        
def setup(client):
    client.add_cog(Calculator(client))
