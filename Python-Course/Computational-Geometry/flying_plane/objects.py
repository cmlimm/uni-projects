from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def circle(R, n, coef=1):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(n+1):
        glColor3f((0.3+1/(i+1))*coef, (0.3+1/(i+1))*coef, (0.3+1/(i+1))*coef)
        glVertex3d(R * cos(2*pi*i/n), R * sin(2*pi*i/n), -0.5)
    glEnd()

def propeller(R1, R2, coef=1):

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(9):
        glColor3f((1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(9):
        glColor3f((1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(9):
        glColor3f((1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef, (1-(0.2+1/(i+1)))*coef)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

def airframe(R1, R2, coef=1):

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(9):
        glColor3f(1*4*coef/(i+1), 0.8*4*coef/(i+1), 0)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(9):
        glColor3f(1*4*coef/(i+1), 0.8*4*coef/(i+1), 0)
        glVertex3d(R1 * cos(2*pi*i/8), R1 * sin(2*pi*i/8), -0.5)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(9):
        glColor3f(1*4*coef/(i+1), 0.8*4*coef/(i+1), 0)
        glVertex3d(R2 * cos(2*pi*i/8), R2 * sin(2*pi*i/8), 0.5)
    glEnd()

def plane(coef=1):
    glPushMatrix()

    # airframe main
    glPushMatrix()
    glRotated(90, 1, -1, 0)
    glScaled(1, 1, 2.5)
    airframe(0.5, 0.2, coef)
    glPopMatrix()

    # airframe front
    glPushMatrix()
    glTranslated(0.94, 0.94, 0)
    glRotated(90, 1, -1, 0)
    glScaled(1, 1, 0.15)
    airframe(0.4, 0.5, coef)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.64, 0.64, 0)
    glRotated(90, 1, -1, 0)
    circle(0.4, 8, coef)
    glPopMatrix()

    # propeller
    glPushMatrix()
    glTranslated(1, 1, 0)
    glRotated(90, 1, -1, 0)
    glScaled(0.3, 0.3, 0.15)
    propeller(0.15, 0.2, coef)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.05, 1.05, 0)
    glRotated(90, 1, -1, 0)
    glScaled(0.4, 0.4, 0.05)
    airframe(0.25, 0.25, coef)
    glPopMatrix()

    # wings
    glPushMatrix()
    glTranslated(0.35, 0.35, 0.4)
    # small supports on the frame
    glPushMatrix()
    glColor3f(1.0*coef, 0.8*coef, 0)
    glTranslated(0.3, 0, 0)
    glRotated(20, 1, 1, 0)
    glScaled(0.05, 0.05, 0.5)
    cube()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0*coef, 0.8*coef, 0)
    glTranslated(0, 0.3, 0)
    glRotated(-20, 1, 1, 0)
    glScaled(0.05, 0.05, 0.5)
    cube()
    glPopMatrix()

    # large supports on the wings
    glPushMatrix()
    glRotated(45, 0, 0, 1)
    glTranslated(0.3, 0, 0)
    glColor3f(1.0*coef, 0.8*coef, 0)

    glPushMatrix()
    glTranslated(0, 1.3, -0.1)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    cube()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -1.3, -0.1)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    cube()
    glPopMatrix()

    glTranslated(-0.37, 0, 0)
    glPushMatrix()
    glTranslated(0, 1.5, 0)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    cube()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -1.5, 0)
    glRotated(10, 0, 1, 0)
    glScaled(0.05, 0.05, 0.7)
    cube()
    glPopMatrix()
    glPopMatrix()

    # upper wing
    glPushMatrix()
    glColor3f(1.0*coef, 0.5*coef, 0)
    glTranslated(0.15, 0.15, 0.3)
    glRotated(45, 0, 0, 1)
    glScaled(0.7, 4, 0.15)
    cube()
    glPopMatrix()

    # bottom wing
    glPushMatrix()
    glColor3f(1.0*coef, 0.5*coef, 0)
    glTranslated(0.08, 0.08, -0.5)
    glRotated(45, 0, 0, 1)
    glScaled(0.7, 4, 0.15)
    cube()
    glPopMatrix()
    glPopMatrix()

    # flops
    glPushMatrix()
    glColor3f(0.9*coef, 0, 0)
    glRotated(45, 0, 0, 1)
    glTranslated(-1, 0, 0.35)
    glScaled(0.3, 0.1, 0.3)
    glRotated(-15, 0, 1, 0)
    cilinder(0.6, 0.2, 4)
    glPopMatrix()

    glPopMatrix()

def snowman():
    glPushMatrix()
    glScaled(4, 4, 4)
    glPushMatrix()
    glColor3f(0.8, 0.8, 0.8)
    glTranslated(0, 0, -0.25)
    sphere(False)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8, 0.8, 0.8)
    glTranslated(0, 0, 0.4)
    glScaled(0.5, 0.5, 0.5)
    sphere(False)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8, 0.4, 0.1)
    glTranslated(0, 0, 0.6)
    glScaled(0.55, 0.55, 0.05)
    cilinder(1, 1, 10, False)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8, 0.4, 0.1)
    glTranslated(0, 0, 0.65)
    glScaled(0.2, 0.2, 0.2)
    cilinder(1, 1, 10, False)
    glPopMatrix()
    glPopMatrix()

def sphere(flag=True):
    R = 0.5

    for j in range(-9,9):
        glBegin(GL_QUAD_STRIP)

        for i in range(21):
            if flag:
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

def cilinder(R1, R2, n, flag=True):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -0.5)
    for i in range(n+1):
        if flag:
            glColor3f(0.9, 0, 0)
        glVertex3d(R1 * cos(2*pi*i/n), R1 * sin(2*pi*i/n), -0.5)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(n+1):
        if flag:
            glColor3f(0.9, 0, 0)
        glVertex3d(R1 * cos(2*pi*i/n), R1 * sin(2*pi*i/n), -0.5)
        glVertex3d(R2 * cos(2*pi*i/n), R2 * sin(2*pi*i/n), 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, 0.5)
    for i in range(n+1):
        if flag:
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
