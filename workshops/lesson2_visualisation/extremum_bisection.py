import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def function(x):
    return x**2+x**4

# производная
def d(func, x, h):
    return (func(x + h)-func(x))/h

def bisection(function, lower, upper, max_iter, precision):
    """
    Функция поиска экстремума методом бисекции, возвращает экстремум и значение в нем
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

class Manipulate():
    def __init__(self, function, bounds, states):
        self.states = states

        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)

        # создаем списки с точками графика функции
        self.display_range = np.arange(bounds[0], bounds[1], 0.01)
        self.display_func = list(map(lambda x: function(x), self.display_range))

        # создаем графики функции, точки экстремума, границ
        self.plotted, = plt.plot(self.display_range, self.display_func, lw=2)
        self.initial_extr = plt.scatter([states[0][2]],[function(states[0][2])], color='red')
        self.lower_border = plt.axvline(x=states[0][0], color='red')
        self.upper_border = plt.axvline(x=states[0][1], color='red')

        self.ax.margins(x=0)
        axsteps = plt.axes([0.25, 0.15, 0.65, 0.03])

        # создаем слайдер для изменения шага
        steps = len(states)
        self.step_slider = Slider(axsteps, 'Step', 0, steps - 1, valinit=0, valfmt='%0.0f')

        self.step_slider.on_changed(self.update)

        plt.show()

    # функция изменения графика при изменении шага
    def update(self, val):
        # получаем состояние на текущем шаге
        state = self.states[int(self.step_slider.val)]

        # изменяем точку экстремума и границы
        self.initial_extr.set_offsets([state[2], function(state[2])])
        self.lower_border.set_xdata(state[0])
        self.upper_border.set_xdata(state[1])

        self.fig.canvas.draw_idle()

# начальные данные
lower = -5
upper = 10
max_iter = 100
precision = 0.001

states = bisection(function, lower, upper, max_iter, precision)
manipulate = Manipulate(function, (lower, upper), states)
