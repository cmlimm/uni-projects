from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from vector import *
from matrix import *
import bmp_to_map

window_width = 800
window_height = 600

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0) # Белый цвет для первоначальной закраски
    glMatrixMode(GL_PROJECTION) # Выбираем матрицу проекций
    glLoadIdentity()            # Сбрасываем все предыдущие трансформации
    gluPerspective(90, window_width / window_height, 0.001, 10) # Задаем перспективу
	#gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    global anglex, angley, anglez, zoom, filled, height_map, camPOS, camDIR, camUP
    anglex = 0
    angley = 0
    anglez = 0
    zoom = 1.0
    filled = 0
    height_map = bmp_to_map.height_map('map.bmp', 0.2)
    camPOS = Vector(0, 0, -1)
    camDIR = Vector(0, 0, 1)
    camUP = Vector(0, 1, 0)

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    global anglex, angley, anglez, zoom, filled, camPOS, camDIR, camUP
    if key == b'\x1b':
        sys.exit(0)
    if key == b'w':
        anglex += 5
    if key == b's':
        anglex -= 5
    if key == b'q':
        angley += 5
    if key == b'e':
        angley -= 5
    if key == b'a':
        anglez += 5
    if key == b'd':
        anglez -= 5
    if key == b'-':
        zoom /= 1.1
    if key == b'=':
        zoom *= 1.1
    if key == b' ':
        filled = 1 - filled
    if key == b'i':
        camPOS = camPOS.add(camDIR.mult(0.05))
    if key == b'k':
        camPOS = camPOS.sub(camDIR.mult(0.05))
    if key == b'l':
        rotM = Matrix.rotation_matrix(camUP, 3.14/18)
        camDIR = rotM.mult_vector(camDIR)
    if key == b'j':
        rotM = Matrix.rotation_matrix(camUP, -3.14/18)
        camDIR = rotM.mult_vector(camDIR)
    if key == b'o':
        rotM = Matrix.rotation_matrix(camDIR, 3.14/18)
        camUP = rotM.mult_vector(camUP)
    if key == b'u':
        rotM = Matrix.rotation_matrix(camDIR, -3.14/18)
        camUP = rotM.mult_vector(camUP)
    if key == b'y':
        cross = camDIR.cross(camUP)
        rotM = Matrix.rotation_matrix(cross, 3.14/18)
        camUP = rotM.mult_vector(camUP)
        camDIR = rotM.mult_vector(camDIR)
    if key == b'h':
        cross = camDIR.cross(camUP)
        rotM = Matrix.rotation_matrix(cross, -3.14/18)
        camUP = rotM.mult_vector(camUP)
        camDIR = rotM.mult_vector(camDIR)
    glutPostRedisplay()         # Вызываем процедуру перерисовки

def cilinder():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_QUAD_STRIP)

	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

def conus():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

def sphere():
	R = 0.5

	for j in range(-9,9):
		glBegin(GL_QUAD_STRIP)

		for i in range(21):
			glVertex3d(R * cos(pi*j/18) * cos(2*pi*i/20), \
				R * cos(pi*j/18) * sin(2*pi*i/20), \
				R * sin(pi*j/18))
			glVertex3d(R * cos(pi*(j+1)/18) * cos(2*pi*i/20), \
				R * cos(pi*(j+1)/18) * sin(2*pi*i/20), \
				R * sin(pi*(j+1)/18))

		glEnd()

def thor():
	R = 0.5
	R2 = R * 0.3

	for i in range(20):
		glBegin(GL_QUAD_STRIP)

		for j in range(21):
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*i/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*i/20), \
				R2 * sin(2*pi*j/20))
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*(i+1)/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*(i+1)/20), \
				R2 * sin(2*pi*j/20))

		glEnd()

def cube():
	glBegin(GL_QUADS)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5, 0.5)

	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5, 0.5)

	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5, 0.5)

	glVertex3d( 0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glEnd()

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glMatrixMode(GL_MODELVIEW) # Выбираем модельно-видовую матрицу
    glLoadIdentity()           # Сбрасываем все предыдущие трансформации
    global anglex, angley, anglez, zoom, filled, texID, camPOS, camDIR, camUP
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,        # Положение камеры
              camPOS.x + camDIR.x, camPOS.y + camDIR.y, camPOS.z + camDIR.z,           # Точка, на которую смотрит камера
              camUP.x, camUP.y, camUP.z)           # Направление "верх" камеры
    glRotated(anglex,1,0,0)
    glRotated(angley,0,1,0)
    glRotated(anglez,0,0,1)
    glRotated(-105,1,0,0)
    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glScaled(zoom, zoom, zoom)

    glColor3f(1, 0, 0)
    glPushMatrix()
    glScaled(0.2, 0.2, 1)
    cilinder()
    glPopMatrix()

    glColor3f(0, 0.5, 0)
    glPushMatrix()
    glTranslated(0, 0, 0.5)
    glScaled(1, 1, 0.2)
    conus()
    glPopMatrix()

    glTranslated(-30, 0, 0)
    n = len(height_map)
    m = len(height_map[0])
    for y in range(1, n, 2):
        for x in range(1, m, 2):
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0, 0, 0)
            glVertex3d(x, y, height_map[x][y])

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

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
