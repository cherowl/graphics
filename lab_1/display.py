from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint, random
from numpy import sin, cos, pi, power

def points():
    # print('draw points')
    # Clear the color and depth buffers
    # left = (width - cube_size) / 2
    # right = left + cube_size
    # bottom = (height - cube_size) / 2
    # top = bottom + cube_size
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
    width = glutGet(GLUT_WINDOW_WIDTH)
    height = glutGet(GLUT_WINDOW_HEIGHT)
    glColor3d(255,0,0) 
    glVertex2f(width*0.05, height*0.05)
    glColor3d(0,255,0)
    glVertex2f(width*0.95,height*0.95)
    glColor3d(0,255,0)    
    glVertex2f(width*0.05,height*0.95)
    glColor3d(0,0,255) 
    glVertex2f(width*0.95,height*0.05)
    glEnd()
    
    # glLineWidth(5)
    # glEnable(GL_LINE_SMOOTH)
    # glEnable(GL_LINE_STIPPLE)
    # glLineStipple(2,58360)   
    # glBegin(GL_LINE_LOOP)
    # glColor3d(1,0,0)
    # glVertex3d(1,3,0)
    # glVertex3d(4,3,0)
    # glColor3d(0,1,0)
    # glVertex3d(3,2.7,0)
    # glColor3d(0,0,1)
    # glVertex3d(2.5,3.7,0)
    # glEnd()
    # glDisable(GL_LINE_SMOOTH)
    # glDisable(GL_LINE_STIPPLE)
    glFinish()


def line_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    width = glutGet(GLUT_WINDOW_WIDTH)
    height = glutGet(GLUT_WINDOW_HEIGHT)
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
    width = glutGet(GLUT_WINDOW_WIDTH)
    height = glutGet(GLUT_WINDOW_HEIGHT)
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


def triangles_strip():
    glClearColor(255, 255, 255, 1)
    x_scale = 1/16*glutGet(GLUT_WINDOW_WIDTH)
    y_scale = 1/16*glutGet(GLUT_WINDOW_HEIGHT)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)
    glEnable(GL_POINT_SMOOTH)
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
    glDisable(GL_POINT_SMOOTH)
    glFinish()

def triangle_fan():

    glClearColor(255, 255, 255, 1)
    width = glutGet(GLUT_WINDOW_WIDTH)
    height = glutGet(GLUT_WINDOW_HEIGHT)
    x_center = width/2
    y_center = height/2
    x_radius = width*0.2
    y_radius = height*0.2
    # print(width, x_center, x_radius, x_step)
    # print(height, y_center, y_radius, y_step)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_TRIANGLE_FAN)
    quantity = randint(5,30)
    glColor3d(255, 0, 0)
    glVertex2f(x_center, y_center)
    for i in range(quantity):
        glColor3d(0, 0, int(i*255/quantity))
        glVertex2f(x_center + cos(2*pi*i/quantity)*x_radius, y_center + sin(2*pi*i/quantity)*y_radius)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()