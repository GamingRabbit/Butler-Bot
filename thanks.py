@commands.command(name="thanks",
                aliases = ["Thanks"],
                pass_context= True)
async def tanks(self, ctx):
    tanks = discord.Embed(name = "Special thanks to:" description = "Adytzu96#3030 , \n everyone who is using this Bot!")
    await client.say(embed = tanks)
