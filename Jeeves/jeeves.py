#Imports - Laddar API:n och moduler som gör development enklare
import discord
import asyncio
import random
import configparser
import json
import logging
from datetime import datetime


#Loggingclassen som ska användas för resten av alla commands
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
        if message.channel.id == "123410749765713920" or "139430532437114880":
            '''
            Command - Knugen
            !knugen
            Postar en bild på moderrikets konung i en embed.
            '''
            if message.content.startswith('%sknugen' % config['Bot']['prefix']):
                with open('config/data.json') as data_file:
                    data = json.loads(data_file.read())
                    embed = discord.Embed(title='Välfärden is here again!', colour=0xEDC922)
                    embed.set_image(url=random.choice(data['knugenLinks']))
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("knugen", message.author.name))

            '''
            Command - Avatar
            !avatar <user>
            Outputtar den specifierade användarens avatar. Om användaren inte har
            specifierat någon annan användare, visa användarens avatar i en embed.
            '''
            if message.content.startswith('%savatar' % config['Bot']['prefix']):
                if len(message.content.split()) < 2:
                    embed = discord.Embed(title='%s\'s avatar' % message.author.name, colour=0xEDC922)
                    embed.set_image(url=message.author.avatar_url)
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("avatar", message.author.name))
                else:
                    embed = discord.Embed(title='%s\'s avatar' % message.mentions[0].name, colour=0xEDC922)
                    embed.set_image(url=message.mentions[0].avatar_url)
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("avatar", message.author.name))

    client.run(config['Bot']['token'])

'''
Kräver att man startar med start.py som ligger i huvudmappen, då denna
låter en specifiera en config fil som inte liggar i default mappen.
'''
if __name__ == "__main__":
    print("Please use the start.py script in the root directory instead")
