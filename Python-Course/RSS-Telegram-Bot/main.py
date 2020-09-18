from bot_utils import *
from parser import *
from config import *
from traceback import format_exc
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import feedparser

updater = Updater(token=TOKEN, use_context=True)
worker = updater.job_queue
dispatcher = updater.dispatcher

try:
    feeds = read_feeds('feeds.txt')
    keywords = read_keywords('keywords.txt')
except:
    add_to_log('log.log', format_exc())

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Добрый день.
Список команд:
/sub [ссылка] [название источника] [-s] -- подписаться на источник, используйте -s, если хотите получать текст новости
/unsub [название источника] -- отписаться от ленты
/addkeywords [источник] [слово] [слово] [слово] -- добавить ключевые слова к источнику
/deletekeyword [источник] [слово] [слово] [слово] -- удалить ключевые слова
/subs -- показать подписки
/keywords -- показать ключевые слова

По умолчанию наличие новостей проверяется каждый час
/check -- проверяет новости вне расписания""")

# подписка на новый источник
def sub(update, context):
    try:
        global feeds
        global keywords

        message = context.args
        feed_link = message[0]
        feed_name = message[1]
        if message[-1] == '-s':
            feed_summary = True
        else:
            feed_summary = False

        # проверка валидности ссылки
        test_feed = feedparser.parse(feed_link)
        feed_date = test_feed.entries[0].published

        # если такой ссылки и такого названия еще нет, то добавляем
        if feed_name not in feeds.keys():
            if feed_link not in feeds.values():
                if '::' not in feed_name and '::' not in feed_link:
                    feeds[feed_name] = {'link':feed_link, 'date':feed_date, 'summary':feed_summary}
                    keywords[feed_name] = []
                    bump_feeds('feeds.txt', feeds)
                    bump_keywords('keywords.txt', keywords)
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
        text="Что-то пошло не так, проверьте корректность данных и попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# добавление новый ключевых слов к источникам
def addkeywords(update, context):
    try:
        global keywords
        global feeds
        message = context.args
        feed = message[0]
        new_keywords = list(set(message[1:]))

        # проверка наличия источника
        if feed in feeds:

            # если такого источника нет, то создаем
            if feed not in keywords:
                keywords[feed] = []
            for word in new_keywords:

                # повторяющиеся слова не добавляем
                if word not in keywords[feed]:
                    keywords[feed].append(word)
            bump_keywords('keywords.txt', keywords)
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Добавлены ключевые слова к источнику {}: {}'.format(feed, ', '.join(new_keywords)))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Такого источника нет')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# отписка
def unsub(update, context):
    try:
        global feeds
        global keywords
        message = context.args
        sources = list(set(message))
        deleted = []

        for source in sources:
            if source in feeds.keys():

                # удаление как источника, так и его ключевых слов
                del feeds[source]
                if source in keywords:
                    del keywords[source]
                deleted.append(source)

        if deleted != []:
            bump_feeds('feeds.txt', feeds)
            bump_keywords('keywords.txt', keywords)
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Вы отписались от следующих источников: {}'.format(', '.join(deleted)))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Таких источников нет')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# удаление ключевых слов у источника
def deletekeywords(update, context):
    try:
        global keywords
        global feeds
        message = context.args
        feed = message[0]
        words = list(set(message[1:]))
        deleted = []

        # если есть такой источник и у этого источника есть ключевые слова
        if feed in feeds and feed in keywords:
            for word in words:
                if word in keywords[feed]:
                    keywords[feed].remove(word)
                    deleted.append(word)
            if deleted != []:
                bump_keywords('keywords.txt', keywords)
                context.bot.send_message(chat_id=update.effective_chat.id, \
                text='Удалены ключевые слова в источнике {}: {}'.format(feed, ', '.join(deleted)))
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, \
                text='Таких ключевых слов в источнике {} нет'.format(feed))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, \
            text='Такого источника нет или у такого источника нет ключевых слов')
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# показать все подписки
def showsubs(update, context):
    try:
        global feeds
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Подписки: {}'.format(', '.join(list(feeds.keys()))))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# показать все ключевые слова
def showkeywords(update, context):
    try:
        global keywords
        show = '\n'.join(['{}: {}'.format(feed, ', '.join(keywords[feed])) for feed in keywords])
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text='Ключевые слова: \n{}'.format(show))
    except Exception as ex:
        context.bot.send_message(chat_id=update.effective_chat.id, \
        text="Что-то пошло не так, попробуйте еще раз"+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# проверка на наличие новостей
def check_for_updates(context):
    try:
        global feeds
        global keywords
        global chat_id

        for source in feeds:
            feed = feeds[source]
            ent = feedparser.parse(feed['link']).entries

            # иногда в валидных ссылках происходят какие-то ошибки
            # в результате которых по ним нет новостей, для этого проверка
            if len(ent) != 0:
                n = 0
                article = ent[0]
                articles = []

                # пока не дойдем до последней увиденной новости или
                # до конца списка новостей, собираем все не просмотренные новости
                while article.published != feed['date'] and n != len(ent) - 1:
                    articles.append(article)
                    n += 1
                    article = ent[n]

                # в обратном порядке просматриваем новости
                for article in articles[::-1]:
                    text = get_description(article, feed, keywords[source])
                    if text:
                        context.bot.send_message(chat_id=chat_id, \
                        text=text,\
                        parse_mode='HTML')

                #закомментировать когда захочется потестить
                #эта строчка обновляет время последней новости у источника
                feed['date'] = ent[0].published
                bump_feeds('feeds.txt', feeds)
    except Exception as ex:
        context.bot.send_message(chat_id=chat_id, \
        text="Ой..."+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# проверка на наличие новостей, но для команды
def check_for_updates_command(update, context):
    try:
        global feeds
        global keywords
        global chat_id

        is_there = False
        for source in feeds:
            feed = feeds[source]
            ent = feedparser.parse(feed['link']).entries
            # иногда в валидных ссылках происходят какие-то ошибки
            # в результате которых по ним нет новостей, для этого проверка
            if len(ent) != 0:
                n = 0
                article = ent[0]
                articles = []

                # пока не дойдем до последней увиденной новости или
                # до конца списка новостей, собираем все не просмотренные новости
                while article.published != feed['date'] and n != len(ent):
                    articles.append(article)
                    n += 1
                    article = ent[n]

                if n != 0:
                    is_there = True

                # в обратном порядке просматриваем новости
                for article in articles[::-1]:
                    text = get_description(article, feed, keywords[source])
                    if text:
                        context.bot.send_message(chat_id=chat_id, \
                        text=text,\
                        parse_mode='HTML')

                #закомментировать когда захочется потестить
                #эта строчка обновляет время последней новости у источника
                feed['date'] = ent[0].published
                bump_feeds('feeds.txt', feeds)
        if not is_there:
            context.bot.send_message(chat_id=chat_id, \
            text="Тут не на что смотреть, уходи.",\
            parse_mode='HTML')
    except Exception as ex:
        context.bot.send_message(chat_id=chat_id, \
        text="Ой..."+'\n'+format_exc())
        add_to_log('log.log', format_exc())

# ловит все, что не подходит под команды
def helpme(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, \
    text="Не понимаю, попробуйте еще раз")

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', start)
sub_handler = CommandHandler('sub', sub)
unsub_handler = CommandHandler('unsub', unsub)
addkeywords_handler = CommandHandler('addkeywords', addkeywords)
deletekeyword_handler = CommandHandler('deletekeywords', deletekeywords)
showsubs_handler = CommandHandler('subs', showsubs)
showkeywords_handler = CommandHandler('keywords', showkeywords)
check_handler = CommandHandler('check', check_for_updates_command)
unknown_handler = MessageHandler(Filters.all, helpme)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(unsub_handler)
dispatcher.add_handler(addkeywords_handler)
dispatcher.add_handler(deletekeyword_handler)
dispatcher.add_handler(showsubs_handler)
dispatcher.add_handler(showkeywords_handler)
dispatcher.add_handler(check_handler)
dispatcher.add_handler(unknown_handler)

# благодаря этой строчке проверяется наличие новостей каждые 3600 сек
worker.run_repeating(check_for_updates, interval=120, first=0, context=chat_id)

updater.start_polling()
updater.idle()
