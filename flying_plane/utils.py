from math import *
from vector import *
from time import process_time

def getz(x, y, H):
    """
    Function to get Z coordinate when you have X and Y coordinates and height map,
    that matches landscape made of triangles (look for Perlin noise or generating
    landscape from image)
    """
    n = len(H)

    if x < 0:
        x = abs(x - n*(x//n))
    else:
        x = x - n*(x//n)

    if y < 0:
        y = abs(y - n*(y//n))
    else:
        y = y - n*(y//n)

    x = round(x, 2)
    y = round(y, 2)

    x_0, y_0 = trunc(x), trunc(y)
    x_m, y_m = x - x_0, y - y_0
    # in case we are out of bounds
    # for infinite landscape
    x_0 = x_0 % (n-1)
    y_0 = y_0 % (n-1)
    x_0_p = (x_0 + 1) % (n-1)
    y_0_p = (y_0 + 1) % (n-1)

    if x_0_p == 0:
        x_0 = 0
        x_0_p = 1
    if y_0_p == 0:
        y_0 = 0
        y_0_p = 1

    if x_0 == 0:
        x = 0
    if y_0 == 0:
        y = 0

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
        v_1 = Vector(x_0,     y_0_p, H[x_0][y_0_p])
        v_2 = Vector(x_0,     y_0,     H[x_0][y_0])
        v_3 = Vector(x_0_p, y_0_p, H[x_0_p][y_0_p])

    if square == 'positive' and triangle == 'lower':
        v_1 = Vector(x_0_p, y_0,     H[x_0_p][y_0])
        v_2 = Vector(x_0_p, y_0_p, H[x_0_p][y_0_p])
        v_3 = Vector(x_0,     y_0,     H[x_0][y_0])

    if square == 'negative' and triangle == 'upper':
        v_1 = Vector(x_0_p, y_0_p, H[x_0_p][y_0_p])
        v_2 = Vector(x_0,     y_0_p, H[x_0][y_0_p])
        v_3 = Vector(x_0_p, y_0,     H[x_0_p][y_0])

    if square == 'negative' and triangle == 'lower':
        v_1 = Vector(x_0,     y_0,     H[x_0][y_0])
        v_2 = Vector(x_0,     y_0_p, H[x_0][y_0_p])
        v_3 = Vector(x_0_p, y_0,     H[x_0_p][y_0])

    # in this section of code we determine equation of the plane
    # that contains triangle
    v_12 = v_2.sub(v_1)
    v_13 = v_3.sub(v_1)
    normal = v_12.cross(v_13)
    d = - normal.dot(v_1)

    z = - (normal.x*x + normal.y*y + d)/normal.z
    z = round(z, 2)
    # print("z:", z)
    # print("--------")
    return z

def sign(x):
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0

def isVisible(x1, y1, x2, y2, height_map):
    points = []
    oldx1 = x1
    oldx2 = x2
    oldy1 = y1
    oldy2 = y2
    flag = True

    x1 = ceil(x1)
    x2 = ceil(x2)
    y1 = ceil(y1)
    y2 = ceil(y2)

    dX = abs(x2 - x1)
    dY = abs(y2 - y1)
    if dX >= dY:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            flag = False
        err = 0
        dErr = dY
        y = y1
        dirY = sign(y2 - y1)
        for x in range(x1, x2 + 1):
            z = (x-oldx1)*(getz(oldx2, oldy2, height_map)-
                           getz(oldx1, oldy1, height_map)-10)/(oldx2-oldx1)+getz(oldx1, oldy1, height_map)+10
            if flag:
                if x <= oldx2:
                    if z < height_map[round(x)][round(y)]:
                        return False
            else:
                if x <= oldx1:
                    if z < height_map[round(x)][round(y)]:
                        return False
            err += dErr
            if err + err >= dX:
                    y += dirY
                    err -= dX
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        err = 0
        dErr = dX
        x = x1
        dirX = sign(x2 - x1)
        for y in range(y1, y2 + 1):
            z = (x-oldx1)*(getz(oldx2, oldy2, height_map)-
                           getz(oldx1, oldy1, height_map)-10)/(oldx2-oldx1)+getz(oldx1, oldy1, height_map)+10
            if flag:
                if y <= oldy2:
                    if z < height_map[round(x)][round(y)]:
                        return False
            else:
                if y <= oldy1:
                    if z < height_map[round(x)][round(y)]:
                        return False
            err += dErr
            if err + err >= dY:
                    x += dirX
                    err -= dY
    return True
