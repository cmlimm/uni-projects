from bs4 import BeautifulSoup
from langdetect import detect
from langcodes import Language
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import re

# получение содержания новости
def get_description(article, feed, keywords):
    text = re.sub('\.(?=\w)', '.\1', BeautifulSoup(article.summary, 'html.parser').get_text())

    # если в новости есть ключевые слова
    if find_keywords(article.title + ' ' + text, keywords) or keywords == []:

        # если пользователь запрашивал текст новости у этого источника
        if feed['summary']:

            # у телеграма стоит ограничение на размер сообщений, поэтому
            # на всякий случай проверяем
            if len(text) > 3000:
                text = text[:3000]+'...\nПродолжение по ссылке'
            return '<b>' + article.title + '</b>\n' + text + '\n' + article.link
        else:
            return '<b>' + article.title + '</b>\n' + article.link
    else:
        return False

# наличие или отсутствие ключевых слов
def find_keywords(text, keywords):

    # автоматически пытаемся определить текст новости
    lang = Language.make(language=detect(text)).language_name().lower()
    try:
        stemmer = SnowballStemmer(lang)
    except:
        # если такого языка не нашлось, то просто используем английский
        stemmer = SnowballStemmer('english')

    keywords = [(word.lower(), stemmer.stem(word)) for word in keywords]
    text = word_tokenize(text)
    for key in keywords:
        for word in text:
                if word == key[0] or word == key[1] or stemmer.stem(word) == key[0] or stemmer.stem(word) == key[1]:
                    return True
    return False
