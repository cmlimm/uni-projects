from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from vector import *
from matrix import *
from PIL import Image

window_width = 800
window_height = 600

def loadImage(imageName):
	im = Image.open(imageName)
	try:
	    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGB", 0, -1)
	except SystemError:
	    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGB", 0, -1)
	glEnable(GL_TEXTURE_2D)
	ID = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, ID)

	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

	glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
	return ID

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0) # Белый цвет для первоначальной закраски
    glMatrixMode(GL_PROJECTION) # Выбираем матрицу проекций
    glLoadIdentity()            # Сбрасываем все предыдущие трансформации
    gluPerspective(90, window_width / window_height, 0.001, 10) # Задаем перспективу
	#gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    global anglex, angley, anglez, zoom, filled, texID, camPOS, camDIR, camUP
    anglex = 0
    angley = 0
    anglez = 0
    zoom = 1.0
    filled = 0
    camPOS = Vector(0, 0, -1)
    camDIR = Vector(0, 0, 1)
    camUP = Vector(0, 1, 0)
    texID = loadImage("skybox.jpg")

def texCube():
	glBegin(GL_QUADS)
	glTexCoord2f(0.75, 0.0); glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(0.50, 0.0); glVertex3f( 1.0, -1.0,  1.0)
	glTexCoord2f(0.50, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.75, 0.5); glVertex3f(-1.0,  1.0,  1.0)

	glTexCoord2f(0.00, 0.0); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.00, 0.5); glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)
	glTexCoord2f(0.25, 0.0); glVertex3f( 1.0, -1.0, -1.0)

	glTexCoord2f(0.25, 1.0); glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.50, 1.0); glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(0.50, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)

	glTexCoord2f(0.50, 0.5); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.50, 1.0); glVertex3f( 1.0, -1.0, -1.0)
	glTexCoord2f(0.75, 1.0); glVertex3f( 1.0, -1.0,  1.0)
	glTexCoord2f(0.75, 0.5); glVertex3f(-1.0, -1.0,  1.0)

	glTexCoord2f(0.25, 0.0); glVertex3f( 1.0, -1.0, -1.0)
	glTexCoord2f(0.25, 0.5); glVertex3f( 1.0,  1.0, -1.0)
	glTexCoord2f(0.50, 0.5); glVertex3f( 1.0,  1.0,  1.0)
	glTexCoord2f(0.50, 0.0); glVertex3f( 1.0, -1.0,  1.0)

	glTexCoord2f(1.00, 0.0); glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.75, 0.0); glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(0.75, 0.5); glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(1.00, 0.5); glVertex3f(-1.0,  1.0, -1.0)
	glEnd()

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
        camPOS = camPOS.add(camDIR.mult(0.1))
    if key == b'k':
        camPOS = camPOS.sub(camDIR.mult(0.1))
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

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glMatrixMode(GL_MODELVIEW) # Выбираем модельно-видовую матрицу
    glLoadIdentity()           # Сбрасываем все предыдущие трансформации
    global anglex, angley, anglez, zoom, filled, texID, camPOS, camDIR, camUP
    filled = 1
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,        # Положение камеры
              camPOS.x + camDIR.x, camPOS.y + camDIR.y, camPOS.z + camDIR.z,           # Точка, на которую смотрит камера
              camUP.x, camUP.y, camUP.z)           # Направление "верх" камеры
    glRotated(anglex,1,0,0)
    glRotated(angley,0,1,0)
    glRotated(anglez,0,0,1)
    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glScaled(zoom, zoom, zoom)

    glColor3f(3, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texID)
    texCube()

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
glutDisplayFunc(draw)
glutKeyboardFunc(keyboardkeys)
init()
glutMainLoop()
