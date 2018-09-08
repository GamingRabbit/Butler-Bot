import discord
from discord.ext import commands

class Calculator():
    def __init__(self, client):
        self.client = client
        
    @commands.command(self)
    async def add(leftn : int, rightn : int):
        await self.client.say(leftn + rightn)
