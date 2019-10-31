import feedparser
from bot_utils import *

def check_for_updates(feeds):
    news = []
    for feed in feeds.values():
        entries = feedparser.parse(feed['link']).entries
        n = 0
        new = entries[n]
        while new.published != feed['date']:
            news.append({'title': new.title, 'link':new.link})
            n += 1
            new = entries[n]
    return news
