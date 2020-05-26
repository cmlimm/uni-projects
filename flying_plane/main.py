from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from vector import *
from matrix import *
import utils
import landscape
import objects
import skybox

window_width = 800
window_height = 600

def init():

    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, window_width / window_height, 0.1, 10000)

    global min_h, max_h, skyboxID, angle_delta, anglex, angley, anglez, zoom, filled, height_map, camPOS, camDIR, camUP, ballPOS, ballDIR, ball_angle_counter, num

    angle_delta = 0

    anglex = 0
    angley = 0
    anglez = 0

    zoom = 1.0
    filled = 0
    skyboxID = skybox.loadImage('skybox.jpg')

    height_map = landscape.height_map('map3.bmp', 0.2)
    min_h = min([min(r) for r in height_map])
    max_h = max([max(r) for r in height_map])

    ballPOS = Vector(129/2, 129/2, height_map[64][64]+5)
    ballDIR = Vector(0.7, 0.7, 0)
    ball_angle_counter = 0

    camPOS = ballPOS.add(Vector(0, 0, 3)).sub(ballDIR.mult(3))
    camUP = Vector(0, 0, 1).cross(ballDIR).cross(Vector(0, 0, 1).sub(ballDIR))
    camUP = Vector(0, 0, 1)

    num = glGenLists(1)
    glNewList(num, GL_COMPILE)
    glEnable(GL_TEXTURE_2D)
    tileID = skybox.loadImage('tile.jpg')
    glBindTexture(GL_TEXTURE_2D, tileID)
    glColor3f(1, 1, 1)
    landscape.draw_landscape(height_map)
    glDisable(GL_TEXTURE_2D)
    glEndList()

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
        anglez -= 5
    if key == b'd':
        anglez += 5
    if key == b'-':
        zoom /= 1.1
    if key == b'=':
        zoom *= 1.1
    if key == b' ':
        filled = 1 - filled

    glutPostRedisplay()

def update_camera():
    global camPOS, campUP
    camPOS = ballPOS.add(Vector(0, 0, 3)).sub(ballDIR.mult(3))
    camUP = Vector(0, 0, 1).cross(ballDIR).cross(Vector(0, 0, 1).sub(ballDIR))

def specialkeys(key, x, y):
    global ballDIR, ballPOS, ball_angle_counter
    if key == GLUT_KEY_UP:
        ballPOS = ballPOS.add(ballDIR)
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map)[0] + 3
        update_camera()
    if key == GLUT_KEY_DOWN:
        ballPOS = ballPOS.sub(ballDIR)
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map)[0] + 3
        update_camera()
    if key == GLUT_KEY_LEFT:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), -3.14/18)
        ballDIR = rotM.mult_vector(ballDIR)
        ball_angle_counter += 1
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0
        update_camera()
    if key == GLUT_KEY_RIGHT:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), 3.14/18)
        ballDIR = rotM.mult_vector(ballDIR)
        ball_angle_counter -= 1
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0
        update_camera()

    glutPostRedisplay()

