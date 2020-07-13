def golden_section(function, lower, upper, max_iter, precision):
    """
    Поиска минимума функции одной переменной методом золотого сечения,
    возвращает точку экстремума

    function: функция
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

    return extr

# производная по первой переменной функции
def dx(func, x, y, h):
    return (func(x + h, y) - func(x, y))/h

# производная по второй переменной функции
def dy(func, x, y, h):
    return (func(x, y + h) - func(x, y))/h

# функция
def func(x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y*y)**2 + (2.625 - x + x*y**3)**2

# градиент
def grad(func, x, y, h):
    return (dx(func, x, y, h), dy(func, x, y, h))

def steepest_descent(function, initial, precision, dprecision):
    """
    Поиска минимума функции двух переменных методом наискорейшего спуска

    function: функция
    initial: начальное приближение
    pecision: точность
    """

    step = 0
    x = initial[0]
    y = initial[1]

    # инициализация начальных значений новых значений минимума
    gradient = grad(function, x, y, dprecision)

    # находим значение параметра eta такое, чтобы значение функции
    # в измененной точке было наименьшим
    eta = golden_section(
                        lambda eta: func(x - eta*gradient[0], y - eta*gradient[1]),
                        0, 1, 100, precision
                        )

    x_new = x - eta*gradient[0]
    y_new = y - eta*gradient[1]

    while abs(function(x, y) - function(x_new, y_new)) > precision:
        step += 1
        x = x_new
        y = y_new

        # шаг алгоритма
        gradient = grad(function, x, y, dprecision)

        eta = golden_section(
                            lambda eta: func(x - eta*gradient[0], y - eta*gradient[1]),
                            0, 1, 100, precision
                            )

        x_new = x - eta*gradient[0]
        y_new = y - eta*gradient[1]

    return ((x_new, y_new), function(x_new, y_new), step)

initial = [0.7, 1.4]
precision = 0.0000001
dprecision = 0.001

print("Минимум функции в точке ({0[0]:.4f}, {0[1]:.4f}): {1:.4f}\nКоличество шагов: {2}".format(
    *steepest_descent(func, initial, precision, dprecision)
))
