import discord
from discord.ext import commands
import sys
import morse
class Morse():
    def __init__(self, client):
        self.client = client
        
    @property 
    async def wcode(self, txt, code):
        code = morse.mtt()
        for z in txt:
            await self.client.say(code[z])
            
    
    
    
    @commands.command()
    async def rcode(self, *, message):
        code = morse.mtt()
        wcode(message, code)
        
def setup(client):
    client.add_cog(Morse(client))
        
