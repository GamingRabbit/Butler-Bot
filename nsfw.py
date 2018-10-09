import discord
from discord.ext import commands
import json
import aiohttp
import io

class nsfw():
    def __init__(self, client):
        self.client = client
 
    @commands.command(pass_context = True)
    async def rule34(self, ctx ,*,message = None):
        url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index'
        async with aiohttp.ClientSession() as session:
            async with session.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index") as resp:
                buffer = io.BytesIO(await resp.read())
        channel = ctx.message.channel

        await self.client.send_file(channel, fp=buffer, filename="Image")
            
def setup(client):
    client.add_cog(nsfw(client))
