from math import log, inf
from heapq import nlargest
import json
import re

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return ''.join(lines)

def write_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

    return True

# загрузка словарей
with open('data/words_count.json', 'r') as file:
    words_count = json.load(file)

with open('data/words_prob.json', 'r') as file:
    words_prob = json.load(file)

# загрузка словарей
with open('data/next_words.json', 'r') as file:
    next_words = json.load(file)

with open('data/all_words_norep.json', 'r') as file:
    all_words_norep = json.load(file)

def bayes(previous, word, neighbours, words_dict):
    # складываем вероятность слова с вероятностями соседствования (до или после) с предыдущими словами
    prob = log(words_dict[word])
    count = 0
    for prev in previous:
        try:
            prob += log(neighbours[word][prev])
            count += 1
        except KeyError:
            pass

    if count == 0:
        return -inf
    else:
        # идея в том, чтобы вероятность не становилась сильно меньше, если предыдущих слов много
        return prob/count

# получаем топ-эн предсказаний следующего слова
# есть возможность учесть, что слово начинается с каких-то букв
def top_n(previous, n, words_list, neighbours, words_dict, beginning=''):
    words_list = filter(lambda word: word.startswith(beginning.lower()), words_list)
    top = nlargest(n, words_list, key=lambda word: bayes(previous, word, neighbours, words_dict))

    return top

# расстояние Хэмминга
def hamming_distance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    h1 = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    h2 = sum(c1 != c2 for c1, c2 in zip(word1[::-1], word2[::-1]))
    
    return min([h1, h2])+abs(n2 - n1)

# функция аналогична подсказке слова, но вместо этого
# исправляет текущее слово с учетом расстояния Хэмминга и вероятностей
def top_n_mistakes(previous, n, mistaken, words_list, neighbours, words_dict):
    top = nlargest(n, words_list,
                   key=lambda word: bayes(previous, word, neighbours, words_dict)*hamming_distance(mistaken, word))

    return top

def recursive(phrase, dictionary, found = []):
    """
    Функция для разделения фразы на все возможные слова рекурсивно

    phrase: фраза без пробелов
    dictionary: словарь
    found: уже найденные слова из разбиения
    """
    first_letter = 0
    n = len(phrase)
    sentences = []

    # если фраза кончилась, то выходим из рекурсии
    if n == 0:
        return found

    # начинаем идти с конца фразы
    for last_letter in range(n, first_letter, -1):
        # если слово от текущей первой буквы до последней есть в словаре
        # то добавляем его
        if phrase[first_letter:last_letter] in dictionary:
            found = found + [phrase[first_letter:last_letter]]
            # запускаем рекурсию от меньшей фразы, то есть убираем слово, которое
            # только что нашли
            rec = recursive(phrase[last_letter:], dictionary, found)
            sentences += [rec]
            # убираем только что найденное слово, чтобы найти другие варианты
            # разбиения
            found = found[:-1]
        # если осталась только одна буква, то добавляем её
        elif last_letter - first_letter == 1:
            found = found + [phrase[first_letter:last_letter]]
            rec = recursive(phrase[last_letter:], dictionary, found)
            sentences += [rec]
            found = found[:-1]

    return sentences

def remove_nested(sentences):
    """
    Функция убирает вложенность из списка списков путем перевода в строку

    sentences: изначальный список предложений
    """
    sentences = str(sentences)
    # убираем лишние открывающие и закрывающие скобки
    sentences = re.sub(r'\[+', '[', sentences)
    sentences = re.sub(r'\]+', ']', sentences)
    sentences = re.sub(r'\], \[', ']\n[', sentences)
    sentences = sentences.split('\n')

    result = []
    for sentence in sentences:
        sentence = [word.strip("[''],") for word in sentence.split()]
        result.append(sentence)

    return result

def sentence_log_probability(sentence, dictionary):
    prob = 0
    for word in sentence:
        prob += log(dictionary[word])

    return prob

def split_sent(sentence, words):
    recur = remove_nested(recursive(sentence, words))
    best = max(recur, key=lambda sent: sentence_log_probability(sent, words))

    return best
