import re
from math import log

def get_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    words = {}
    for line in lines:
        line = line.split()
        # создаем словарь вида слово: частота
        words[line[0]] = int(line[-1])

    return words

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
    total = 1024908267229
    prob = 0
    
    for word in sentence:
        if word in dictionary:
            prob += log(dictionary[word]/total)
        else:
            prob += log(1/total)

    return prob

phrases = ['themendinehere']

dictionary = get_words('/Users/cmlimm/Documents/uni-projects/workshops/lesson7_probability_model/count_1w.txt')
for phrase in phrases:
    recur = remove_nested(recursive(phrase, dictionary))
    # for sent in recur:
    #     print(sent)
    best = max(recur, key=lambda sent: sentence_log_probability(sent, dictionary))
    print("Наиболее вероятный варинат: ", best)
