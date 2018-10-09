import discord
from discord.ext import commands
import json

class nsfw():
    def __init__(self, client):
        self.client = client
 
    @commands.command(pass_context = True)
    async def rule34(self, ctx ,*,message = None):
        url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index'
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.image()
            response = json.loads(response)
            await client.say(response)
            
def setup(client):
    client.add_cog(nsfw(client))
