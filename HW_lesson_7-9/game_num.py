from random import randint

number = randint(1, 11)
TRIES = 3
print('Компьютер загадал число.\nУ вас есть три попытки. Удачи!')
for i in range(TRIES):
    guess = input('Попробуйте угадать: ')
    if guess.lower() == 'выход':
        break
    guess = int(guess)
    if guess == number:
        print('Победа')
        break
    elif i == TRIES - 1:
        print('Game over!')
    else:       
        print('Повторите еще раз!')
        if guess > number:
            print('Попробуйте число меньше!')
        else:
            print('Попробуйте число больше!')
