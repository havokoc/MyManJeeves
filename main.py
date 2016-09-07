import discord
from discord.ext import commands
import random
import configparser

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
config = configparser.ConfigParser()
config.read('config.ini')
bot = commands.Bot(command_prefix=config['Bot']['prefix'], description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')
	
@bot.command(description='For when you wanna knugen')
async def knugen():
    """Chooses between multiple choices."""
    knugenLinks = [
	"http://i.imgur.com/dG0q4a9.png",
    "http://i.imgur.com/pCtYLDP.jpg",
    "http://i.imgur.com/QnvhnT8.jpg",
    "http://i.imgur.com/rjxCi4a.jpg",
    "http://i.imgur.com/mpSoTfk.png",
    "http://i.imgur.com/Jy3g2Q6.jpg",
    "http://i.imgur.com/bpwp3rb.jpg",
    "http://i.imgur.com/Y0ylzT5.jpg",
	"http://i.imgur.com/AlC76nS.png"
    ]
    await bot.say(random.choice(knugenLinks))

bot.run(config['Bot']['token'])