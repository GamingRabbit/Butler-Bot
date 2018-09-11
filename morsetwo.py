import discord
from discord.ext import commands
import sys
import morse
class Morse():
    def __init__(self, client):
        self.client = client
        
    
    def wcode(txt, code):
        for z in txt:
            try:
                await self.client.say(code[z])
        print()
    
    code = morse.mtt()
    
    @commands.command()
    async def rcode(self, *, message):
        wcode(message, code)
