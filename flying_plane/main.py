from math import *
from time import process_time
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

window_width = 800
window_height = 600

def init():

    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, window_width / window_height, 0.1, 1000)

    global min_h, max_h, length, filled
    global height_map, landspace_model, skybox_model
    global camPOS, camDIR, camUP, planePOS, planeDIR, plane_angle_counter, angle_delta
    global plane_force_up, plane_force_fwd, reached_max_h, fixed_force_up

    height_map = landscape.height_map('map2.bmp', 0.3)
    min_h = min([min(r) for r in height_map])
    max_h = max([max(r) for r in height_map])
    length = len(height_map)
    height_map[0][:] = [min_h for _ in range(length)]
    height_map[length - 1][:] = [min_h for _ in range(length)]
    height_map[:][0] = [min_h for _ in range(length)]
    height_map[:][length - 1] = [min_h for _ in range(length)]

    planePOS = Vector(length/2, length/2, height_map[round(length/2)][round(length/2)]+2)
    planeDIR = Vector(1, 1, 0).norm()
    plane_angle_counter = 0
    angle_delta = 0
    plane_force_up = 0
    plane_force_fwd = 0
    reached_max_h = False

    camPOS = planePOS.add(Vector(0, 0, 3)).sub(planeDIR.mult(3))
    camUP = Vector(0, 0, 1)

    tile_grassID = skybox.loadImage('tile_grass.jpg')
    tileID = skybox.loadImage('tile.jpg')
    skyboxID = skybox.loadImage('skybox.jpg')

    landspace_model = glGenLists(1)
    glNewList(landspace_model, GL_COMPILE)
    glEnable(GL_TEXTURE_2D)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(length - 1, 0, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(0, -length + 1, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(-length + 1, 0, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(-length + 1, 0, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(0, length - 1, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(0, length - 1, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(length - 1, 0, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glTranslated(length - 1, 0, 0)
    landscape.draw_landscape(height_map, [tileID, tile_grassID], max_h)
    glDisable(GL_TEXTURE_2D)
    glEndList()

    skybox_model = glGenLists(1)
    glNewList(skybox_model, GL_COMPILE)
    glEnable(GL_TEXTURE_2D)
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, skyboxID)
    glRotated(90, 1, 0, 0)
    glScaled(length, length, length)
    skybox.texCube()
    glDisable(GL_TEXTURE_2D)
    glEndList()

    pygame.init()

def keyboardkeys(key, x, y):
    if key == b's':
        pass
    glutPostRedisplay()

def update_camera():
    global camPOS, campUP
    camPOS = planePOS.add(Vector(0, 0, 3)).sub(planeDIR.mult(3))
    camUP = Vector(0, 0, 1).cross(planeDIR).norm().cross(Vector(0, 0, 1).sub(planeDIR)).norm()

def keyboard():
    global planeDIR, planePOS, plane_angle_counter, plane_force_up, plane_force_fwd, reached_max_h, fixed_force_up

    pygame.event.get()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), -3.14/36)
        planeDIR = rotM.mult_vector(planeDIR).norm()
        plane_angle_counter += 0.5
        if plane_angle_counter == 36 or plane_angle_counter == -36:
            plane_angle_counter = 0
    if keys[pygame.K_RIGHT]:
        rotM = Matrix.rotation_matrix(Vector(0, 0, 1), 3.14/36)
        planeDIR = rotM.mult_vector(planeDIR).norm()
        plane_angle_counter -= 0.5
        if plane_angle_counter == 36 or plane_angle_counter == -36:
            plane_angle_counter = 0

    if plane_force_fwd > 20:
        plane_force_up = plane_force_fwd - 20
    else:
        plane_force_up = 0

    if keys[pygame.K_UP]:
        if plane_force_fwd + 0.25 <= 50:
            plane_force_fwd += 0.25
    else:
        if plane_force_fwd - 0.25 >= 0:
            plane_force_fwd -= 0.25

    if keys[pygame.K_DOWN]:
        if plane_force_fwd - 0.25 >= 0:
            plane_force_fwd -= 0.25

    planePOS = planePOS.add(planeDIR.mult(plane_force_fwd/50))
    zero_level = utils.getz(round(planePOS.x, 2), round(planePOS.y, 2), height_map) + 2
    planePOS.z = zero_level + plane_force_up
    if zero_level + plane_force_up > max_h:
        if not reached_max_h:
            reached_max_h = True
            fixed_force_up = plane_force_up
        planePOS.z = max_h + plane_force_up - fixed_force_up
    else:
        if reached_max_h:
            reached_max_h = False
            plane_force_up = fixed_force_up
        planePOS.z = zero_level + plane_force_up
    update_camera()

    if keys[pygame.K_ESCAPE]:
        sys.exit(0)

def draw(*args, **kwargs):
    global angle_delta

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,        # camera position
              planePOS.x, planePOS.y, planePOS.z+2,# point camera is looking at
              camUP.x, camUP.y, camUP.z)           # up direction of camera
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glPushMatrix()
    glTranslated(planePOS.x, planePOS.y, planePOS.z)
    glCallList(skybox_model)
    glPopMatrix()

    glPushMatrix()
    glTranslated(planePOS.x, planePOS.y, planePOS.z)
    glRotated(plane_angle_counter*10, 0, 0, 1)
    objects.plane()

    # propeller
    angle_delta += 20*plane_force_fwd/50
    if angle_delta >= 720:
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
    landscape_x = length*(planePOS.x//length)
    landscape_y = length*(planePOS.y//length)
    glTranslated(landscape_x, landscape_y, 0)
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
init()
glutMainLoop()
