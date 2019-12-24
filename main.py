import requests
import bs4
import re
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
from chlen import *

url = 'http://www.rating.unecon.ru/index.php?&y=2018&f=1&up=12020&s=3&g=all&upp=all&ball=hide&sort=fio'
brs_HTML = requests.get(url)
brs_Soup = bs4.BeautifulSoup(brs_HTML.text)

clear_HTML_re = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def clear_HTML(text):
    return re.sub(clear_HTML_re, '', text)

subjects_short = brs_Soup.find('div', {'class': 'page_info'}).find_all('b')
subjects_short = [subject.text.strip('</b>') for subject in subjects_short]
subjects_full = brs_Soup.find('div', {'class': 'page_info'}).find_all('li')
subjects_full = [re.findall("</b> - (.*?)</li>", str(subject))[0] for subject in subjects_full]
subjects = dict(zip(subjects_short, subjects_full))

students = brs_Soup.find('tbody').find_all('tr')
students = {clear_HTML(student.find('a').text): [int(clear_HTML(score.text)) if clear_HTML(score.text) else 0 for score in student.find_all('td', {'class': 'w50 no_mobile'})] for student in students if student.find('a')}

participants = [
    'Ерофеевский Александр Сергеевич',
    'Захаров Кирилл Александрович',
    'Зотов Максим Дмитриевич',
    'Мотылева Екатерина Дмитриевна',
    'Соболев Даниил Дмитриевич',
    'Спирин Владислав Сергеевич',
    'Толдов Кирилл Алексеевич',
    'Шульняев Сергей Андреевич'
]
participants_scores = {student: students[student] for student in students if student in participants}
participants_nicknames = {
    'Ерофеевский Александр Сергеевич': 'Саня',
    'Захаров Кирилл Александрович': 'Кирюша',
    'Зотов Максим Дмитриевич': 'Максибон',
    'Мотылева Екатерина Дмитриевна': 'Катя',
    'Соболев Даниил Дмитриевич': 'Даня',
    'Спирин Владислав Сергеевич': 'Владик',
    'Толдов Кирилл Алексеевич': 'Кирилл',
    'Шульняев Сергей Андреевич': 'Сергей'
}
inverse_participants_nicknames = {short: full for full, short in participants_nicknames.items()}

def one_subject_stats(name):
    index = subjects_short.index(name)
    text = subjects[name] + '\n'
    for participant in participants_scores:
        text += participants_nicknames[participant] + ': ' + str(participants_scores[participant][index]) + '\n'
    return(text[:-1])

def all_stats():
    text = 'Статистика по БРС' + '\n\n'
    for subject in subjects_short:
            text += one_subject_stats(subject) + '\n\n'
    return text[:-2]

def one_student_stats(name):
    full_name = inverse_participants_nicknames[name]
    text = name + '\n'
    for i in range(len(participants_scores[full_name])):
        text += subjects[subjects_short[i]] + ': ' + str(participants_scores[full_name][i]) + '\n'
    return text[:-1]

def show_subjects():
    text = 'Предметы:\n'
    for subject in subjects:
        text += subject + ': ' + subjects[subject] + '\n'
    return text[:-1]

def show_participants():
    text = 'Участники:\n'
    for member in inverse_participants_nicknames:
        text += member + ': ' + inverse_participants_nicknames[member] + '\n'
    return text[:-1]

'''
Пишем бота
'''

token = ""

client = discord.Client()
bot = commands.Bot(command_prefix = "!")

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
    elif param == 'хуй':
        response = chlen_ascii
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
