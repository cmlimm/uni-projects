from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from vector import *
from matrix import *
import utils
import landscape
import objects

window_width = 800
window_height = 600

def init():

    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, window_width / window_height, 0.001, 100)

    global angle_delta, anglex, angley, anglez, zoom, filled, height_map, camPOS, camDIR, camUP, ballPOS, ballDIR, ball_angle_counter

    angle_delta = 0

    anglex = 0
    angley = 0
    anglez = 0

    zoom = 1.0
    filled = 0

    height_map = landscape.height_map('map.bmp', 0.2)

    ballPOS = Vector(0, 0, height_map[0][0])
    ballDIR = Vector(0.7, 0.7, 0)
    ball_angle_counter = 0

    camPOS = ballPOS.add(Vector(-2, -2, 1.5))
    camDIR = Vector(0.7, 0.7, 0)
    camUP = Vector(0, 0, 1)

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
        camPOS = camPOS.add(camDIR.mult(0.5))
    if key == b'k':
        camPOS = camPOS.sub(camDIR.mult(0.5))
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

    glutPostRedisplay()

def specialkeys(key, x, y):
    global ballDIR, ballPOS, camPOS, ball_angle_counter
    if key == GLUT_KEY_UP:
        ballPOS = ballPOS.add(ballDIR)
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map) + 3
        camPOS = camPOS.add(ballDIR)
        camPOS.z = ballPOS.z + 1.5
    if key == GLUT_KEY_DOWN:
        ballPOS = ballPOS.sub(ballDIR)
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map) + 3
        camPOS = camPOS.sub(ballDIR)
        camPOS.z = ballPOS.z + 1.5
    if key == GLUT_KEY_LEFT:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), -3.14/18)
        ballDIR = rotM.mult_vector(ballDIR)
        ball_angle_counter += 1
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0
    if key == GLUT_KEY_RIGHT:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), 3.14/18)
        ballDIR = rotM.mult_vector(ballDIR)
        ball_angle_counter -= 1
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0

    glutPostRedisplay()

def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global angle_delta, anglex, angley, anglez, zoom, filled, texID, camPOS, camDIR, camUP, ballPOS, ballDIR, ball_angle_counter
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,                                  # camera position
              camPOS.x + camDIR.x, camPOS.y + camDIR.y, camPOS.z + camDIR.z, # point camera is looking at
              camUP.x, camUP.y, camUP.z)                                     # up direction of camera
    glRotated(anglex,1,0,0)
    glRotated(angley,0,1,0)
    glRotated(anglez,0,0,1)

    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glScaled(zoom, zoom, zoom)

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
    angle_delta += 50
    if angle_delta >= 500:
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

    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    landscape.draw_landscape(height_map)

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
