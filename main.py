from bot_exceptions import *
from bot_utils import *
from parser import *
from traceback import format_exc
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '972310320:AAFPLWK_5lOiNfanIQjGFgD20RM2dK98Mos'

updater = Updater(token=TOKEN, use_context=True)
worker = updater.job_queue
dispatcher = updater.dispatcher

try:
    feeds = read_feeds_from_file('feeds')
    keywords = read_keywords_from_file('keywords')
    chat_id = load_chat_id('chat_id')
except:
    add_to_log('log', format_exc())

def start(update, context):
    save_chat_id('chat_id', update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Добрый день.
Список команд:
/sub [ссылка] [название ленты] [-s] -- подписаться на источник, используйте -s, если хотите получать текст новости
/unsub [название ленты] -- отписаться от ленты
/addkeywords [слово] [слово] [слово] -- добавить ключевые слова
/deletekeyword [слово] [слово] [слово] -- удалить ключевые слова
/subs -- показать подписки
/keywords -- показать ключевые слова""")

def sub(update, context):
    try:
        global feeds
        message = context.args
        feed_link = message[0]
        feed_name = message[1]
        if message[-1] == '-s':
            feed_summary = True
        else:
            feed_summary = False
        test_feed = feedparser.parse(feed_link)
        feed_date = test_feed.entries[0].published
        if feed_name not in feeds.keys():
            if feed_link not in feeds.values():
                if '::' not in feed_name and '::' not in feed_link:
                    feeds[feed_name] = {'link':feed_link, 'date':feed_date, 'summary':feed_summary}
                    add_feed_to_file('feeds', feed_name, feed_link, feed_date, feed_summary)
                    context.bot.send_message(chat_id=update.effective_chat.id, \
                    text="Вы подписались на источник " + "'" + feed_name + "'")
                else:
                    raise RestrictedSymbols
            else:
                raise RepeatedFeedLink
        else:
            raise RepeatedFeedName
    except RepeatedFeedName:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Такое имя ленты уже существует')
    except RepeatedFeedLink:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Такая лента уже существует')
    except RestrictedSymbols:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Пожалуйста, не используйте :: в названии ленты или ссылке на ленту")
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, проверьте корректность данных и попробуйте еще раз")
        add_to_log('log', format_exc())

def addkeywords(update, context):
    try:
        global keywords
        message = context.args
        new_keywords = list(set(message))
        added = []
        for word in new_keywords:
            if word not in keywords:
                keywords.append(word)
                added.append(word)
        add_keywords_to_file('keywords', added)
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Добавлены ключевые слова: " +', '.join(new_keywords))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def unsub(update, context):
    try:
        global feeds
        message = context.args
        sources = list(set(message))
        not_deleted = []
        deleted = []
        for source in sources:
            if source in feeds.keys():
                del feeds[source]
                deleted.append(source)
            else:
                not_deleted.append(source)
        bump_feeds_to_file('feeds', feeds)
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Вы отписались от следующих источников: " + \
        ', '.join(deleted) + '\n')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def deletekeywords(update, context):
    try:
        global keywords
        message = context.args
        words = list(set(message))
        not_deleted = []
        deleted = []
        for word in words:
            if word in keywords:
                keywords.remove(word)
                deleted.append(word)
            else:
                not_deleted.append(word)
        bump_keywords_to_file('keywords', keywords)
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Удалены ключевые слова: " + ', '.join(deleted) + '\n')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def showsubs(update, context):
    try:
        global feeds
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Подписки: ' + ', '.join([name for name in feeds.keys()]))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def showkeywords(update, context):
    try:
        global feeds
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Ключевые слова: ' + ', '.join(keywords))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def helpme(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, \
    text="Кстати, я Пудж")

def check_for_updates(context):
    try:
        global feeds
        global chat_id
        news = []
        for feed in feeds.values():
            entries = feedparser.parse(feed['link']).entries
            #раcкомментировать, когда надоест тестить
            #feed['date'] = entries[0].published
            n = 0
            article = entries[n]
            while article.published != feed['date'] and n != len(entries):
                text = ''
                if feed['summary']:
                    text = get_description(article)+'\n'
                context.bot.send_message(chat_id=chat_id, \
                text='<b>'+article.title+'</b>'+'\n'+text+article.link,\
                parse_mode='HTML')
                n += 1
                article = entries[n]
        bump_feeds_to_file('feeds', feeds)
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Ой...")
        add_to_log('log', format_exc())

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', start)
sub_handler = CommandHandler('sub', sub)
unsub_handler = CommandHandler('unsub', unsub)
addkeywords_handler = CommandHandler('addkeywords', addkeywords)
deletekeyword_handler = CommandHandler('deletekeywords', deletekeywords)
showsubs_handler = CommandHandler('subs', showsubs)
showkeywords_handler = CommandHandler('keywords', showkeywords)
unknown_handler = MessageHandler(Filters.all, helpme)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(unsub_handler)
dispatcher.add_handler(addkeywords_handler)
dispatcher.add_handler(deletekeyword_handler)
dispatcher.add_handler(showsubs_handler)
dispatcher.add_handler(showkeywords_handler)
dispatcher.add_handler(unknown_handler)

worker.run_repeating(check_for_updates, interval=20, first=0, context=chat_id)

updater.start_polling()
updater.idle()
