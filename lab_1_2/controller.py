from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *
from random import randint, random
from numpy import sin, cos, pi, power
from lab1 import PRIMITIVES


class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        self.width = 640
        self.height = 480
        self.current_mode = 'GL_POINTS'

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

    def changeFigure(self, text):
        self.current_mode = text
       
    def paintGL(self):
        """It is called whenever the widget needs to be painted"""
        PRIMITIVES[self.current_mode]()

    def resizeGL(self, w, h):
        self.width = w
        self.height = h

        glViewport(0, 0, w, h)
        glOrtho(0, w, 0, h, -1.0, 1.0)
        glLoadIdentity()
