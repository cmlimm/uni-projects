import feedparser
from bs4 import BeautifulSoup
import re

def get_description(article):
    return re.sub('\.(?=\w)', '.\1', BeautifulSoup(article.summary, 'html.parser').get_text())
