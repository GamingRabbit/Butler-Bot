import discord
from discord.ext import commands
import cter

class Don_t_Use_The_Default_Help_Command():
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["halp"])
    async def Use_James_commands(self):
        await self.client.say("Use James,commands !")
        cter.counter +=1
        await self.client.say("btw, you are the" + counter "user who used this command")
        
def setup(client):
    client.add_cog(Don_t_Use_The_Default_Help_Command(client))
