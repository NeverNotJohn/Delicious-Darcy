from time import monotonic
import discord
from func import *
from discord.ext import commands
from asyncio import sleep
import atexit
import datetime
from private import key

# CLIENT:
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# DEBUG TEST CHANNEL

def DD_test():
    dd = bot.get_channel(979493252015206441)
    return dd

" ON STARTUP "
print('running!')

# INIT Message
@bot.event
async def on_ready():
    print("Discord Connected!")
    testServer = DD_test()

    now = datetime.datetime.now()
    dt_string = now.strftime(f"%d/%m/%Y %H:%M:%S")
    await testServer.send(f"\n \n ** Run time: {dt_string} * \n \n")

    # Auto change status
    readyTime = monotonic()
    while True:
        runTime = int((monotonic() - readyTime) / 60)
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"{NUM()} users for {runTime} minutes"))
        await sleep(20)

# CANNOT HAVE MULTIPLE ON_READY()

# FIXME
@bot.event # detect status change
async def on_member_update(before, after):
    if ((str(after.status) == "online") and (str(before.status) != "online")):
        print('any status -> online')
    
    elif ((str(after.status) == "offline") and (str(before.status) != "offline")):
        print('any status -> offline')



" Bot Commands: "

@bot.command()
async def test(ctx):
    await ctx.send("Hello World!")



" On Disconnect: "

@bot.event
async def on_disconnect():
    testServer = DD_test()
    await testServer.send("Exited!")

" DEBUG: "

@bot.command() # check everyone bot can see
async def check_all_online(ctx):

    for i in bot.users:
        print(i.id)

" Do something with genshin "

@bot.command()
async def genshinID(ctx, user):
    userGenID = user
    await ctx.send(userGenID)

@bot.command()
async def genRank(ctx):
    rankedList = 2 # dictionaries w/ id and level
    sortedList = []
    for i in rankedList:
        sortedList.append(i)
        print("Sort function here based on dictionary attributes")
        #does git detect comments?
    await ctx.send(sortedList)










# Secret Super Client Code
# In external py file :)... replace with your own discord bot key on the discord developer portal

bot.run(key.botKey)
client.run(key.botKey)