from discord import *
from func import *
from discord.ext import commands
from asyncio import sleep
import atexit
from SECRET import shh

"""
Notes:

STZ Ideas:

    Wordle leaderboard

    BE REAL (aka Bea's app thing)
        -Have role

ACTUAL FIXING STUFF:
    
    should probably make hashmaps and other user data storage based around userid rather than name :l
    
    ur time recording is wrong... init time is being saved onto user


"""

print('running')

# Client
intents = Intents.default()
intents.members = True
intents.presences = True
client = Client(intents = intents)
bot = commands.Bot(command_prefix = '!', intents = intents)

# Specific Channels

DD_Test = bot.get_channel(979493252015206441)


# VARIABLES

# BOT COMMANDS

@bot.command()
async def test(ctx):
    await ctx.send("Hello World!")
    done()

@bot.command()
async def list(ctx):

    guild = ctx.guild

    await ctx.send('List of all members in {}'.format(guild.name))

    for i in range(guild.member_count):
        status = (guild.members[i]).status
        await ctx.send('{} is {}'.format(guild.members[i], status))

@bot.command()
async def status(ctx, status):
    print("it worked")
    await bot.change_presence(activity = Activity(type = ActivityType.watching, name = status))

@bot.command()
async def watch(ctx, status):

    guild = ctx.guild

    if status == "online":
        for i in range(guild.member_count):
            while True:
                await sleep(20)
                if (str(guild.members[i].status) == "online"):
                    await ctx.send("Watching {}".format(guild.members[i]))
                    observe(str(guild.members[i]))

    elif status == "offline":
        for i in range(guild.member_count):

            if (str(guild.members[i].status) == "offline"):
                await ctx.send("Watching {}".format(guild.members[i]))
                observe(str(guild.members[i]))

    elif status == "dnd":
        for i in range(guild.member_count):

            if (str(guild.members[i].status) == "dnd"):
                await ctx.send("Watching {}".format(guild.members[i]))
                observe(str(guild.members[i]))

    else:
        await ctx.send("Invalid argument dumbass")

@bot.command()
async def pickled(ctx):
   await ctx.send(str((users)))

@bot.command()
async def data(ctx):
    
    for key in users:
        await ctx.send(checkUser(users[key]))

# DEBUG COMMANDS

@bot.command()
async def userYeet(ctx):
    print(userNum)

@bot.command()
async def save():
    saveData()

@bot.command()
async def yeet(ctx, input):
    print(input)
    print(type(input))
    await ctx.send(f"Boiii this bih issa {type(input)}")
    await ctx.send(input)

@bot.command()
async def stalk(ctx, input):
    input = input.replace("@", "")
    input = input.replace("<", "")
    input = input.replace(">", "")
    name = (ctx.guild.get_member(int(input))).name
    await ctx.send(checkUser(users[name]))

# bot events:

@bot.event
async def on_member_update(before, after):

    if ((str(after.status) == "online") and (str(before.status) != "online")):

        observe(after.name)
        temp = users[after.name]

        if (temp.loaded == False):

            temp.loaded = True

            print(before.guild.name)
            DD_Test = bot.get_channel(979493252015206441)
            await DD_Test.send(f"{after.name} has gone {after.status}.")

    elif ((str(after.status) == "offline") and (str(before.status) != "offline")):

        temp = users[after.name]

        if (temp.loaded == True):
            stopObserve(after.name)
            print(before.guild.name)
            DD_Test = bot.get_channel(979493252015206441)
            await DD_Test.send(f"{after.name} has gone {after.status}.")

@bot.event
async def on_ready():

    DD_Test = bot.get_channel(979493252015206441)
    init_online = 0
    guildNum = 0
    print("Now we're cooking")

    # Init Message
    now = datetime.now()
    dt_string = now.strftime(f"%d/%m/%Y %H:%M:%S")
    await DD_Test.send(f"\n \n ** Run time: {dt_string} * \n \n")

    readyTime = monotonic()

    # Auto watch everyone online:

    for guild in bot.guilds:
        guildNum += 1
        for member in guild.members:
            if (str(member.status) == "online"):
                    observe(str(member))
                    init_online += 1

    await DD_Test.send(f"Successfully watching {init_online} members in {guildNum} guilds")

    while True:
        await sleep(20)
        presentTime = monotonic() - readyTime
        mins = presentTime / 60
        runTime = int(mins)
        print("yes")
        await bot.change_presence(activity = Activity(type = ActivityType.watching, name = f"{NUM()} users for {runTime} minutes"))
        saveData()

# save when code is terminated

@bot.event
async def on_disconnect():
    await DD_Test.send("Exited!")

@bot.event
async def on_ready():
    atexit.register(done)



    
          






# Commands:


"""
bot that tracks how long people are online for on discord and send info from commands
"""

#TRACK PEOPLE

#test


# Run the client on the server
# botKey located on private folder... replace with your own discord bot from discord developer portal
client.run(shh.botKey)
bot.run(shh.botKey)