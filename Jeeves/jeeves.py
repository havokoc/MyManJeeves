import discord
import asyncio
import random
import configparser

def RunBot():
    description = '''TODO: -list(Minecraft), -hojj(STENBERG), -help/My Man..., -INSERTMORECOMMANDSHERE'''
    config = configparser.ConfigParser()
    config.read('config.ini')

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
                knugenLinks = [
                "http://i.imgur.com/dG0q4a9.png",
                "http://i.imgur.com/pCtYLDP.jpg",
                "http://i.imgur.com/QnvhnT8.jpg",
                "http://i.imgur.com/rjxCi4a.jpg",
                "http://i.imgur.com/mpSoTfk.png",
                "http://i.imgur.com/Jy3g2Q6.jpg",
                "http://i.imgur.com/bpwp3rb.jpg",
                "http://i.imgur.com/Y0ylzT5.jpg",
                "http://i.imgur.com/AlC76nS.png",
                "http://i.imgur.com/fkAAgh1.gifv",
                "https://i.imgur.com/qdzHLJA.jpg",
                ]
                await client.send_message(message.channel, random.choice(knugenLinks))

    client.run(config['Bot']['token'])

if __name__ == "__main__":
    RunBot()
