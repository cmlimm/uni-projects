from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

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
