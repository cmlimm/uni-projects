from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from vector import *
from matrix import *
import utils
import landscape
import objects
import skybox
from math import trunc

window_width = 800
window_height = 600

def init():

    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, window_width / window_height, 0.1, 10000)

    global up_jump, jump, snowman_coord, min_h, max_h, length, skyboxID, angle_delta, filled, height_map, camPOS, camDIR, camUP, ballPOS, ballDIR, ball_angle_counter, landspace_model, landspace_big

    angle_delta = 0

    filled = 0
    skyboxID = skybox.loadImage('skybox.jpg')

    height_map = landscape.height_map('map4.bmp', 0.3)
    min_h = min([min(r) for r in height_map])
    max_h = max([max(r) for r in height_map])
    length = len(height_map)

    ballPOS = Vector(length/2, length/2, height_map[round(length/2)][round(length/2)]+10)
    ballDIR = Vector(1, 1, 0).norm()
    ball_angle_counter = 0
    jump = 0
    up_jump = True

    camPOS = ballPOS.add(Vector(0, 0, 3)).sub(ballDIR.mult(3))
    # camUP = Vector(0, 0, 1).cross(ballDIR).norm().cross(Vector(0, 0, 1).sub(ballDIR)).norm()
    camUP = Vector(0, 0, 1)

    landspace_model = glGenLists(1)
    glNewList(landspace_model, GL_COMPILE)
    glEnable(GL_TEXTURE_2D)
    tileID = skybox.loadImage('tile.jpg')
    # tileYellowID = skybox.loadImage('tileYellow.jpg')
    tileGrayID = skybox.loadImage('tileGray.jpg')
    landscape.draw_landscape(height_map, [tileID, tileGrayID], max_h)
    # landscape.draw_landscape(height_map, [tileID], max_h)
    glDisable(GL_TEXTURE_2D)
    glEndList()

    # landspace_big = glGenLists(1)
    # glNewList(landspace_big, GL_COMPILE)
    # glPushMatrix()
    # glCallList(landspace_model)
    # glTranslated(length-1, 0, 0)
    # glCallList(landspace_model)
    # glPopMatrix()
    # glEndList()

    pygame.init()

def keyboardkeys(key, x, y):
    global filled
    if key == b' ':
        filled = 1 - filled
    glutPostRedisplay()

def update_camera():
    global camPOS, campUP
    camPOS = ballPOS.add(Vector(0, 0, 3)).sub(ballDIR.mult(3))
    camUP = Vector(0, 0, 1).cross(ballDIR).norm().cross(Vector(0, 0, 1).sub(ballDIR)).norm()

def keyboard():
    global ballDIR, ballPOS, ball_angle_counter

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ballPOS = ballPOS.add(ballDIR.mult(1))
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map) + 10
        update_camera()
    if keys[pygame.K_DOWN]:
        ballPOS = ballPOS.sub(ballDIR.mult(1))
        ballPOS.z = utils.getz(ballPOS.x, ballPOS.y, height_map) + 10
        update_camera()
    if keys[pygame.K_LEFT]:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), -3.14/36)
        ballDIR = rotM.mult_vector(ballDIR).norm()
        ball_angle_counter += 0.5
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0
        update_camera()
    if keys[pygame.K_RIGHT]:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), 3.14/36)
        ballDIR = rotM.mult_vector(ballDIR).norm()
        ball_angle_counter -= 0.5
        if ball_angle_counter == 36 or ball_angle_counter == -36:
            ball_angle_counter = 0
        update_camera()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0)


def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global angle_delta, jump, up_jump
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,     # camera position
              ballPOS.x, ballPOS.y, ballPOS.z+2,# point camera is looking at
              camUP.x, camUP.y, camUP.z)        # up direction of camera

    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, skyboxID)
    glTranslated(ballPOS.x, ballPOS.y, ballPOS.z)
    glRotated(90, 1, 0, 0)
    glScaled(length, length, length)
    skybox.texCube()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

    # if utils.isVisible(ballPOS.x, ballPOS.y, 64, 64, height_map):
    #     if abs(5 - jump) <= 0.001 or jump > 5:
    #         up_jump = False
    #         jump -= 0.05
    #     elif jump < 5 and up_jump:
    #         jump += 0.05
    #     elif jump < 5 and not up_jump:
    #         if abs(jump) <= 0.001:
    #             up_jump = True
    #         else:
    #             jump -= 0.05
    # else:
    #     jump = 0
    #
    # glPushMatrix()
    # glTranslated(64, 64, height_map[64][64]+jump)
    # objects.snowman()
    # glPopMatrix()

    glPushMatrix()
    glTranslated(ballPOS.x, ballPOS.y, ballPOS.z)
    glRotated(ball_angle_counter*10, 0, 0, 1)
    # coef=utils.getz(ballPOS.x, ballPOS.y, height_map)/max_h
    objects.plane()

    # propeller
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
    glPopMatrix()

    glPushMatrix()
    landscape_x = length*(trunc(ballPOS.x)//length)
    landscape_y = length*(trunc(ballPOS.y)//length)
    glTranslated(landscape_x, landscape_y, 0)
    # glCallList(landspace_model)
    # glTranslated(length-1, 0, 0)
    glCallList(landspace_model)
    glPopMatrix()
    keyboard()
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
# glutSpecialFunc(keyboard)
init()
glutMainLoop()
