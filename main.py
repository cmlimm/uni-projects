import requests
import bs4
import re
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

'''
Определяем баллы и меряем бибу
'''

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

'''
Пишем бота
'''

token = ""

'''client = discord.Client()



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

    if message.content.startswith("!brs Саня"):
        await message.channel.send(one_student_stats('Саня'))
    if message.content.startswith("!brs Катя"):
        await message.channel.send(one_student_stats('Катя'))
    if message.content.startswith("!brs Кирюша"):
        await message.channel.send(one_student_stats('Кирюша'))
    if message.content.startswith("!brs Владик"):
        await message.channel.send(one_student_stats('Владик'))
    if message.content.startswith("!brs Максибон"):
        await message.channel.send(one_student_stats('Максибон'))
    if message.content.startswith("!brs Даня"):
        await message.channel.send(one_student_stats('Даня'))
    if message.content.startswith("!brs Кирилл"):
        await message.channel.send(one_student_stats('Кирилл'))
    if message.content.startswith("!brs Сергей"):
        await message.channel.send(one_student_stats('Сергей'))
    if message.content.startswith("!biba"):
        await message.channel.send("")
    if message.content.startswith("!ping"):
        await message.channel.send(f"Your ping ping is {round(client.latency * 1000)}ms")'''


bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def age(ctx):
    await ctx.send(random.randint(5,80))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Your ping ping is {round(client.latency * 1000)}ms")

@bot.command()
async def whoispidor(ctx):
    list1 = ['Владик','Кирюша','Саня','Катя','Максибон','Даня','Сергей']
    await ctx.send(random.choice(list1))


bot.run(token)
