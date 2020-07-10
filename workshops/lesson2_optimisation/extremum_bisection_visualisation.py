import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

def function(x):
    return x**2+x**4

def d(func, x, h):
    return func(x + h)-func(x)

def bisection(function, lower, upper, max_iter, precision):
    iterations = 0
    states = []
    while abs(lower - upper) > precision and iterations <= max_iter:
        current_extr = (lower+upper)/2

        current_der = d(function, current_extr, precision)
        lower_der = d(function, lower, precision)
        upper_der = d(function, upper, precision)

        states.append((lower, upper, current_extr, function(current_extr)))

        if lower_der*current_der < 0:
            upper = current_extr
        elif upper_der*current_der < 0:
            lower = current_extr

        iterations += 1

    return states


class ManipulateBisection():
    def __init__(self, states):
        self.states = states
        self.steps = len(states)
        self.fig, self.ax = plt.subplots()

        display_range = np.arange(states[0][0], states[0][1], 0.001)
        value_list = list(map(lambda x: function(x), display_range))
        plt.plot(display_range, value_list, lw=2)

        axstep = plt.axes([0.25, 0.15, 0.65, 0.03])
        self.step_slider = Slider(axstep, 'Step', 0, self.steps - 1, valinit=0, valfmt="%i")

        self.step_slider.on_changed(self.update)

        plt.show()

    def update(self, val):
        step = int(self.step_slider.val)

        lower = self.states[step][0]
        upper = self.states[step][1]
        extr = self.states[step][2]
        val = self.states[step][3]

        plt.scatter(extr, val)

        self.fig.canvas.draw_idle()

lower = -10
upper = 10
max_iter = 100
precision = 0.001

states = bisection(function, lower, upper, max_iter, precision)
print(states)
manipulate = ManipulateBisection(states)