def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global anglex, angley, anglez, zoom, filled, skyboxID, camPOS, camUP, ballPOS, ball_angle_counter, angle_delta
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,                                  # camera position
              ballPOS.x, ballPOS.y, ballPOS.z+2,                               # point camera is looking at
              camUP.x, camUP.y, camUP.z)                                     # up direction of camera
    glRotated(anglex, 1, 0, 0)
    glRotated(angley, 0, 1, 0)
    glRotated(anglez, 0, 0, 1)

    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glScaled(zoom, zoom, zoom)

    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, skyboxID)
    glTranslated(ballPOS.x, ballPOS.y, ballPOS.z)
    glRotated(90, 1, 0, 0)
    glScaled(max_h, max_h, max_h)
    skybox.texCube()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

    glPushMatrix()
    glTranslated(ballPOS.x, ballPOS.y, ballPOS.z)
    glRotated(ball_angle_counter*10, 0, 0, 1)

    # airframe main
    glPushMatrix()
    glRotated(90, 1, -1, 0)
    glScaled(1, 1, 2.5)
    objects.airframe(0.5, 0.2)
    glPopMatrix()

    # airframe front
    glPushMatrix()
    glTranslated(0.94, 0.94, 0)
    glRotated(90, 1, -1, 0)
    glScaled(1, 1, 0.15)
    objects.airframe(0.4, 0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.64, 0.64, 0)
    glRotated(90, 1, -1, 0)
    objects.circle(0.4, 8)
    glPopMatrix()

    # propeller
    glPushMatrix()
    glTranslated(1, 1, 0)
    glRotated(90, 1, -1, 0)
    glScaled(0.3, 0.3, 0.15)
    objects.propeller(0.15, 0.2)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.05, 1.05, 0)
    glRotated(90, 1, -1, 0)
    glScaled(0.4, 0.4, 0.05)
    objects.airframe(0.25, 0.25)
    glPopMatrix()

    # propeller wings
    angle_delta += 20
    if angle_delta >= 1440:
        angle_delta = 0
    glPushMatrix()
    glTranslated(1.015, 1.015, 0)
    glRotated(45, 0, 0, 1)
    glTranslated(0, 0, 0)
    glRotated(90, 1, 0, 0)
    glRotated(-45-angle_delta, 1, 0, 0)
    glScaled(0.01, 2, 0.3)
    objects.sphere()
    glPopMatrix()

    # wings
    glPushMatrix()
    glTranslated(0.35, 0.35, 0.4)
    # small supports on the frame
    glPushMatrix()
    glColor3f(1, 0.8, 0)
    glTranslated(0.3, 0, 0)
    glRotated(20, 1, 1, 0)
    glScaled(0.05, 0.05, 0.5)
    objects.cube()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0.8, 0)
    glTranslated(0, 0.3, 0)
    glRotated(-20, 1, 1, 0)
    glScaled(0.05, 0.05, 0.5)
    objects.cube()
    glPopMatrix()

    # large supports on the wings
    glPushMatrix()
    glRotated(45, 0, 0, 1)
    glTranslated(0.3, 0, 0)
    glColor3f(1, 0.8, 0)

    glPushMatrix()
    glTranslated(0, 1.3, -0.1)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    objects.cube()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -1.3, -0.1)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    objects.cube()
    glPopMatrix()

    glTranslated(-0.37, 0, 0)
    glPushMatrix()
    glTranslated(0, 1.5, 0)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    objects.cube()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -1.5, 0)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    objects.cube()
    glPopMatrix()

    glPopMatrix()

    # upper wing
    glPushMatrix()
    glColor3f(1, 0.5, 0)
    glTranslated(0.15, 0.15, 0.3)
    glRotated(45, 0, 0, 1)
    glScaled(0.7, 4, 0.15)
    objects.cube()
    glPopMatrix()

    # bottom wing
    glPushMatrix()
    glColor3f(1, 0.5, 0)
    glTranslated(0.08, 0.08, -0.5)
    glRotated(45, 0, 0, 1)
    glScaled(0.7, 4, 0.15)
    objects.cube()
    glPopMatrix()
    glPopMatrix()

    # flops
    glPushMatrix()
    glColor3f(0.9, 0, 0)
    glRotated(45, 0, 0, 1)
    glTranslated(-1, 0, 0.35)
    glScaled(0.3, 0.1, 0.3)
    glRotated(-15, 0, 1, 0)
    objects.cilinder(0.6, 0.2, 4)
    glPopMatrix()

    glPopMatrix()

    glCallList(num)

    glutSwapBuffers()
    glutPostRedisplay()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Flying plane")
glShadeModel(GL_FLAT)
glutDisplayFunc(draw)
glutKeyboardFunc(keyboardkeys)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()
