import random

words = ['самовар', 'весна', 'лето']
word = random.choice(words)
letterNumber = random.randint(0, len(word)-1)
letter = word[letterNumber]
wordQuestion = word[:letterNumber] + '?' + word[letterNumber+1:]

print(wordQuestion)
guess = input('Введите букву: ')
if guess == letter:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз.')
print('Слово: ' + word)
