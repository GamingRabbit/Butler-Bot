import discord
from discord.ext import commands

class Members():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def joined(self,ctx,member: discord.Member):
        if member == None:
            member = ctx.message.author            
        await self.client.say(':clock1:{0.name} joined in {0.joined_at}'.format(member))

        
    @commands.command(pass_context=True)
    async def info(self,ctx,member: discord.Member=None):
        'Show info about a member'
        if member is None:
            member = ctx.message.author
        em = discord.Embed(color=0x00ff00)
        em.add_field(name='Name', value='{0.name}'.format(member))
        em.add_field(name='ID', value='{0.id}'.format(member))
        em.add_field(name='Top Role', value='{0.top_role}'.format(member))
        em.add_field(name='Roles', value=', '.join(g.name for g in member.roles))
        em.add_field(name='Joined', value='{0.joined_at}'.format(member))
        em.set_thumbnail(url=member.avatar_url)
        await self.client.say(embed=em)
        
    @commands.command(pass_context=True)
    async def changelog(self):
      em = discord.Embed()
      em.add_field(name='0.8. and previous versions', value='I don"t remeber everything what I"ve done in every version')
      em.add_field(name='0.9.',  value='added a new Cog called Info2\n')
      em.add_field(name='.', value='.\n')
      em.add_field(name='1.0.0', value='added some new cogs and made a new support server.\n')
      em.add_field(name='1.0.0.1', value='fixed the changelog')
      em.add_field(name='1.5.0', value='made a little calculator.')
      em.add_field(name='.', value='.\n')
      em.add_field(name='1.5.5', value='made a delete messages command')
      await self.client.say(embed=em)

def setup(client):
    client.add_cog(Members(client))
