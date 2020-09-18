from manipulate import Manipulate

def function(x):
    return x**2+x**4

# производная
def d(func, x, h):
    return (func(x + h)-func(x))/h

def bisection(function, lower, upper, max_iter, precision):
    """
    Поиска экстремума функции одной переменной методом бисекции,
    возвращает все пройденные шаги по время поиска экстремума
    (нижняя граница, верхняя граница, точка экстремума)

    function: функция
    lower, upper: границы участка, на котором происходит поиск экстремума
    max_iter: целое число, максимум итераций
    precision: точность
    """

    iterations = 0
    states = []

    while abs(lower - upper) > precision and iterations <= max_iter:
        current_extr = (lower+upper)/2

        # находим производные в текущей точке и конечных точках отрезка
        current_der = d(function, current_extr, precision)
        lower_der = d(function, lower, precision)
        upper_der = d(function, upper, precision)

        states.append((lower, upper, current_extr))
        # если производная в текущей точке отличается по знаку от производной
        # на одном из концов отрезка, то мы сдвигаем другой конец в текущую точку
        if lower_der*current_der < 0:
            upper = current_extr
        elif upper_der*current_der < 0:
            lower = current_extr

        iterations += 1

    return states

# начальные данные
lower = -5
upper = 10
max_iter = 100
precision = 0.001

states = bisection(function, lower, upper, max_iter, precision)
manipulate = Manipulate(function, (lower, upper), states)
