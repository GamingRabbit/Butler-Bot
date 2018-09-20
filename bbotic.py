import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import os
import sys
import traceback


BOT_PREFIX = ("!j!?", "James,", "James, ", "james,")


client = Bot(command_prefix=BOT_PREFIX)
c2 = discord.Client()
client.load_extension('info2')
client.load_extension('thanks')
client.load_extension('eh')
client.load_extension('dabotlist')
client.load_extension('randomgames')
client.load_extension('calcu')
client.load_extension('jc')
client.load_extension('nsfw')
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Use James,commands"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

@client.command()
async def hey(ctx):
    responses =["That is a resounding no", "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "no, sir", "yes", "of course!"]
    await client.say(random.choice(responses))
    
@client.command(pass_context=True)
async def counter(ctx):
    embed = discord.Embed(title="Counter", description="Server info", color=0x6FA8DC)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Owner", value=ctx.message.server.owner.mention)
    embed.add_field(name="Members", value=ctx.message.server.member_count)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="About me",description="Hello Sir, I'm *James* the `Butler Bot`, I'm a Bot made by **Gaming Rabbit #9860**. If you want to invite me type James,invite.",color=0x00ff00)
    await client.say(embed=embed)
    
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command()
async def double(number):
    squared_value = int(number) + int(number)
    await client.say(str(number) + " x2 is " + str(squared_value))

@client.command(pass_context=True,hidden=True)
async def apartment(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="apartement")
    role2 = discord.utils.get(user.server.roles, name="a")
    await client.add_roles(user, role)
    await client.say("Here are the keys, but don't be to long in the room")
    await asyncio.sleep(100)
    await client.say("Sorry, you can't stay here for too long, you got to got sir")
    await client.remove_roles(user, role)

@client.command(name='where',
                description="should I go",
                brief="should I go",
                aliases=['location', 'b', 'ughno'],
                pass_context=True, hidden=True)
async def nineteen_ball(context):
    possible_responses = [
        'Go left, sir',
        'Go right, sir',
        'You should just go forward, sir',
        'I would recommend to stay, sir',
        'The apartment is a nice place, I would recommend you to go there',
        'I dont know sir, this is your decision',
        'why dont we just go to the nearest house',
        'just saty here sir, here is a nice place',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='if',
                description="I would (your question) what would you do",
                brief="I would (your question) what would you do",
                aliases=['what', 'would', 'happen'],
                pass_context=True,hidden=True)
async def nineninenine_ball(context):
    possible_responses = [
        'I would run away',
        'I would need to shoot you',
        'Too hard to tell',
        'I dont know',
        'Definitely, I would call the police',
        'I would build a wall if you would do this',
        'I would bake a cake if you would do this',
        'I would play on your computer sir',
        'I would build a X-01 power armor and kill you if you do this',
        'I would just accept it',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='Is',
                description="this funny(your question/joke/video)",
                brief="this funny",
                aliases=['is', 'this', 'funny'],
                pass_context=True,hidden=True)
async def fortwenty_ball(context):
    possible_responses = [
        'If you call this funny I dont longer want to be friends with you',
        'THIS IS AWFUL',
        'Yes, sir',
        'not really',
        'Definitely',
        'no, sir',
        'yes',
        'of course!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name="you",
                description="won",
                brief="won",
                aliases=['u', 'have', 'won'],
                pass_context=True,hidden=True)
async def fuck_yeah(context):
    possible_responses = [
        'ok',
        'good',
    ]
    await client.say(random.choice(possible_responses))

@client.command(name="ok",
                description="ok",
                brief="ok",
                aliases=['o', 'k', 'okey'],
                pass_context=True)
async def ok_questionmark(context):
    possible_responses = [
        'ok',
        'not ok',
        'it is ok',
        'yep',
        'No',
    ]
    await client.say(random.choice(possible_responses))    

@client.command(pass_context = True)
@commands.has_permissions(kick_members = True) 
async def kick(ctx, userName: discord.User):
    await client.kick(userName)
    await client.say("sucessfully kicked, sir!")

@client.command(pass_context = True)
@commands.has_permissions(ban_members = True) 
async def ban(ctx, userName: discord.User):
    await client.ban(userName)
    await client.say("sucessfully banned, sir!")

@client.command()
async def say(*,message):
         await client.say(message)

@client.command(name="rps",
                desription="ROCK PAPER SCISSORS",
                brief="ROCK PAPER SCISSORS")
async def rps(message):
    rand = random.randint(0,2)
    user_choice=message
    choices = ["paper", "scissors", "rock"]
    outcome_list = ["did not win and you did not lost, it's a draw", "lose", "win"]
    result =(choices.index(user_choice)+rand)%3
    await client.say("I chose {}, you {}".format(choices[result], outcome_list[rand]))

@client.command(pass_context=True)
async def ping(ctx):
    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, 'Pong! That took {:.1f}ms.'.format(1000*diff.total_seconds()))

@client.event
async def on_member_join(Member):
    role = discord.utils.get(Member.server.roles,  name="Unverified")
    await client.add_roles(Member, role)
    
    

@client.command(hidden = True)
async def grhrr():
               embed = discord.Embed(title="Private Port role requirements:",description="`PrivatePortaccess1`: everyone can have it,just ping me(Gaming Rabbit)\n Other Privat Port access roles: `Medium`: For long members `High`: for friends only\n")
               await client.say(embed=embed)
               role = discord.utils.get(member.server.roles,  name="unverified")
               await client.add_roles(member, role)
               
