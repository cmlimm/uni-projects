from math import *
from vector import *

def getz(x, y, H):
    """
    Function to get Z coordinate when you have X and Y coordinates and height map,
    that matches landscape made of triangles (look for Perlin noise or generating
    landscape from image)
    """
    x_0, y_0 = trunc(x), trunc(y)
    x_m, y_m = x - x_0, y - y_0

    # There is two types of squares
    # *********     *********
    # *  2   **     **    4 *
    # *   *   * and *   *   *
    # **    1 *     * 3    **
    # *********     *********
    # First is positive
    # Second is negative
    if (x_0 + y_0) % 2 == 0:
        square = 'positive'
    else:
        square = 'negative'

    # then we determine in which part of the square point lies
    if square == 'positive':
        if x_m > y_m:
            # first triangle
            triangle = 'lower'
        else:
            # second triangle
            triangle = 'upper'
    else:
        if 1 - x_m > y_m:
            # third triangle
            triangle = 'lower'
        else:
            # fourth triangle
            triangle = 'upper'

    # now we determine vertecies of triangle that contains our point
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

    # in this section of code we determine equation of the plane
    # that contains triangle
    v_12 = v_2.sub(v_1)
    v_13 = v_3.sub(v_1)
    n = v_12.cross(v_13)
    d = - n.dot(v_1)

    z = - (n.x*x + n.y*y + d)/n.z
    return z
