import feedparser
from bs4 import BeautifulSoup
import re

def get_description(article, keywords):
    text = re.sub('\.(?=\w)', '.\1', BeautifulSoup(article.summary, 'html.parser').get_text())
    if len(text) > 3000:
        text = text[:3000]+'...\nПродолжение по ссылке'
    return text+'\n'
