from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ESCAPE = b'\x1b'

def keyboard(key, x, y):
    if key == ESCAPE:
        exit(0)

def reshape(w, h):
    width = w
    height = h
    # print(w, h)
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()