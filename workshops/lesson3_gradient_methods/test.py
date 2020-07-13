def f(x, y): #initial function
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2


def partialX(f, x, y, d): #take the partial derivative by X
    return (f(x + d, y) - f(x, y))/d

def partialY(f, x, y, d): #take the partial derivative by Y
    return (f(x, y + d) - f(x, y))/d

def grad(f, x, y, d): #function for finding the gradient
    x0 = partialX(f, x, y, d)
    y0 = partialY(f, x, y, d)
    return (x0, y0) #output is the vector of patial derivatives

def nesterov_m(f, initial, eta, eps, d, max_iter, gamma):

    step = 0
    x = initial[0]
    y = initial[1]
    dir = [0, 0]

    gradient = grad(f, x, y, d)
    x_new = x - eta*gradient[0]
    y_new = y - eta*gradient[1]

    array = [(x_new, y_new)]

    while abs(f(x, y) - f(x_new, y_new)) > eps and step < 1000:
        step += 1
        x = x_new
        y = y_new

        gradient = grad(f, x - gamma*dir[0], y - gamma*dir[1], d)
        dir[0] = gamma*dir[0] + eta*(gradient[0])
        dir[1] = gamma*dir[1] + eta*(gradient[1])

        x_new = x - dir[0]
        y_new = y - dir[1]

        array.append((x_new, y_new)) #array of every steps

    return (x_new, y_new), step, array

step = 0.01
eps = 10**(-7)
d = 0.001
max_iter = 1000
gamma = 0.9
initial = [0.7, 1.4]

minf, iters, array = nesterov_m(f, initial, step, eps, d, max_iter, gamma)
print(minf, iters)
