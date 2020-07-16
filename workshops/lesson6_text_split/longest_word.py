# получаем слова из словаря
def get_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    words = []
    for line in lines:
        words.append(line.split("\n")[0].lower())

    return words

def split_phrase_direct(phrase, dictionary):
    """
    Функция для разделения фразы без пробелов на слова прямым ходом
    """
    first_letter = 0
    n = len(phrase)

    words = []

    # пока первая буква следующего слова не окажется вне фразы
    while first_letter != n:
        # начинаем идти с конца фразы
        for last_letter in range(n, first_letter, -1):
            # если слово от текущей первой буквы до последней есть в словаре
            # то добавляем его
            if phrase[first_letter:last_letter] in dictionary:
                words.append(phrase[first_letter:last_letter])
                first_letter = last_letter
                break
            # если осталась только одна буква, то добавляем её
            elif last_letter - first_letter == 1:
                words.append(phrase[first_letter:last_letter])
                first_letter = last_letter
                break

    return words

def split_phrase_reverse(phrase, dictionary):
    """
    Функция для разделения фразы без пробелов на слова обратным ходом
    """
    n = len(phrase)
    last_letter = n

    words = []

    # пока последняя буква следующего слова не окажется вне фразы
    while last_letter != 0:
        # начинаем идти с начала фразы
        for first_letter in range(0, last_letter):
            # если слово от текущей первой буквы до последней есть в словаре
            # то добавляем его
            if phrase[first_letter:last_letter] in dictionary:
                words.append(phrase[first_letter:last_letter])
                last_letter = first_letter
                break
            # если осталась только одна буква, то добавляем её
            elif last_letter - first_letter == 1:
                words.append(phrase[first_letter:last_letter])
                last_letter = first_letter
                break

    return words[::-1]

def choose_best(direct, reverse, dictionary):
    """
    Функция для выбора из двух видов разбиений
    Выбирается то разбиение, в котором больше слов из словаря
    """
    direct_n = 0
    for word in direct:
        if word in dictionary:
            direct_n += 1

    reverse_n = 0
    for word in reverse:
        if word in dictionary:
            reverse_n += 1

    if direct_n > reverse_n:
        return direct
    else:
        return reverse

phrases = ['quickbrownfoxjumpoverlazydog',
           'tableapplecharitablecupboarding',
           'themendinehere']
dictionary = get_words('/Users/cmlimm/Documents/uni-projects/workshops/lesson6_text_split/1000.txt')

for phrase in phrases:
    direct = split_phrase_direct(phrase, dictionary)
    reverse = split_phrase_reverse(phrase, dictionary)

    print("Прямой ход:", direct)
    print("Обратный ход", reverse)
    print("Лучший вариант", choose_best(direct, reverse, dictionary))
    print()
