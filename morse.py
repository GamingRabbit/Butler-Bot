import discord
from discord.ext import commands

class Morse():
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases = ["morsetotext", "MTT", "Mtt", "mTt", "mtT", "mTT"], pass_context = True)
    async def mtt(self, ctx, message):
      morsetext = message
      code = {}
      for l in morsetext:
        w = l.split()
        code[w[0]] = w[1]
        
      for i in range(97,123):
        code[chr(i)] = code[chr(i - 32)]
      await self.client.say(code)
    
def setup(client):
    client.add_cog(Morse(client))
