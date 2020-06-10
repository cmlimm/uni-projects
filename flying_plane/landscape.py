from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageDraw
import skybox
from random import choice

def height_map(filename, scale):
    """
    Function to create height map from grayscale image
    Returns integer array of size [width][height] of image
    """
    image = Image.open(filename)
    width  = image.size[0]
    height = image.size[1]
    pix = image.load()
    array = [[0]*width for _ in range(height)]
    for x in range(width):
        for y in range(height):
            # darker areas are lower
            array[x][y] = round(pix[x, y][0]*scale, 3)
    return array

def draw_landscape(height_map, ids, max_h):
    n = len(height_map)
    m = len(height_map[0])
    hprev = height_map[1][1]
    glBindTexture(GL_TEXTURE_2D, ids[0])
    for y in range(1, n, 2):
        for x in range(1, m, 2):
            h = height_map[x][y]
            glColor3f(1, 1, 1)
            hprev = h
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0.95*h/max_h, 0.95*h/max_h, 0.95*h/max_h)

            k = 10

            xTex = x%k/k
            yTex = y%k/k

            xTexp = (x+1)%k/k
            yTexp = (y+1)%k/k
            if xTexp == 0:
                xTexp = 1
            if yTexp == 0:
                yTexp = 1

            xTexm = (x-1)%k/k
            yTexm = (y-1)%k/k

            glTexCoord2f(xTex, yTex)
            glVertex3d(x, y, h)
            glTexCoord2f(xTexp, yTex)
            glVertex3d(x + 1, y, height_map[x + 1][y])
            glTexCoord2f(xTexp, yTexp)
            glVertex3d(x + 1, y + 1, height_map[x + 1][y + 1])
            glTexCoord2f(xTex, yTexp)
            glVertex3d(x, y + 1, height_map[x][y + 1])
            glTexCoord2f(xTexm, yTexp)
            glVertex3d(x - 1, y + 1, height_map[x - 1][y + 1])
            glTexCoord2f(xTexm, yTex)
            glVertex3d(x - 1, y, height_map[x - 1][y])
            glTexCoord2f(xTexm, yTexm)
            glVertex3d(x - 1, y - 1, height_map[x - 1][y - 1])
            glTexCoord2f(xTex, yTexm)
            glVertex3d(x, y - 1, height_map[x][y - 1])
            glTexCoord2f(xTexp, yTexm)
            glVertex3d(x + 1, y - 1, height_map[x + 1][y - 1])
            glTexCoord2f(xTexp, yTex)
            glVertex3d(x + 1, y, height_map[x + 1][y])

            glEnd()
