def function(x):
    return x**2+x**4

# производная
def d(func, x, h):
    return (func(x + h)-func(x))/h

def bisection(function, lower, upper, max_iter, precision):
    """
    Поиски экстремума функции одной переменной методом бисекции,
    возвращает точку экстремума и значение в нем

    function: функция
    lower, upper: границы участка, на котором происходит поиск экстремума
    max_iter: целое число, максимум итераций
    precision: точность
    """
    iterations = 0

    while abs(lower - upper) > precision and iterations <= max_iter:
        current_extr = (lower+upper)/2

        # находим производные в текущей точке и конечных точках отрезка
        current_der = d(function, current_extr, precision)
        lower_der = d(function, lower, precision)
        upper_der = d(function, upper, precision)

        # если производная в текущей точке отличается по знаку от производной
        # на одном из концов отрезка, то мы сдвигаем другой конец в текущую точку
        if lower_der*current_der < 0:
            upper = current_extr
        elif upper_der*current_der < 0:
            lower = current_extr

        iterations += 1

    return current_extr, function(current_extr)

# начальные данные
lower = -10
upper = 10
max_iter = 100
precision = 0.001

print("Экстремум функции в точке {0:.4f}: {1:.4f}".format(
    *bisection(function, lower, upper, max_iter, precision)))
