from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def circle(R, n):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(n+1):
        glColor3f(0.3+1/(i+1), 0.3+1/(i+1), 0.3+1/(i+1))
        glVertex3d(R * cos(2*pi*i/n), R * sin(2*pi*i/n), -0.5)
    glEnd()

def propeller(R1, R2):

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(9):
        glColor3f(1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)))
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(9):
        glColor3f(1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)))
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(9):
        glColor3f(1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)), 1-(0.2+1/(i+1)))
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

def airframe(R1, R2):

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(9):
        glColor3f(1*4/(i+1), 0.8*4/(i+1), 0)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(9):
        glColor3f(1*4/(i+1), 0.8*4/(i+1), 0)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(9):
        glColor3f(1*4/(i+1), 0.8*4/(i+1), 0)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

def sphere():
    R = 0.5

    for j in range(-9,9):
        glBegin(GL_QUAD_STRIP)

        for i in range(21):
            if i % 2 == 0:
                glColor3f(0.5, 0, 0)
            else:
                glColor3f(0.8, 0, 0)
            glVertex3d(R * cos(pi*j/18) * cos(2*pi*i/20), R * cos(pi*j/18) * sin(2*pi*i/20), R * sin(pi*j/18))
            glVertex3d(R * cos(pi*(j+1)/18) * cos(2*pi*i/20), R * cos(pi*(j+1)/18) * sin(2*pi*i/20), R * sin(pi*(j+1)/18))
        glEnd()

def conus():
    R = 0.5
    glBegin(GL_TRIANGLE_FAN)
    glVertex3d( 0,  0, -0.5)
    for i in range(21):
        glVertex3d(R * cos(2*pi*i/20), R * sin(2*pi*i/20), -0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d( 0,  0, 0.5)
    for i in range(21):
        glVertex3d(R * cos(2*pi*i/20), R * sin(2*pi*i/20), -0.5)
    glEnd()

def cilinder(R1, R2, n):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(n+1):
        glColor3f(0.9, 0, 0)
        glVertex3d(R1 * cos(2*pi*i/n), R1 * sin(2*pi*i/n), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(n+1):
        glColor3f(0.9, 0, 0)
        glVertex3d(R1 * cos(2*pi*i/n), R1 * sin(2*pi*i/n), -0.5)
        glVertex3d(R2 * cos(2*pi*i/n), R2 * sin(2*pi*i/n), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(n+1):
        glColor3f(0.9, 0, 0)
        glVertex3d(R2 * cos(2*pi*i/n), R2 * sin(2*pi*i/n), 0.5)
    glEnd()

def thor():
    R = 0.5
    R2 = R * 0.3
    for i in range(20):
        glBegin(GL_QUAD_STRIP)
        for j in range(21):
            glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*i/20), (R + R2 * cos(2*pi*j/20)) * sin(2*pi*i/20), R2 * sin(2*pi*j/20))
            glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*(i+1)/20), (R + R2 * cos(2*pi*j/20)) * sin(2*pi*(i+1)/20), R2 * sin(2*pi*j/20))
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
