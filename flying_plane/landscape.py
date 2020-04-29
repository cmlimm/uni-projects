from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageDraw

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
    for x in range(width)[:-1]:
        for y in range(height):
            # darker areas are higher
            array[x][y] = round(pix[x, y]*scale, 3)
    return array

def draw_landscape(height_map):
    n = len(height_map)
    m = len(height_map[0])
    for y in range(1, n, 2):
        for x in range(1, m, 2):
            glBegin(GL_TRIANGLE_FAN)
            h = height_map[x][y]
            if h > 40:
                glColor3f(0.8, 0.8, 0.8)
            elif h > 30:
                glColor3f(0.5, 0.5, 0.5)
            elif h > 10:
                glColor3f(0, 0.6, 0)
            else:
                glColor3f(0, 0.2, 0)
            glVertex3d(x, y, h)

            glVertex3d(x + 1, y, height_map[x + 1][y])
            glVertex3d(x + 1, y + 1, height_map[x + 1][y + 1])
            glVertex3d(x, y + 1, height_map[x][y + 1])
            glVertex3d(x - 1, y + 1, height_map[x - 1][y + 1])
            glVertex3d(x - 1, y, height_map[x - 1][y])
            glVertex3d(x - 1, y - 1, height_map[x - 1][y - 1])
            glVertex3d(x, y - 1, height_map[x][y - 1])
            glVertex3d(x + 1, y - 1, height_map[x + 1][y - 1])
            glVertex3d(x + 1, y, height_map[x + 1][y])

            glEnd()
