from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *
from random import randint, random
from numpy import sin, cos, pi, power

import sys
sys.path.append('..')

from lab_1.views import PRIMITIVES
from lab_2.views import TRANSPARENCY, DFACTOR, SFACTOR, alpha, blending


class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        self.width = 800
        self.height = 630
        self.x_cut = 0
        self.y_cut = 0
        self.ref = 0.0
        self.test = None
        self.current_mode = 'GL_POINTS'
        self.transparency = 'GL_ALWAYS'
        self.sfactor = 'GL_ONE'
        self.dfactor = 'GL_ZERO'
        self.setFixedSize(self.width, self.height)

    def initializeGL(self):
        """It is called once before the first call to paintGL() or resizeGL(),
        and then once whenever the widget has been assigned a new QGLContext """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # очистка буферов
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION) # загрузка матрицы проекции
        gluOrtho2D(0, self.width, 0, self.height) 
        glMatrixMode(GL_MODELVIEW)
        glClearDepth(1.0)
        glShadeModel(GL_SMOOTH)
        glLoadIdentity()

       
    def paintGL(self):
        """It is called whenever the widget needs to be painted"""

        if self.test is not None:
            if self.test == GL_ALPHA_TEST:
                glAlphaFunc(TRANSPARENCY[self.transparency], self.ref)
            if self.test == GL_SCISSOR_TEST:
                glScissor(0, 0, self.x_cut, self.y_cut)
            if self.test == GL_BLEND:
                # blending(SFACTOR[self.sfactor], DFACTOR[self.dfactor], self.current_mode) 
                glBlendFunc(SFACTOR[self.sfactor], DFACTOR[self.dfactor]) 

            glEnable(self.test)

            print(self.test, SFACTOR[self.sfactor], DFACTOR[self.dfactor])
            

        if self.current_mode in PRIMITIVES:
            PRIMITIVES[self.current_mode]()
        
        if self.test is not None:
            glDisable(self.test)

        

    def resizeGL(self, w, h):
        self.width = w
        self.height = h

        glViewport(0, 0, w, h)
        glOrtho(0, w, 0, h, -1.0, 1.0)
        glLoadIdentity()

    def changeFigure(self, text):
        print(text)
        self.test = None
        self.current_mode = text
        self.updateGL()

    def changeTransparency(self, text):
        print(text)
        self.test = GL_ALPHA_TEST
        self.transparency = text
        self.updateGL()

    def changeRef(self, value):
        self.test = GL_ALPHA_TEST
        self.ref = value / 100
        print(self.ref)        
        self.updateGL()

    def changeSfactor(self, text):
        print(text)
        self.test = GL_BLEND
        self.sfactor = text
        self.updateGL()

    def changeDfactor(self, text):
        print(text)
        self.test = GL_BLEND
        self.dfactor = text
        self.updateGL()

    def changeX(self, value):
        print(value)
        self.test = GL_SCISSOR_TEST
        self.x_cut = value
        self.updateGL()

    def changeY(self, value):
        print(value)
        self.test = GL_SCISSOR_TEST
        self.y_cut = value
        self.updateGL()