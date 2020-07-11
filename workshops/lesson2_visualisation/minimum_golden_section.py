from manipulate import Manipulate

def function(x):
    return x**2+x**4

def golden_section(function, lower, upper, max_iter, precision):
    """
    Функция поиска экстремума методом золотого сечения, возвращает экстремум и значение в нем
    function: функция
    lower, upper: границы участка, на котором происходит поиск экстремума
    max_iter: целое число, максимум итераций
    precision: точность
    """

    iterations = 0
    states = [(lower, upper, (lower + upper)/2)]

    while abs(lower - upper) > precision and iterations <= max_iter:

        # вычисление точек деления
        lower_section = upper - (upper - lower)/1.618
        upper_section = lower + (upper - lower)/1.618

        # вычисление значений функции в точках деления
        func_lower_section = function(lower_section)
        func_upper_section = function(upper_section)

        if func_lower_section >= func_upper_section:
            lower = lower_section
        else:
            upper = upper_section

        states.append((lower, upper, (lower + upper)/2))

        iterations += 1

    return states

# начальные данные
lower = -5
upper = 10
max_iter = 100
precision = 0.001

states = golden_section(function, lower, upper, max_iter, precision)
manipulate = Manipulate(function, (lower, upper), states)
