from random import randint

number = randint(1, 4)
guess = int(input('Угадайте число: '))
if guess == number:
    print('Победа')
else:
    print('Повторите еще раз!')
    if guess > number:
        print('Загаданное число меньше, чем вы подумали')
    else:
        print('Загаданное число больше, чем вы подумали')
