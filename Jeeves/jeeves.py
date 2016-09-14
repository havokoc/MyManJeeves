import discord
import asyncio
import random
import configparser
import json

def RunBot(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('------')
        print('Logged in as %s (%s)' % (client.user.name, client.user.id))
        print('------')

    @client.event
    async def on_message(message):
        if message.channel.id == "123410749765713920":
            if message.content.startswith('-knugen'):
                
                await client.send_message(message.channel, random.choice(knugenLinks))

    client.run(config['Bot']['token'])

if __name__ == "__main__":
    print("Please use the start.py script in the root directory instead")
