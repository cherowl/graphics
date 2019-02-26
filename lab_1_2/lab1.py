from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint, random
from numpy import sin, cos, pi, power

# shouldn't present in a such way 
width = 640
height = 480

def points():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3d(1,0,0)
    glVertex3f(30,30,0)
    glColor3d(0,1,0)
    glVertex3f(100,30,0)
    glColor3d(0,0,1)
    glVertex3f(170,30,0)
    glEnd()
    glPointSize(30)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glColor3d(1,0,0)
    glVertex3f(30,100,0)
    glColor3d(0,1,0)
    glVertex3f(100,100,0)
    glColor3d(0,0,1)
    glVertex3f(170,100,0)
    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def lines():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3d(255,0,0) 
    glVertex2f(width*0.05, height*0.05)
    glColor3d(0,255,0)
    glVertex2f(width*0.95,height*0.95)
    glColor3d(0,255,0)    
    glVertex2f(width*0.05,height*0.95)
    glColor3d(0,0,255) 
    glVertex2f(width*0.95,height*0.05)
    glEnd()
    glFinish()


def line_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINE_STRIP)
    counter = randint(5,30)
    glColor3d(255, 0, 0)
    for i in range(counter):
        glVertex2f(((1+cos(2 * pi * i / counter))*0.4+0.1)*width, ((1+sin(2 * pi * i / counter))*0.4+0.1)*height)
    glEnd()
    glFinish()


def line_loop():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINE_STRIP)
    counter = randint(5,30)
    glColor3d(255, 0, 0)
    for i in range(counter):
        glVertex2f(((1+cos(2 * pi * i / counter))*0.4+0.1)*width, ((1+sin(2 * pi * i / counter))*0.4+0.1)*height)
    glEnd()
    glFinish()


def triangles():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_TRIANGLES)

    glColor3d(255,0,0)
    glVertex2d(30,40)
    glColor3d(0,255,0)
    glVertex2d(50,80)
    glColor3d(0,0,255)
    glVertex2d(120,20)
    
    glColor3d(0,255,0)
    glVertex2d(110,120)
    glColor3d(0,0,255)
    glVertex2d(210,400)
    glColor3d(255,0,0)
    glVertex2d(320,80)
    
    glColor3d(0,255,0)
    glVertex2d(320,400)
    glColor3d(255,0,0)
    glVertex2d(400,500)
    glColor3d(0,0,255)
    glVertex2d(490,80)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def triangle_strip():
    glClearColor(255, 255, 255, 1)
    x_scale = 1/16*width
    y_scale = 1/16*height
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)
    
    glBegin(GL_TRIANGLE_STRIP)

    glColor3d(255,0,0)
    glVertex2d(x_scale,y_scale)
    glColor3d(0,255,0)
    glVertex2d(4*x_scale,y_scale)
    glColor3d(0,0,255)
    glVertex2d(2.5*x_scale,3*y_scale)
    glColor3d(0,255,0)
    glVertex2d(5*x_scale,5*y_scale)
    glColor3d(255,0,255)
    glVertex2d(3*x_scale,7*y_scale)
    glColor3d(255,0,0)
    glVertex2d(5*x_scale,7*y_scale)
    glColor3d(255,255,0)
    glVertex2d(5*x_scale,10*y_scale)
    glColor3d(0,255,0)
    glVertex2d(8*x_scale,7*y_scale)
    glColor3d(0,255,255)
    glVertex2d(10*x_scale,7*y_scale)
    glColor3d(0,0,255)
    glVertex2d(7*x_scale,3*y_scale)
    glColor3d(255,0,255)
    glVertex2d(10*x_scale,5*y_scale)
    glColor3d(255,0,0)
    glVertex2d(11*x_scale,2*y_scale)
    glColor3d(255,255,0)
    glVertex2d(13*x_scale,4*y_scale)
    glColor3d(0,255,0)
    glVertex2d(15*x_scale,3*y_scale)
    glColor3d(0,255,255)
    glVertex2d(13*x_scale,7*y_scale)
    glColor3d(0,0,255)
    glVertex2d(15*x_scale,11*y_scale)
    glColor3d(255,0,255)
    glVertex2d(9*x_scale,12*y_scale)

    glEnd()
    glFinish()


