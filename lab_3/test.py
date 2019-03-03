from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

Width = 512
Height = 512

def display():
    
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor4f(255,0,0,1.0)
    glPointSize(20) 
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex3f(-0.9,-0.9, 0.0)
    glVertex3f(-0.9,0.9, 0.0)
    glVertex3f(0.9,0.9, 0.0)
    glVertex3f(0.9,-0.9, 0.0)
    glEnd()
    glDisable(GL_POINT_SMOOTH)

    glFinish()



def keyboard(key, x, y):
    ESCAPE = '\027'
    if key == ESCAPE:
        exit(0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 140)
    glutCreateWindow("test")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutMainLoop()
