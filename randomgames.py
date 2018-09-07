import discord
from discord.ext import commands
import random
class rg():
    def __init__(self, client):
        self.client = client
   @commands.command()     
   async def gg(message):
    rand = random.randint(0,2)
    user_choice=message
    choices = ["1", "2", "3"]
    outcome_list = ["won", "lose!", "lose."]
    result =(choices.index(user_choice)+rand)%3
    await client.say("I chose {}, you {}".format(choices[result], outcome_list[rand]))
def setup(client):
    client.add_cog(rg(client))
