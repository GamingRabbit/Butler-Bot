'''import discord
from discord.ext import commands
import sys
import morse
import mthree
class Morse():
    def __init__(self, client):
        self.client = client
        
     
    
            
    
    code = morse.mtt()
    
    @commands.command(pass_context = True)
    async def rcode(self, ctx, code : morse.mtt()):
        mthree.wcode(ctx.message.content, code)
        
def setup(client):
    client.add_cog(Morse(client))
   '''     

