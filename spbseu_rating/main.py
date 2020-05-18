import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
from rating import *

token = ""

client = discord.Client()
bot = commands.Bot(command_prefix = "biba!")

@bot.command(name='brs', help='Показывает баллы БРС указанного человека, предмета или вообще все сразу')
async def brs(ctx, name):
    if name in inverse_participants_nicknames:
        response = one_student_stats(name)
    elif name in subjects_short or name in subjects_full:
        response = one_subject_stats(name)
    elif name == 'фул':
        response = all_stats()
    else:
        response = 'Сори не понел'
    await ctx.send(response)

@bot.command(name='show', help='Показывает предметы или участников')
async def show(ctx, param):
    if param == 'участники':
        response = show_participants()
    elif param == 'предметы':
        response = show_subjects()
    else:
        response = 'Сори не понел'
    await ctx.send(response)

#след две команды почему-то не робят и вообще бот не запускается теперь лол
@bot.command(name='pidor', help='Указывает на пидора')
async def pidor(ctx):
    await ctx.send(random.choice(participants))

@bot.command(name='ping', help='Возвращает пинг')
async def ping(ctx):
    await ctx.send(f'Пинг: {round(client.latency * 1000)}ms')

bot.run(token)
