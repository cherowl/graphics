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
    glVertex2f(100,100)
    glColor4d(0,1,0,0.2)
    glVertex2f(320,100)
    glColor4d(0,0,1,0.8)
    glVertex2f(540,100)
    glEnd()
    glPointSize(30)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glColor4d(1,0,0,0.5)
    glVertex2f(100,400)
    glColor4d(0,1,0,0.2)
    glVertex2f(320,400)
    glColor4d(0,0,1,0.8)
    glVertex2f(540,400)
    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def lines():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor4d(255,0,0,0) 
    glVertex2f(512,384)
    glColor4d(0,255,0,1)
    glVertex2f(128,96)
    glColor4d(0,255,0,0.2)    
    glVertex2f(512,96)
    glColor4d(0,0,255, 0.8) 
    glVertex2f(128,384)
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
        glVertex2f(cos(2 * pi * i / counter)*192+320, sin(2 * pi * i / counter)*192+240)
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
        glVertex2f(cos(2 * pi * i / counter)*192+320, sin(2 * pi * i / counter)*192+240)
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
    glVertex2d(30,40)
    glColor4d(0,255,0,0)
    glVertex2d(50,80)
    glColor4d(0,0,255,0.5)
    glVertex2d(120,20)
    
    glColor4d(0,255,0,1)
    glVertex2d(110,120)
    glColor4d(0,0,255,0)
    glVertex2d(210,400)
    glColor4d(255,0,0,0.5)
    glVertex2d(320,80)
    
    glColor4d(0,255,0,1)
    glVertex2d(320,400)
    glColor4d(255,0,0,0)
    glVertex2d(500,450)
    glColor4d(0,0,255,0.5)
    glVertex2d(490,80)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def triangle_strip():
    glClearColor(255, 255, 255, 1)
    x_scale = 40
    y_scale = 30
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)
    
    glBegin(GL_TRIANGLE_STRIP)

    glColor4d(255,0,0,0.18)
    glVertex2d(40,30)
    glColor4d(0,255,0,0.7)
    glVertex2d(160,30)
    glColor4d(0,0,255,0.49)
    glVertex2d(100,90)
    glColor4d(0,255,0,0.51)
    glVertex2d(200,150)
    glColor4d(255,0,255,0.5)
    glVertex2d(120,210)
    glColor4d(255,0,0,0.93)
    glVertex2d(200,210)
    glColor4d(255,255,0,0.39)
    glVertex2d(200,300)
    glColor4d(0,255,0,0.17)
    glVertex2d(320,210)
    glColor4d(0,255,255,0.01)
    glVertex2d(400,210)
    glColor4d(0,0,255,0.1)
    glVertex2d(280,90)
    glColor4d(255,0,255,0.93)
    glVertex2d(400,150)
    glColor4d(255,0,0,0.89)
    glVertex2d(440,60)
    glColor4d(255,255,0,0.42)
    glVertex2d(520,120)
    glColor4d(0,255,0,0.32)
    glVertex2d(600,90)
    glColor4d(0,255,255,0.22)
    glVertex2d(520,210)
    glColor4d(0,0,255,0.14)
    glVertex2d(600,330)
    glColor4d(255,0,255,0.15)
    glVertex2d(360,360)

    glEnd()
    glFinish()


def triangle_fan():
    glClearColor(255, 255, 255, 1)
    x_center = 320
    y_center = 240
    x_radius = 128
    y_radius = 96
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(1)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_TRIANGLE_FAN)
    quantity = 30
    glColor4d(255, 0, 0, 1)
    glVertex2f(x_center, y_center)
    for i in range(quantity):
        glColor4d(0, 0, int(i*255/quantity), i/quantity)
        glVertex2f(x_center + cos(2*pi*i/quantity)*x_radius, y_center + sin(2*pi*i/quantity)*y_radius)

    glEnd()
    glDisable(GL_POINT_SMOOTH)
    glFinish()


def quads():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(2)
    glBegin(GL_QUADS)
    glColor4d(255, 0, 0, 0.2)
    glVertex2f(64, 48)
    glVertex2f(64, 96)
    glVertex2f(128, 192)
    glVertex2f(128, 48)
    
    glColor4d(0, 255, 0, 0.5)
    glVertex2f(320, 288)
    glVertex2f(384, 384)
    glVertex2f(512, 384)
    glVertex2f(512, 288)

    glColor4d(0, 0, 255, 0.8)
    glVertex2f(128, 192)
    glVertex2f(160, 264)
    glVertex2f(320, 288)
    glVertex2f(384, 96)

    glEnd()
    glFinish()



def quad_strip():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(2)
    glBegin(GL_QUAD_STRIP)
    glColor4d(255, 0, 0,0.9)
    glVertex2f(64, 48)
    glVertex2f(64, 96)
    glVertex2f(128, 48)
    glVertex2f(128, 192)
    glColor4d(255, 255, 0,0.82)
    glVertex2f(256, 96)
    glVertex2f(256, 192)
    glColor4d(0, 255, 0,0.25)
    glVertex2f(384, 216)
    glVertex2f(320, 216)
    glColor4d(0, 255, 255,0.05)
    glVertex2f(576, 264)
    glVertex2f(512, 264)
    glColor4d(0, 0, 255,0.11)
    glVertex2f(512, 384)
    glVertex2f(448, 336)
    glColor4d(255, 0, 255,0.5)
    glVertex2f(256, 384)
    glVertex2f(192, 240)

    glEnd()
    glFinish()


def polygon():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) 
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glColor4d(255, 0, 0,0.69)
    glVertex2f(64, 96)
    glVertex2f(64, 48)
    glVertex2f(128, 48)
    glColor4d(255, 255, 0,0.98)
    glVertex2f(256, 96)
    glColor4d(0, 255, 0,0.04)
    glVertex2f(384, 216)
    glVertex2f(320, 216)
    glColor4d(0, 255, 255,0.36)
    glVertex2f(576, 264)
    glVertex2f(512, 264)
    glColor4d(0, 0, 255,0.92)
    glVertex2f(512, 384)
    glVertex2f(448, 336)
    glColor4d(255, 0, 255,0.15)
    glVertex2f(256, 384)
    glVertex2f(192, 240)

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