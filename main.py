from bot_utils import *
from parser import *
from config import *
from traceback import format_exc
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token=TOKEN, use_context=True)
worker = updater.job_queue
dispatcher = updater.dispatcher

try:
    feeds = read_feeds('feeds')
    keywords = read_keywords('keywords')
except:
    add_to_log('log', format_exc())

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Добрый день.
Список команд:
/sub [ссылка] [название источника] [-s] -- подписаться на источник, используйте -s, если хотите получать текст новости
/unsub [название источника] -- отписаться от ленты
/addkeywords [источник] [слово] [слово] [слово] -- добавить ключевые слова к источнику
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
                    bump_feeds('feeds', feeds)
                    context.bot.send_message(chat_id=update.effective_chat.id, \
                    text='Вы подписались на источник {}'.format(feed_name))
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id, \
                    text="Пожалуйста, не используйте :: в названии источника или ссылке на источник")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, \
                text='Такой источник уже существует')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Такое название источника уже существует')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, проверьте корректность данных и попробуйте еще раз")
        add_to_log('log', format_exc())

def addkeywords(update, context):
    try:
        global keywords
        global feeds
        message = context.args
        feed = message[0]
        new_keywords = list(set(message[1:]))
        if feed in feeds:
            if feed not in keywords:
                keywords[feed] = []
            for word in new_keywords:
                if word not in keywords[feed]:
                    keywords[feed].append(word)
            bump_keywords('keywords', keywords)
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Добавлены ключевые слова к источнику {}: {}'.format(feed, ', '.join(new_keywords)))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Такого источника нет')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def unsub(update, context):
    try:
        global feeds
        message = context.args
        sources = list(set(message))
        deleted = []
        for source in sources:
            if source in feeds.keys():
                del feeds[source]
                deleted.append(source)
        if deleted != []:
            bump_feeds('feeds', feeds)
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Вы отписались от следующих источников: {}'.format(', '.join(deleted)))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Таких источников нет')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def deletekeywords(update, context):
    try:
        global keywords
        global feeds
        message = context.args
        feed = message[0]
        words = list(set(message[1:]))
        deleted = []
        if feed in feeds and feed in keywords:
            for word in words:
                if word in keywords[feed]:
                    keywords[feed].remove(word)
                    deleted.append(word)
            if deleted != []:
                bump_keywords('keywords', keywords)
                context.bot.send_message(chat_id=update.effective_chat.id, \
                text='Удалены ключевые слова: {}'.format(', '.join(deleted)))
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, \
                text='Таких ключевых слов нет')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Такого источника нет или у такого источника нет ключевых слов')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def showsubs(update, context):
    try:
        global feeds
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Подписки: {}'.format(', '.join(list(feeds.keys()))))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз")
        add_to_log('log', format_exc())

def showkeywords(update, context):
    try:
        global keywords
        show = '\n'.join(['{}: {}'.format(feed, ', '.join(keywords[feed])) for feed in keywords])
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Ключевые слова: \n{}'.format(show))
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
        for source in feeds:
            feed = feeds[source]
            entries = feedparser.parse(feed['link']).entries
            #раcкомментировать, когда надоест тестить
            #feed['date'] = entries[0].published
            n = 0
            article = entries[n]
            while article.published != feed['date'] and n != len(entries):
                text = ''
                if feed['summary']:
                    text = get_description(article, keywords[source])
                context.bot.send_message(chat_id=chat_id, \
                text='<b>{}</b>\n{}{}'.format(article.title, text, article.link),\
                parse_mode='HTML')
                n += 1
                article = entries[n]
        bump_feeds('feeds', feeds)
    except Exception as ex:
        context.bot.send_message(chat_id=chat_id, \
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

#worker.run_repeating(check_for_updates, interval=20, first=0, context=chat_id)

updater.start_polling()
updater.idle()