def triangle_fan():
    glClearColor(255, 255, 255, 1)
    x_center = width/2
    y_center = height/2
    x_radius = width*0.2
    y_radius = height*0.2
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_TRIANGLE_FAN)
    quantity = 12
    glColor3d(255, 0, 0)
    glVertex2f(x_center, y_center)
    for i in range(quantity):
        glColor3d(0, 0, int(i*255/quantity))
        glVertex2f(x_center + cos(2*pi*i/quantity)*x_radius, y_center + sin(2*pi*i/quantity)*y_radius)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def quads():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glBegin(GL_QUADS)
    glColor3d(255, 0, 0)
    glVertex2f(0.1*width, 0.1*height)
    glVertex2f(0.1*width, 0.2*height)
    glVertex2f(0.2*width, 0.4*height)
    glVertex2f(0.2*width, 0.1*height)
    
    glColor3d(0, 255, 0)
    glVertex2f(0.5*width, 0.6*height)
    glVertex2f(0.6*width, 0.8*height)
    glVertex2f(0.8*width, 0.8*height)
    glVertex2f(0.8*width, 0.6*height)

    glColor3d(0, 0, 255)
    glVertex2f(0.2*width, 0.4*height)
    glVertex2f(0.25*width, 0.55*height)
    glVertex2f(0.5*width, 0.6*height)
    glVertex2f(0.6*width, 0.2*height)

    glEnd()
    glFinish()



def quad_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glBegin(GL_QUAD_STRIP)
    glColor3d(255, 0, 0)
    glVertex2f(0.1*width, 0.1*height)
    glVertex2f(0.1*width, 0.2*height)
    glVertex2f(0.2*width, 0.1*height)
    glVertex2f(0.2*width, 0.4*height)
    glColor3d(255, 255, 0)
    glVertex2f(0.4*width, 0.2*height)
    glVertex2f(0.4*width, 0.4*height)
    glColor3d(0, 255, 0)
    glVertex2f(0.6*width, 0.45*height)
    glVertex2f(0.5*width, 0.45*height)
    glColor3d(0, 255, 255)
    glVertex2f(0.9*width, 0.55*height)
    glVertex2f(0.8*width, 0.55*height)
    glColor3d(0, 0, 255)
    glVertex2f(0.8*width, 0.8*height)
    glVertex2f(0.7*width, 0.7*height)
    glColor3d(255, 0, 255)
    glVertex2f(0.4*width, 0.8*height)
    glVertex2f(0.3*width, 0.5*height)

    glEnd()
    glFinish()


def polygon():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glBegin(GL_POLYGON)
    glColor3d(255, 0, 0)
    glVertex2f(0.1*width, 0.2*height)
    glVertex2f(0.1*width, 0.1*height)
    glVertex2f(0.2*width, 0.1*height)
    glColor3d(255, 255, 0)
    glVertex2f(0.4*width, 0.2*height)
    glVertex2f(0.4*width, 0.4*height)
    glColor3d(0, 255, 0)
    glVertex2f(0.6*width, 0.45*height)
    glVertex2f(0.5*width, 0.45*height)
    glColor3d(0, 255, 255)
    glVertex2f(0.9*width, 0.55*height)
    glVertex2f(0.8*width, 0.55*height)
    glColor3d(0, 0, 255)
    glVertex2f(0.8*width, 0.8*height)
    glVertex2f(0.7*width, 0.7*height)
    glColor3d(255, 0, 255)
    glVertex2f(0.4*width, 0.8*height)
    glVertex2f(0.3*width, 0.5*height)

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