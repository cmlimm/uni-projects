from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0) # Определяем границы рисования по горизонтали и вертикали

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    if key == b'\x1b':
        sys.exit(0)
    glutPostRedisplay()         # Вызываем процедуру перерисовки

def draw_cube(centre, edge, color):
    radius = edge/2
    centre_x = centre[0]
    centre_y = centre[1]
    centre_z = centre[2]

    r = color[0]
    g = color[1]
    b = color[2]

    x = [centre_x - radius, centre_x + radius]
    y = [centre_y - radius, centre_y + radius]
    z = [centre_z - radius, centre_z + radius]

    glColor3f(r, g, b)
    glVertex3d(x[0], y[0], z[1])
    glVertex3d(x[1], y[0], z[1])
    glVertex3d(x[1], y[1], z[1])
    glVertex3d(x[0], y[1], z[1])

    glVertex3d(x[0], y[0], z[0])
    glVertex3d(x[1], y[0], z[0])
    glVertex3d(x[1], y[1], z[0])
    glVertex3d(x[0], y[1], z[0])

    glVertex3d(x[1], y[0], z[1])
    glVertex3d(x[1], y[0], z[0])
    glVertex3d(x[1], y[1], z[0])
    glVertex3d(x[1], y[1], z[1])

    glVertex3d(x[0], y[1], z[1])
    glVertex3d(x[1], y[1], z[1])
    glVertex3d(x[1], y[1], z[0])
    glVertex3d(x[0], y[1], z[0])

    glVertex3d(x[0], y[0], z[0])
    glVertex3d(x[0], y[1], z[0])
    glVertex3d(x[0], y[1], z[1])
    glVertex3d(x[0], y[0], z[1])

    glVertex3d(x[0], y[0], z[1])
    glVertex3d(x[0], y[0], z[0])
    glVertex3d(x[1], y[0], z[0])
    glVertex3d(x[1], y[0], z[1])

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glRotated(0.125,1,1,1)

    glBegin(GL_QUADS)

    for i in range(11):
        draw_cube([-1 + i*0.2, 0, 0], 0.2, [(11-i)/11, 0, i/11])

    glEnd()

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL 8 cubes!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
