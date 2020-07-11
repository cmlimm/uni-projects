from math import sqrt

def function(x):
    return x**2+x**4

def fib(n):
    """
    Функция возвращает n-ное число Фибоначчи, вычисленное по формуле Бине
    """
    return round((((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5))

def fibonacci_section(function, lower, upper, iterations):
    """
    Функция поиска экстремума методом чисел Фибоначчи, возвращает экстремум и значение в нем
    function: функция
    lower, upper: границы участка, на котором происходит поиск экстремума
    iterations: целое число, количество шагов
    """

    # рассчитываем начальные значения числе Фибоначчи
    fib_n = fib(iterations)
    fib_n1 = fib(iterations)
    fib_n2 = fib(iterations)

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

        # идем "вниз" по числам Фибоначчи
        fib_n = fib_n1
        fib_n1 = fib_n2
        fib_n2 = fib(n-2)

    extr = (x1 + x2)/2

    return extr, function(extr)

# начальные данные
lower = -10
upper = 10
iterations = 100

print("Минимум функции в точке {0:.4f}: {1:.4f}".format(
    *fibonacci_section(function, lower, upper, iterations)))
