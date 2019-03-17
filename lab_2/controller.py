from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *
from random import randint, random
from numpy import sin, cos, pi, power

import sys
sys.path.append('..')

from lab_1.views import PRIMITIVES
from lab_2.views import TRANSPARENCY, DFACTOR, SFACTOR#, alpha, blending


class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        self.width = 650
        self.height = 650
        self.x_cut = 0
        self.y_cut = 0
        self.ref = 0.0
        self.test = None
        self.current_mode = 'GL_POINTS'
        self.transparency = 'GL_ALWAYS'
        self.sfactor = 'GL_ONE'
        self.dfactor = 'GL_ZERO'
        # self.setFixedSize(self.width, self.height)


    def initializeGL(self):
        """It is called once before the first call to paintGL() or resizeGL(),
        and then once whenever the widget has been assigned a new QGLContext """
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # очистка буферов
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION) # загрузка матрицы проекции
        # gluOrtho2D(0, self.width, 0, self.height) 
        glMatrixMode(GL_MODELVIEW)
        glClearDepth(1.0)
        glShadeModel(GL_SMOOTH)
        glLoadIdentity()

       
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glEnable(GL_ALPHA_TEST)
        glEnable(GL_SCISSOR_TEST)
        glEnable(GL_BLEND)

        glAlphaFunc(TRANSPARENCY[self.transparency], self.ref)
        glScissor(0, 0, int(self.width*(1-self.x_cut/100)), int(self.height*(1-self.y_cut/100)))
        glBlendFunc(SFACTOR[self.sfactor], DFACTOR[self.dfactor]) 
        PRIMITIVES[self.current_mode]()

        glDisable(GL_BLEND)
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        

    def resizeGL(self, w, h):
        self.width = w
        self.height = h

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # glOrtho(0, w, 0, h, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def changeFigure(self, text):
        self.current_mode = text
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()

    def changeTransparency(self, text):
        self.transparency = text
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()

    def changeRef(self, value):
        self.ref = value / 100
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()

    def changeSfactor(self, text):
        # print(text)
        # self.test = GL_BLEND
        self.sfactor = text
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()

    def changeDfactor(self, text):
        self.dfactor = text
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()

    def changeX(self, value):
        self.x_cut = value
        glClear(GL_COLOR_BUFFER_BIT)
        self.updateGL()

    def changeY(self, value):
        self.y_cut = value
        glClear(GL_COLOR_BUFFER_BIT)
        self.updateGL()