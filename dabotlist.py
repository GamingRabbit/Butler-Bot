import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging
import os

class DiscordBotsOrgAPI:
    

    def __init__(self, client):
        self.client = client
        self.token = os.getenv('DBLT')  #  set this to your DBL token
        self.dblpy = dbl.Client(self.client, self.token)
        self.client.loop.create_task(self.update_stats())

    async def update_stats(self):
        

        while True:
            logger.info('attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('posted server count')
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)


def setup(client):
    global logger
    logger = logging.getLogger('client')
    client.add_cog(DiscordBotsOrgAPI(client))
