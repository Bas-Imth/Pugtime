#This is what happens when I am bored and I have some spare time.
#Send help.
import datetime
import time
import platform
import discord
from discord.ext import commands


wanted_day = 'saturday'
wanted_time = 19
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Discord ready to count!.")
    print("Discord.py version %s | Python version %s" % (discord.__version__, platform.python_version()))
    print("------------------------------")
    print("Bot name: %s" % bot.user.name)
    print("Bot ID: %s" % bot.user.name)
    print("The Bot is in %d servers." % len(bot.servers))
    print("A collective ammount of %d users are in the servers." % len(set(())))
    print("------------------------------")
    await bot.change_presence(game=discord.Game(name='Counting...'))

@bot.command(pass_context=True)
async def pugtime(ctx):
    lst = [['monday', 0],['tuesday', 1],['wednesday', 2],['thursday', 3],['friday', 4],['saturday', 5],['sunday', 6]]
    for i in lst:
        if wanted_day == i[0]:
            number_wanted_day = i[1]
            today = datetime.datetime.today().weekday()
            days = number_wanted_day - today
            timed = time.localtime(time.time()+ time.timezone)
            if wanted_time > timed[3]:
                hours = wanted_time - timed[3] - 1
                mins = 59 - timed[4]
                secs = 59 - timed[5]
                return await bot.say("%d day(s), %d hour(s), %d minute(s) and %d second(s) left untill the next PUG!" % (days, hours, mins, secs))
                #return await bot.say( [days, 'day(s)', hours,'hour(s)', mins,'minute(s) and', secs,'seconds untill the Saturday PUG!']) - Old format

            else:
                days = days
                hours = 23 - timed[3] + wanted_time #- 1 #Not sure if one hour off or not.
                mins = 59 - timed[4]
                secs = 59 - timed[5]
                return await bot.say("%d day(s), %d hour(s), %d minute(s) and %d second(s) left untill the next PUG!" % (days, hours, mins, secs))
@bot.command(pass_context=True)
async def ping(ctx):
    return await bot.say("No! \n I refuse to play this stupid game!")


@bot.event
async def on_message(msg):

    if msg.author.bot:
        print("I don't listen to bots.")
        return

    await bot.process_commands(msg)


bot.run("<Token>")
