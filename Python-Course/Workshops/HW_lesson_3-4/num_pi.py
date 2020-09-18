from math import pi

def pi_fun(x):
    return f'{pi:.{x}f}'

x = int(input('Введите количество знаков после запятой: '))
print(pi_fun(x))
