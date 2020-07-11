from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

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

    states = [(lower, upper)]

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

        states.append((lower, upper))

        # идем "вниз" по числам Фибоначчи
        fib_n = fib_n1
        fib_n1 = fib_n2
        fib_n2 = fib(n-2)

    return states

class Manipulate():
    def __init__(self, function, bounds, states):
        self.states = states

        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)

        # создаем списки с точками графика функции
        self.display_range = np.arange(bounds[0], bounds[1], 0.01)
        self.display_func = list(map(lambda x: function(x), self.display_range))

        # создаем графики функции и границ
        self.plotted, = plt.plot(self.display_range, self.display_func, lw=2)
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

        # изменяем границы
        self.lower_border.set_xdata(state[0])
        self.upper_border.set_xdata(state[1])

        self.fig.canvas.draw_idle()

# начальные данные
lower = -5
upper = 10
iterations = 20

states = fibonacci_section(function, lower, upper, iterations)
manipulate = Manipulate(function, (lower, upper), states)
