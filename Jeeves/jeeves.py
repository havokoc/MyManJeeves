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
        if message.channel.id == "123410749765713920" or "139430532437114880":
            #Command - Knugen
            if message.content.startswith('%sknugen' % config['Bot']['prefix']):
                with open('config/data.json') as data_file:
                    data = json.loads(data_file.read())
                    #await client.send_message(message.channel, random.choice(data['knugenLinks']))
                    embed = discord.Embed(title='Välfärden is here again!', colour=0xEDC922)
                    embed.set_image(url=random.choice(data['knugenLinks']))
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("knugen", message.author.name))
            #Command - Avatar
            if message.content.startswith('%savatar' % config['Bot']['prefix']):
                if len(message.content.split()) < 2:
                    embed = discord.Embed(title='%s\'s avatar' % message.author.name, colour=0xEDC922)
                    #embed.set_image(url='https://cdn.discordapp.com/avatars/'+message.author.id+'/'+message.author.avatar+'.gif')
                    embed.set_image(url=message.author.avatar_url)
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("avatar", message.author.name))
                else:
                    embed = discord.Embed(title='%s\'s avatar' % message.mentions[0].name, colour=0xEDC922)
                    #embed.set_image(url='https://cdn.discordapp.com/avatars/'+message.mentions[0].id+'/'+message.mentions[0].avatar+'.gif')
                    embed.set_image(url=message.mentions[0].avatar_url)
                    await client.send_message(message.channel, embed=embed)
                    print(loggingFunc("avatar", message.author.name))
            if message.content.startswith('%shonk' % config['Bot']['prefix']):
                if message.author.voice.voice_channel == None:
                    await client.send_message(message.channel, "You are not in a voice channel.")
                else:
                    voice = await client.join_voice_channel(message.author.voice.voice_channel)
                    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=4Iut-7RzwkQ')
                    player.start()
                    player.stop()
                    voice.disconnect()
            #Command - X

    client.run(config['Bot']['token'])

if __name__ == "__main__":
    print("Please use the start.py script in the root directory instead")
