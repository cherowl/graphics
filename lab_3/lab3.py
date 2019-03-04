from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
order = 2

def draw():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.96, -0.48)
    glVertex2f(0, -0.48)
    glVertex2f(0, 0.48)
    glVertex2f(0.96, -0.48)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(255,255,255,1.0)
    glVertex2f(-0.32, -0.16)
    glVertex2f(0.32, -0.16)
    glEnd()


def action(order):
    glTranslatef(0.5, 0.0, 0.0)
    glScalef(0.5, 0.5, 0.5)
    glRotatef(135, 0.0, 0.0, -1.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()
    action(1)
    draw()
    glPopMatrix()
    glutSwapBuffers()
    # glClearColor(0, 0, 0, 1)
    # glClear(GL_COLOR_BUFFER_BIT)
    # glColor4f(255,0,0,1.0)
    
    # if order - 1:
    #     action(order - 1)
    # # action(1)
    # glFinish()


# def keyboard(key, x, y):
#     ESCAPE = '\027'
#     if key == ESCAPE:
#         exit(0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize (700, 700)
    glutInitWindowPosition (100, 10)
    glutCreateWindow( "OpenGL Test" )
    glutDisplayFunc(display )
    # glutSpecialFunc(KeyboardEvent)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glShadeModel(GL_SMOOTH)
    # init(win_size)
    glutMainLoop()
