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

def impulses_method(function, initial, precision, eta, gamma):
    """
    Поиска минимума функции двух переменных методом импульсов

    function: функция
    initial: начальное приближение
    pecision: точность
    eta: параметр градиентного спуска
    gamma: параметр, определяющий скорость изменения направления движения.
    """

    step = 0
    x = initial[0]
    y = initial[1]
    dir = [0, 0]

    # инициализация начальных значений новых значений минимума
    gradient = grad(function, x, y, precision)
    x_new = x - eta*gradient[0]
    y_new = y - eta*gradient[1]

    while abs(function(x, y) - function(x_new, y_new)) > precision:
        step += 1
        x = x_new
        y = y_new

        # шаг алгоритма
        gradient = grad(function, x, y, 0.001)
        dir[0] = gamma*dir[0] + eta*gradient[0]
        dir[1] = gamma*dir[1] + eta*gradient[1]

        x_new = x - dir[0]
        y_new = y - dir[1]

    return ((x_new, y_new), function(x_new, y_new), step)

initial = [0.7, 1.4]
precision = 0.0000001
eta = 0.01
gamma = 0.9

print("Минимум функции в точке ({0[0]:.4f}, {0[1]:.4f}): {1:.4f}\nКоличество шагов: {2}".format(
    *impulses_method(func, initial, precision, eta, gamma)
))
