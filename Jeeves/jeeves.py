#Imports - Laddar API:n och moduler som gör development enklare
import discord
import asyncio
import random
import configparser
import json
import logging
from datetime import datetime
#HOJJ

#Loggingclassen som ska användas för resen av alla commands
class loggingFunc(object):
    def __init__(self, command, user):
        self.command = command
        self.user = user
    def __str__(self):
        return '[%s] %s ran a command (%s)' % (datetime.now().time(), self.user, self.command)

def RunBot(config_file):
    #Laddar config
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
            #Command - Knugen
            if message.content.startswith('%sknugen' % config['Bot']['prefix']):
                with open('config/data.json') as data_file:
                    data = json.loads(data_file.read())
                    await client.send_message(message.channel, random.choice(data['knugenLinks']))
                    print(loggingFunc("knugen", message.author.name))

            if message.content.startswith('%savatar' % config['Bot']['prefix']):
                await client.send_message(message.channel, message.author.avatar_url)
                print(loggingFunc("avatar", message.author.name))

    client.run(config['Bot']['token'])

if __name__ == "__main__":
    print("Please use the start.py script in the root directory instead")
