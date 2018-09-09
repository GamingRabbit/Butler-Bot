import discord
from discord.ext import commands

class Don_t_Use_The_default_help_command():
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def Use_James_commands():
        await client.say("Use James,commands !")
        
