'''import discord
from discord.ext import commands
import sys
import morse
import mthree
class Morse():
    def __init__(self, client):
        self.client = client
        
     
    
            
    
    code = morse.mtt()
    
    @commands.command()
    async def rcode(self, message : txt, code):
        mthree.wcode(txt, code)
        
def setup(client):
    client.add_cog(Morse(client))
        
'''
