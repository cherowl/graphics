from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint, random
from numpy import sin, cos, pi, power


def points():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor4d(1,0,0,0.5)
    glVertex2f(-0.6,-0.3)
    glColor4d(0,1,0,0.2)
    glVertex2f(0,-0.3)
    glColor4d(0,0,1,0.8)
    glVertex2f(0.6,-0.3)
    glEnd()
    glPointSize(30)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glColor4d(1,0,0,0.5)
    glVertex2f(-0.6,0.3)
    glColor4d(0,1,0,0.2)
    glVertex2f(0,0.3)
    glColor4d(0,0,1,0.8)
    glVertex2f(0.6,0.3)
    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def lines():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor4d(255,0,0,0) 
    glVertex2f(0.8,0.8)
    glColor4d(0,255,0,1)
    glVertex2f(-0.8,-0.8)
    glColor4d(0,255,0,0.2)    
    glVertex2f(0.8,-0.8)
    glColor4d(0,0,255, 0.8) 
    glVertex2f(-0.8,0.8)
    glEnd()
    glFinish()


def line_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINE_STRIP)
    counter = 20
    for i in range(counter):
        glColor4d(255, 0, 0, i/counter)
        glVertex2f(cos(2 * pi * i / counter)*0.7, sin(2 * pi * i / counter)*0.7)
    glEnd()
    glFinish()


def line_loop():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    counter = 20
    glColor3d(255, 0, 0)
    for i in range(counter):
        glColor4d(255, 0, 0, i/counter)
        glVertex2f(cos(2 * pi * i / counter)*0.8, sin(2 * pi * i / counter)*0.8)
    glEnd()
    glFinish()


def triangles():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_TRIANGLES)

    glColor4d(255,0,0,1)
    glVertex2d(-.9,-.95)
    glColor4d(0,255,0,0)
    glVertex2d(-.8,-.6)
    glColor4d(0,0,255,.5)
    glVertex2d(-.6,-.75)
    
    glColor4d(0,255,0,1)
    glVertex2d(-.7,-.65)
    glColor4d(0,0,255,0)
    glVertex2d(-.2,0.2)
    glColor4d(255,0,0,.5)
    glVertex2d(0,-0.4)
    
    glColor4d(0,255,0,1)
    glVertex2d(0.2,0.8)
    glColor4d(255,0,0,0)
    glVertex2d(0.8,0-.3)
    glColor4d(0,0,255,0.5)
    glVertex2d(0,0.1)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def triangle_strip():
    glClearColor(255, 255, 255, 1)
    x_scale = 40
    y_scale = 30
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) 
    glLineWidth(3)
    
    glBegin(GL_TRIANGLE_STRIP)

    glColor4d(255,0,0,0.18)
    glVertex2d(0., 0. )
    glColor4d(0,255,0,0.7)
    glVertex2d(-0.6 , -0.9)
    glColor4d(0,0,255,0.49)
    glVertex2d(-0.75, -0.7)
    glColor4d(0,255,0,0.51)
    glVertex2d(-0.5 , -0.5)
    glColor4d(255,0,255,0.5)
    glVertex2d(-0.7 , -0.3)
    glColor4d(255,0,0,0.93)
    glVertex2d(-0.5 , -0.3)
    glColor4d(255,255,0,0.39)
    glVertex2d(-0.5 , 0. )
    glColor4d(0,255,0,0.17)
    glVertex2d(-0.2 , -0.3)
    glColor4d(0,255,255,0.01)
    glVertex2d(0., -0.3)
    glColor4d(0,0,255,0.1)
    glVertex2d(-0.3 , -0.7)
    glColor4d(255,0,255,0.93)
    glVertex2d(0., -0.5)
    glColor4d(255,0,0,0.89)
    glVertex2d(0.1 , -0.8)
    glColor4d(255,255,0,0.42)
    glVertex2d(0.3 , -0.6)
    glColor4d(0,255,0,0.32)
    glVertex2d(0.5 , -0.7)
    glColor4d(0,255,255,0.22)
    glVertex2d(0.3 , -0.3)
    glColor4d(0,0,255,0.14)
    glVertex2d(0.5 , 0.1)
    glColor4d(255,0,255,0.15)
    glVertex2d(-0.1 ,  0.2)

    glEnd()
    glFinish()


