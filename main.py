import telebot
from parser import *
from bot_exceptions import *
from bot_utils import *
from telebot import types
from traceback import format_exc
import time

TOKEN = '972310320:AAFPLWK_5lOiNfanIQjGFgD20RM2dK98Mos'

bot = telebot.TeleBot(TOKEN)

try:
    feeds = read_feeds_from_file('feeds')
    keywords = read_keywords_from_file('keywords')
    chat_id = load_chat_id('chat_id')
except:
    add_to_log('log', format_exc())

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    save_chat_id('chat_id', message.chat.id)
    bot.reply_to(message, """Добрый день.
Я могу:
- Присылать новости из RSS-лент, которые мне укажут
- Отбирать новости по ключевым словам
Список команд:
/sub [ссылка] [название ленты] -- подписаться на источник
/unsub [название ленты] -- отписаться от ленты
/addkeywords [слово] [слово] [слово] -- добавить ключевые слова
/deletekeyword [слово] [слово] [слово] -- удалить ключевые слова
/subs -- показать подписки
/keywords -- показать ключевые слова""")

@bot.message_handler(commands=['sub'])
@bot.message_handler(regexp='/sub .+\.\S+ .+')
def sub(message):
    try:
        global feeds
        feed_link = message.text.split()[1]
        feed_name = message.text.split()[2]
        test_feed = feedparser.parse(feed_link)
        feed_date = test_feed.entries[0].published
        if feed_name not in feeds.keys():
            if feed_link not in feeds.values():
                if '::' not in feed_name and '::' not in feed_link:
                    feeds[feed_name] = {'link':feed_link, 'date':feed_date}
                    add_feed_to_file('feeds', feed_name, feed_link, feed_date)
                    bot.send_message(message.chat.id, "Вы подписались на источник " + "'" + feed_name + "'")
                else:
                    raise RestrictedSymbols
            else:
                raise RepeatedFeedLink
        else:
            raise RepeatedFeedName
    except RepeatedFeedName:
        bot.send_message(message.chat.id, 'Такое имя ленты уже существует')
    except RepeatedFeedLink:
        bot.send_message(message.chat.id, 'Такая лента уже существует')
    except RestrictedSymbols:
        bot.send_message(message.chat.id, "Пожалуйста, не используйте :: в названии ленты или ссылке на ленту")
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, проверьте корректность данных и попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(commands=['addkeyword'])
@bot.message_handler(regexp='/addkeyword \w+( \w+)*$')
def new_keywords(message):
    try:
        global keywords
        new_keywords = list(set(message.text.split()[1:]))
        added = []
        for word in new_keywords:
            if word not in keywords:
                keywords.append(word)
                added.append(word)
        add_keywords_to_file('keywords', added)
        bot.send_message(message.chat.id, "Добавлены ключевые слова: " +', '.join(new_keywords))
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(commands=['unsub'])
@bot.message_handler(regexp='/unsub \w+( \w+)*$')
def unsub(message):
    try:
        global feeds
        sources = list(set(message.text.split()[1:]))
        not_deleted = []
        deleted = []
        for source in sources:
            if source in feeds.keys():
                del feeds[source]
                deleted.append(source)
            else:
                not_deleted.append(source)
        bump_feeds_to_file('feeds', feeds)
        bot.send_message(message.chat.id, "Вы отписались от следующих источников: " + \
        ', '.join(deleted) + '\n')
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(commands=['deletekeyword'])
@bot.message_handler(regexp='/deletekeyword \w+( \w+)*$')
def delete_keywords(message):
    try:
        global keywords
        words = list(set(message.text.split()[1:]))
        not_deleted = []
        deleted = []
        for word in words:
            if word in keywords:
                keywords.remove(word)
                deleted.append(word)
            else:
                not_deleted.append(word)
        bump_keywords_to_file('keywords', keywords)
        bot.send_message(message.chat.id, "Удалены ключевые слова: " + \
        ', '.join(deleted) + '\n')
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(commands=['subs'])
def show_subs(message):
    try:
        global feeds
        bot.send_message(message.chat.id, 'Подписки: ' + \
        ', '.join([name for name in feeds.keys()]))
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(commands=['keywords'])
def show_keywords(message):
    try:
        global feeds
        bot.send_message(message.chat.id, 'Ключевые слова: ' + \
        ', '.join(keywords))
    except Exception as ex:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

@bot.message_handler(func=lambda message: True)
def delete_old_keywords(message):
    bot.send_message(message.chat.id, "Кстати, я Пудж")

def check_for_updates():
    global feeds
    news = []
    for feed in feeds.values():
        entries = feedparser.parse(feed['link']).entries
        #feed['date'] = entries[0].published
        n = 0
        new = entries[n]
        while new.published != feed['date']:
            news.append({'title': new.title, 'link':new.link})
            bot.send_message(chat_id, new.title+'\n'+new.link+'\n\n')
            n += 1
            new = entries[n]
    time.sleep(10)
    check_for_updates()

check_for_updates()

bot.polling()
