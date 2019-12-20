import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

token = "NjU3NjY1MTcyNzA5NTcyNjQ4.Xf0geQ.7y3Wx8vbVpHESgQijGKEt_zZOe4"
Bot = commands.Bot(command_prefix = "!")

client = discord.Client()

list1 = ['Vladik','Kirill','Sasha','Katya','Maxim']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("!whoispidor"):
        await message.channel.send(random.choice(list1))
#@Bot.command
#async def foo(ctx):
#    await ctx.send('Hello')
client.run(token)