def triangle_fan():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    quantity = 30
    glColor4d(255, 0, 0, 1)
    glVertex2f(0,0)
    for i in range(quantity):
        glColor4d(0, 0, int(i*255/quantity), i/quantity)
        glVertex2f(cos(2*pi*i/quantity)*0.8, sin(2*pi*i/quantity)*0.8)

    glEnd()
    glFinish()


def quads():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(2)
    glBegin(GL_QUADS)
    glColor4d(255, 0, 0, 0.2)
    glVertex2f(-0.84, -0.84)
    glVertex2f(-0.84, -0.68)
    glVertex2f(-0.68, -0.36)
    glVertex2f(-0.68, -0.84)
    
    glColor4d(0, 255, 0, 0.5)
    glVertex2f(-0.2 , -0.04)
    glVertex2f(-0.04,  0.28)
    glVertex2f(0.28,  0.28)
    glVertex2f(0.28, -0.04)

    glColor4d(0, 0, 255, 0.8)
    glVertex2f(-0.68, -0.36)
    glVertex2f(-0.6 , -0.12)
    glVertex2f(-0.2 , -0.04)
    glVertex2f(-0.04, -0.68)

    glEnd()
    glFinish()



def quad_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(2)
    glBegin(GL_QUAD_STRIP)
    glColor4d(255, 0, 0,0.9)
    glVertex2f(-0.56, -0.54)
    glVertex2f(-0.56, -0.38)
    glVertex2f(-0.4 , -0.54)
    glVertex2f(-0.4 , -0.06)
    glColor4d(255, 255, 0,0.82)
    glVertex2f(-0.08, -0.38)
    glVertex2f(-0.08, -0.06)
    glColor4d(0, 255, 0,0.25)
    glVertex2f(0.24,  0.02)
    glVertex2f(0.08,  0.02)
    glColor4d(0, 255, 255,0.05)
    glVertex2f(0.72,  0.18)
    glVertex2f(0.56,  0.18)
    glColor4d(0, 0, 255,0.11)
    glVertex2f(0.56,  0.58)
    glVertex2f(0.4 ,  0.42)
    glColor4d(255, 0, 255,0.5)
    glVertex2f(-0.08,  0.58)
    glVertex2f(-0.24,  0.1)

    glEnd()
    glFinish()


def polygon():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) 
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glColor4d(255, 0, 0,0.69)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.6, -0.8)
    glColor4d(255, 255, 0,0.98)
    glVertex2f(-0.2, -0.6)
    glColor4d(0, 255, 0,0.04)
    glVertex2f( 0.2, -0.1)
    glVertex2f( 0. , -0.1)
    glColor4d(0, 255, 255,0.36)
    glVertex2f( 0.8,  0.1)
    glVertex2f( 0.6,  0.1)
    glColor4d(0, 0, 255,0.92)
    glVertex2f( 0.6,  0.6)
    glVertex2f( 0.4,  0.4)
    glColor4d(255, 0, 255,0.15)
    glVertex2f(-0.2,  0.6)
    glVertex2f(-0.4,  0. )

    glEnd()
    glFinish()


PRIMITIVES = {
    'GL_POINTS': points,
    'GL_LINES': lines,
    'GL_LINE_STRIP': line_strip, 
    'GL_LINE_LOOP': line_loop,
    'GL_TRIANGLES': triangles,
    'GL_TRIANGLE_STRIP': triangle_strip, 
    'GL_TRIANGLE_FAN': triangle_fan,
    'GL_QUADS': quads,
    'GL_QUAD_STRIP': quad_strip,
    'GL_POLYGON': polygon,
}