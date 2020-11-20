from math import *
from vector import *

def GetZ(x, y, H):
    x_0, y_0 = trunc(x), trunc(y)
    x_m, y_m = x - x_0, y - y_0

    if (x_0 + y_0) % 2 == 0:
        square = 'positive'
    else:
        square = 'negative'

    if square == 'positive':
        if x_m > y_m:
            triangle = 'lower'
        else:
            triangle = 'upper'
    else:
        if 1 - x_m > y_m:
            triangle = 'lower'
        else:
            triangle = 'upper'

    if square == 'positive' and triangle == 'upper':
        v_1 = Vector(x_0,     y_0 + 1, H[x_0][y_0 + 1])
        v_2 = Vector(x_0,     y_0,     H[x_0][y_0])
        v_3 = Vector(x_0 + 1, y_0 + 1, H[x_0 + 1][y_0 + 1])

    if square == 'positive' and triangle == 'lower':
        v_1 = Vector(x_0 + 1, y_0,     H[x_0 + 1][y_0])
        v_2 = Vector(x_0 + 1, y_0 + 1, H[x_0 + 1][y_0 + 1])
        v_3 = Vector(x_0,     y_0,     H[x_0][y_0])

    if square == 'negative' and triangle == 'upper':
        v_1 = Vector(x_0 + 1, y_0 + 1, H[x_0 + 1][y_0 + 1])
        v_2 = Vector(x_0,     y_0 + 1, H[x_0][y_0 + 1])
        v_3 = Vector(x_0 + 1, y_0,     H[x_0 + 1][y_0])

    if square == 'negative' and triangle == 'lower':
        v_1 = Vector(x_0,     y_0,     H[x_0][y_0])
        v_2 = Vector(x_0,     y_0 + 1, H[x_0][y_0 + 1])
        v_3 = Vector(x_0 + 1, y_0,     H[x_0 + 1][y_0])

    v_12 = v_2.sub(v_1)
    v_13 = v_3.sub(v_1)

    n = v_12.cross(v_13)
    d = - n.dot(v_1)
    z = - (n.x*x + n.y*y + d)/n.z
    return z
