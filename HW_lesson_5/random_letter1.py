import random

words = ['самовар', 'весна', 'лето']
word = random.choice(words)
letterNumber = random.randint(0, len(word)-1)
letter = word[letterNumber]
wordQuestion = word[:letterNumber] + '?' + word[letterNumber+1:]

print(wordQuestion)
while True:
    guess = input('Введите букву: ')
    if guess == letter:
        print('Победа!')
        break
    else:
        print('Увы! Попробуйте еще раз.')
print('Слово: ' + word)