@client.command(pass_context=True)
async def commands(ctx):
    await client.add_reaction(ctx.message,'\N{white heavy check mark}')
    embed = discord.Embed(title="Commands:", description="  `ping`     shows the ping of the Bot\n `thanks`    shows the special thanks\n `Invite`    Invites the Bot\n `vote`    gives the link to vote the bot up on discordbots.org(why should you do this?!)\n `changelog`    shows the versions changelog\n `google`    googles something\n `counter`    shows a little server info\n `rps`    Play Rock Paper scissors with the Bot\n `gg`    a simple guessing game(1 -3)\n `say`\n `double`    doubles a number\n `add`    adds two numbers together\n `multi`    multiplies two numbers\n `sub`    substracts two numbers\n `square`     squares a number\n `hey`     answers a question with yes or no \n `about`\n `clear`    deletes messages(range: 2 - 100)\n `kick`     kicks a member(role `kicker` required)\n `ban`    bans a member\n `joined`      gives out the jointime (in UTC)\n `info`    infos about a member\you\n\n\n", color=0x00ff00)
    embed.set_footer(text="Use James,help (command) for more help with the command")
    await client.say(embed=embed)
    await client.send_message(ctx.message.author, embed=embed)

@client.command(pass_context=True, hidden=True)
async def Terminal(ctx):
    counter = 0
    channel = discord.Object(id='477465945057525760')
    counter += 1
    await client.send_message(channel," ---------------------------")
    await client.send_message(channel,"`Butler Bot Main Terminal`")
    await client.send_message(channel,"`Status`")
    await asyncio.sleep(1)
    await client.send_message(channel,"|`Online`|")
    resp = await client.send_message(channel,'`Loading`')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, '` Ping: {:.1f}ms.`'.format(1000*diff.total_seconds()))
    await client.send_message(channel,"-------------------------- \n `Terminal commands:`\n `stdown`\n `status`\n `ls`\n `load`\n `unload`\n `reload`\n ---------------------------")

@client.command(pass_context=True, hidden=True)
async def stdown(ctx):
    if ctx.message.author.id == '353501847324983299':
        await client.say("shutting down...")
        await client.logout()
    else:
        await client.say("You don't have the permission to do this!!!!")
        print(ctx.message.author, "tried to shut me down!")

@client.command(pass_context=True,hidden=True,aliases = ["state"])
async def status(ctx,*,message):
    if ctx.message.author.id == '353501847324983299':
         await client.change_presence(game=Game(name= message))
         await client.say("`successfully changed presence`")
    else:
        await client.say("You don't own me!")

@client.command(pass_context=True, hidden=True)
async def load(ctx,extension_name : str):
    if ctx.message.author.id == '353501847324983299':
        try:
            client.load_extension(extension_name)
            await client.say("`{} loaded.`".format(extension_name))
        except (AttributeError, ImportError) as e:
            await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
    else:
        await client.say("I wont let YOU do this")

@client.command(pass_context=True,hidden=True)
async def unload(ctx,extension_name : str):
    if ctx.message.author.id == '353501847324983299':
        client.unload_extension(extension_name)
        await client.say("`{} unloaded.`".format(extension_name))
    else:
        await client.say("Reporting you for trying to unload {}".format(extension_name))

@client.command(pass_context=True,hidden=True)
async def reload(ctx,extension_name : str):
    if ctx.message.author.id == '353501847324983299':
        client.unload_extension(extension_name)
        try:
            client.load_extension(extension_name)
            await client.say("`{} reloaded.`".format(extension_name))
        except (AttributeError, ImportError) as e:
            await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
    else:
        await client.say("You can't reload cogs, because you are you.")


@client.command(aliases = ["invite"])
async def Invite():
    await client.say("Heres my Invite link: https://discordapp.com/api/oauth2/authorize?client_id=468353740903022592&permissions=8&scope=bot")
    await client.say("also feel free to join my (new) Server : https://discord.gg/Te6g5XF")

@client.command()
async def vote():
    await client.say("You really want to vote ME up on discordbots.org? If you really want to vote me up thanks heres my link:https://discordbots.org/bot/468353740903022592")

    
@client.command()
async def servers():
    await client.say(len(client.servers))
    
    
@client.command(hidden=True, pass_context=True)
async def ls(ctx):
    if ctx.message.author.id == '353501847324983299':
        for server in client.servers:
            await client.say(server.name)
            
@client.command()
async def USRS():
    usrs = list(client.get_all_members())
    await client.say(len(usrs))

@client.event    
async def on_command_error(self, error: Exception):
    if isinstance(error, commands.CommandNotFound):
        await client.say("Error, command not found!")
@client.command(hidden=True)
async def STFU():
    possible_responses = [
        'https://youtu.be/OLpeX4RRo28',
        'https://youtu.be/nc_LIR5ExIU'
        
    ]
    await client.say(random.choice(possible_responses))

@client.command(pass_context = True)
async def clear(ctx, number):
    if ctx.message.author.server_permissions.administrator:
        mgs = []
        number = int(number)
        async for x in client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await client.delete_messages(mgs)
    else:
        await client.say("you don't have the permissions to do that")


@client.command()
async def google(*, query):
    search = query
    URL = 'https://www.google.com/search?q='
    words = search.split(" ")
    num = 0
    for w in words:
        if num is 0:
            URL = URL + w
            num = 1
        else:
            URL = URL + "+"+ w
    embed = discord.Embed(title = 'Results', url = URL)
    await client.say(embed = embed)
    
@client.command()
async def sayd(ctx,*,message):
         await client.delete_message(ctx.message.channel,ctx.message)
         await client.say(message)

    
    
client.loop.create_task(list_servers())
client.run(os.getenv("TOKEN"))
