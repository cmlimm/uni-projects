def function(x):
    return x**2+x**4

def golden_section(function, lower, upper, max_iter, precision):
    """
    Функция поиска экстремума методом золотого сечения, возвращает экстремум и значение в нем
    function: функция в символьном виде
    lower, upper: границы участка, на котором происходит поиск экстремума
    max_iter: целое число, максимум итераций
    precision: точность
    """
    iterations = 0

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

        iterations += 1

    extr = (lower + upper)/2

    return extr, function(extr)

# начальные данные
lower = -10
upper = 10
max_iter = 100
precision = 0.001

print("Минимум функции в точке {0:.4f}: {1:.4f}".format(
    *golden_section(function, lower, upper, max_iter, precision)))
