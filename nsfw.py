import discord
from discord.ext import commands

class nsfw():
    def __init__(self, client):
        self.client = client
 
    @commands.command(pass_context = True)
    async def rule34(self, ctx ,*,message : discord.message):
        if 'nsfw' in ctx.message.channel.name:
            if message == None:
                await self.client.say('https://rule34.xxx/index.php?page=post&s=random')
            else:
                await self.client.say('https://rule34.xxx/index.php?page=post&s=list&tags={0}'.format(message))
                
        else:
            await self.client.say("This channel doesn't has nsfw inside it's name. Please note that I can't check IF a nsfw channel is a nsfw channel. I can only check if 'nsfw' is in the channel name.") 

            
def setup(client):
    client.add_cog(nsfw(client))
