from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# shouldn't present in a such way 
width = 640
height = 480

def scissor():
    glClearColor(255, 255, 255, 1)
    x_scale = 1/16*width
    y_scale = 1/16*width
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    glLineWidth(3)

    x_start, y_start = 100, 100
    width, height = 200, 200
    glEnable(GL_SCISSOR_TEST)
    glScissor(x_start, y_start, width, height)
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
    glDisable(GL_SCISSOR_TEST)

    glFinish()


def alpha():
    glClearColor(255, 255, 255, 1)
    # x_scale = 1/7*glutGet(GLUT_WINDOW_WIDTH)
    # y_scale = 1/8*glutGet(GLUT_WINDOW_HEIGHT)

    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) 
    glEnable(GL_ALPHA_TEST)

    glAlphaFunc(GL_GEQUAL, 0.5)

    glBegin(GL_QUAD_STRIP)
    # glColor3d(255, 255, 0)
    # glVertex2d(x_scale*1, y_scale*2)
    # glVertex2d(x_scale*5, y_scale*1)
    # glVertex2d(x_scale*4, y_scale*3)
    # glVertex2d(x_scale*4, y_scale*4)
    # glVertex2d(x_scale*5, y_scale*7)
    # glVertex2d(x_scale*1, y_scale*6)

    glColor4f(255, 0, 0, 0.8)
    glVertex2f(0.1*width, 0.1*height)
    glVertex2f(0.1*width, 0.2*height)
    glVertex2f(0.2*width, 0.1*height)
    glVertex2f(0.2*width, 0.4*height)
    glColor4f(255, 0, 0, 0.6)
    glVertex2f(0.4*width, 0.2*height)
    glVertex2f(0.4*width, 0.4*height)
    glColor4f(0, 255, 0, 0.4)
    glVertex2f(0.6*width, 0.45*height)
    glVertex2f(0.5*width, 0.45*height)
    glColor4f(0, 255, 255, 0.5)
    glVertex2f(0.9*width, 0.55*height)
    glVertex2f(0.8*width, 0.55*height)
    glColor4f(0, 0, 255, 0.6)
    glVertex2f(0.8*width, 0.8*height)
    glVertex2f(0.7*width, 0.7*height)
    glVertex2f(0.4*width, 0.65*height)
    glVertex2f(0.2*width, 0.8*height)
    glColor4f(255, 0, 255, 0.6 )
    glVertex2f(0.4*width, 0.3*height)
    glVertex2f(0.3*width, 0.4*height)

    glEnd()
    glDisable(GL_ALPHA_TEST)
    glFinish()


def blending():
    dfactor = GL_SRC_ALPHA
    sfactor = GL_ONE_MINUS_SRC_ALPHA
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(GL_BLEND)
    glBlendFunc(dfactor,sfactor)
    
    quantity = 36

    glBegin(GL_POLYGON)
    glColor4f(1.0, 1.0, 0.0, 0.8)
    for i in range(quantity):
        glVertex2f(cos(2*pi*i/quantity)*0.6+0.2, sin(2*pi*i/quantity)*0.6-0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor4f(0.0, 0.0, 1.0, 0.6)
    for i in range(quantity):
        glVertex2f(cos(2*pi*i/quantity)*0.6, sin(2*pi*i/quantity)*0.6+0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor4f(0.0, 1.0, 0.0, 0.4)
    for i in range(quantity):
        glVertex2f(cos(2*pi*i/quantity)*0.6-0.2, sin(2*pi*i/quantity)*0.6-0.2)
    glEnd()

    glDisable(GL_BLEND)
    glFinish()
