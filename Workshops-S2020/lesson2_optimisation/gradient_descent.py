# производная по первой переменной функции
def dx(func, x, y, h):
    return (func(x + h, y) - func(x, y))/h

# производная по второй переменной функции
def dy(func, x, y, h):
    return (func(x, y + h) - func(x, y))/h

# функция
def func(x, y):
    return (1.5 - x - x*y)**2 + (2.25 - x - x*y*y)**2 + (2.625 - x - x*y**3)**2

# градиент
def grad(func, x, y, h):
    return (dx(func, x, y, h), dy(func, x, y, h))

def gradient_descent(function, initial, precision, eta):
    """
    Поиска минимума функции двух переменных методом градиентного спуска

    function: функция
    initial: начальное приближение
    pecision: точность
    eta: начальное значение параметра спуска
    """

    step = 1
    x = initial[0]
    y = initial[1]

    # инициализация начальных значений новых значений минимума
    gradient = grad(function, x, y, precision)
    x_new = x - eta*gradient[0]
    y_new = y - eta*gradient[1]

    while abs(function(x, y) - function(x_new, y_new)) > precision:
        step += 1
        x = x_new
        y = y_new

        # шаг алгоритма
        gradient = grad(function, x, y, precision)
        x_new = x - eta*gradient[0]/step
        y_new = y - eta*gradient[1]/step

    return ((x_new, y_new), function(x_new, y_new), step)

initial = [0.7, 1.4]
precision = 0.0000001
eta = 0.01

print("Минимум функции в точке ({0[0]:.4f}, {0[1]:.4f}): {1:.4f}\nКоличество шагов: {2}".format(
    *gradient_descent(func, initial, precision, eta)
))