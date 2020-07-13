from math import sqrt
from manipulate import Manipulate

def function(x):
    return x**2+x**4

def fib(n):
    """
    Функция возвращает n-ное число Фибоначчи, вычисленное по формуле Бине
    """
    return round((((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5))

def fibonacci_section(function, lower, upper, iterations):
    """
    Поиска экстремума функции одной переменной методом чисел Фибоначчи,
    возвращает все пройденные шаги по время поиска экстремума
    (нижняя граница, верхняя граница, точка экстремума)
    
    function: функция
    lower, upper: границы участка, на котором происходит поиск экстремума
    iterations: целое число, количество шагов
    """

    # рассчитываем начальные значения числе Фибоначчи
    fib_n = fib(iterations)
    fib_n1 = fib(iterations)
    fib_n2 = fib(iterations)

    states = [(lower, upper, (lower + upper)/2)]

    for n in range(iterations - 1, 0, -1):
        # рассчитываем точки деления
        x1 = lower + (upper - lower)*fib_n2/fib_n
        x2 = lower + (upper - lower)*fib_n1/fib_n

        y1 = function(x1)
        y2 = function(x2)

        if y1 > y2:
            lower = x1
        else:
            upper = x2

        states.append((lower, upper, (lower + upper)/2))

        # идем "вниз" по числам Фибоначчи
        fib_n = fib_n1
        fib_n1 = fib_n2
        fib_n2 = fib(n-2)

    return states

# начальные данные
lower = -5
upper = 10
iterations = 20

states = fibonacci_section(function, lower, upper, iterations)
manipulate = Manipulate(function, (lower, upper), states)
