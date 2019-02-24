from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ESCAPE = b'\x1b'

def mouse(button, state, x, y):
    # if state == GLUT_DOWN:
    #     if button == GLUT_LEFT_BUTTON:
    #         print('left down')
    #     elif button == GLUT_RIGHT_BUTTON:
    #         print('right down')
    # elif state == GLUT_UP:
    #     if button == GLUT_LEFT_BUTTON:
    #         print('left up')
    #     elif button == GLUT_RIGHT_BUTTON:
    #         print('right up')
    pass


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