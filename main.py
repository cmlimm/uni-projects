import telebot
import feedparser
from bot_exceptions import *
from telebot import types

TOKEN = '972310320:AAFPLWK_5lOiNfanIQjGFgD20RM2dK98Mos'

bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=1)
add_feed_button = types.KeyboardButton('Новая лента')
add_keyword_button = types.KeyboardButton('Новое ключевое слово')
delete_feed_button = types.KeyboardButton('Удалить ленту')
delete_keyword_button = types.KeyboardButton('Удалить ключевое слово')
markup.add(add_feed_button, add_keyword_button, delete_feed_button, \
            delete_feed_button)

try:
    feeds = read_feeds_from_file('feeds')
except:
    bot.send_message(message.chat.id, """Проблемы с чтением списка лент из файла,
    обратитесь к разработчику""")

try:
    keywords = read_keywords_from_file('keywords')
except:
    bot.send_message(message.chat.id, """Проблемы с чтением списка ключевых слов
    из файла, обратитесь к разработчику""")

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    bot.reply_to(message, """Добрый день.\n
    Я могу: \n
    - Присылать новости из RSS-лент, которые мне укажут \n
    - Отбирать новости по ключевым словам \n
    Для добавления новости или ключевого слова нажмите соответствующую кнопку""")

@bot.message_handler(regexp='Новая лента')
def add_feed(message):
    bot.send_message(message.chat.id, """Введите ссылку на ленту и
    её короткое название в следующем формате:\n
    [ссылка] [короткое название]""")
    waiting_for_feed = True

@bot.message_handler(regexp='.+\.\S+ .+')
def new_source(message):
    try:
        feed_link = message.text.split()[0]
        feed_name = message.text.split()[1]
        if waiting_for_feed:
            try:
                test_feed = feedparser.parse(feed_link)
                feeds[feed_name] = test_feed
                if feed_name not in feeds.keys():
                    if feed_link not in feeds.values():
                        if '::' not in feed_name and '::' not in feed_link:
                            feeds[feed_name] = feed_link
                            add_feed_to_file('feeds', feed_name, feed_link)
                            bot.send_message(message.chat.id, """Вы добавили новую ленту под
                            названием """ + "'" + feed_name + "'")
                            waiting_for_feed = False
                        else:
                            raise RestrictedSymbols
                    else:
                        raise RepeatedFeedLink
                else:
                    raise RepeatedFeedName
        else:
            raise NotWaitingForFeed
    except NotWaitingForFeed:
        bot.send_message(message.chat.id, """Пожалуйста,
        воспользуйтесь функцией 'Новая лента' и попробуйте еще раз""")
    except RepeatedFeedName:
        bot.send_message(message.chat.id, 'Такое имя ленты уже существует')
    except RepeatedFeedLink:
        bot.send_message(message.chat.id, 'Такая лента уже существует')
    except RestrictedSymbols:
        bot.send_message(message.chat.id, """Пожалуйста, не используйте :: в
        названии ленты или ссылке на ленту""")
    except:
        bot.send_message(message.chat.id, """Что-то пошло не так,
        пожалуйста, проверьте корректность данных и попробуйте еще раз""")

@bot.message_handler(regexp='Новое ключевое слово')
def add_keywords(message):
    bot.send_message(message.chat.id, """Введите новое ключевое слово
    или слова в следующем формате:\n
    Добавить [слово] [слово] ... [слово]""")
    waiting_for_keywords = True

@bot.message_handler(regexp='Добавить \w+( \w+)*$')
def new_keywords(message):
    try:
        new_keywords = list(set(message.text.split()[1:])
        if waiting_for_keywords:
                add_keywords_to_file('keywords', new_keywords)
                bot.send_message(message.chat.id, """Успешно добавлены следующие
                ключевые слова: """+', '.join(new_keywords))
        else:
            raise NotWaitingForKeywords
    except NotWaitingForKeywords:
        bot.send_message(message.chat.id, """Пожалуйста,
        воспользуйтесь функцией 'Новое ключевое слово' и попробуйте еще раз""")
    except:
        bot.send_message(message.chat.id, """Что-то пошло не так, попробуйте
        еще раз""")

@bot.message_handler(regexp='Удалить ленту')
def delete_feed(message):
    bot.send_message(message.chat.id, """Введите названия лент, от которых
    хотите отписаться, в следующем формате:\n
    Удалить ленты [название] [название] ... [название]""")
    waiting_for_to_be_deleted_feeds = True

@bot.message_handler(regexp='(У|у)далить лент(ы|у) \w+( \w+)*$')
def delete_old_sources(message):
    try:
        sources = list(set(message.text.split()[2:]))
        not_deleted = []
        deleted = []
        if waiting_for_to_be_deleted_feeds:
                for source in sources:
                    if source in feeds.keys():
                        del keys[source]
                        deleted.append(source)
                    else:
                        not_deleted.append(source)
                bump_feeds_to_file('feeds', feeds)
                bot.send_message(message.chat.id, """Успешно удалены следующие
                ленты: """ + ', '.join(deleted)+'\n'+"""Не удалось удалить
                следующие ленты по причине их отсутствия: """ + ', '.join(not_deleted))
                waiting_for_to_be_deleted_feeds = False
        else:
            raise NotWaitingForToBeDeletedFeeds
    except NotWaitingForToBeDeletedFeeds:
        bot.send_message(message.chat.id, """Пожалуйста,
        воспользуйтесь функцией 'Удалить ленту' и попробуйте еще раз""")
    except:
        bot.send_message(message.chat.id, """Что-то пошло не так, попробуйте
        еще раз""")

@bot.message_handler(regexp='Удалить ключевое слово')
def delete_keywords(message):
    bot.send_message(message.chat.id, """Введите названия ключевых слов, которые
    хотите удалить, в следующем формате:\n
    Удалить слова [слово] [слово] ... [слово]""")
    waiting_for_to_be_deleted_keywords = True

@bot.message_handler(regexp='(У|у)далить слов(а|о) \w+( \w+)*$')
def delete_old_keywords(message):
    try:
        words = list(set(message.text.split()[2:]))
        not_deleted = []
        deleted = []
        if waiting_for_to_be_deleted_keywords:
                for word in words:
                    if word in keywords:
                        keywords.remove(word)
                        deleted.append(word)
                    else:
                        not_deleted.append(word)
                bump_keywords_to_file('keywords', keywords)
                bot.send_message(message.chat.id, """Успешно удалены следующие
                слова: """ + ', '.join(deleted)+'\n'+"""Не удалось удалить
                следующие слова по причине их отсутствия: """ + ', '.join(not_deleted))
                waiting_for_to_be_deleted_keywords = False
        else:
            raise NotWaitingForToBeDeletedKeywords
    except NotWaitingForToBeDeletedKeywords:
        bot.send_message(message.chat.id, """Пожалуйста,
        воспользуйтесь функцией 'Удалить ключевое слово' и попробуйте еще раз""")
    except:
        bot.send_message(message.chat.id, """Что-то пошло не так, попробуйте
        еще раз""")

bot.polling()

while True:
    pass
