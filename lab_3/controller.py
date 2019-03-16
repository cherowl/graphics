from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *
import sys
import numpy as np

# for testing
sys.path.append('..')
from lab_1.views import PRIMITIVES

rotate_matrix = lambda angle: np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
mirror_matrix = np.array([[-1, 0], [0, 1]])


class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        
        self.width = 800
        self.height = 600
        self.setFixedSize(self.width, self.height)
        self.order = 5 # main variableordeorderr



    def initializeGL(self):
        """It is called once before the first call to paintGL() or resizeGL(),
        and then once whenever the widget has been assigned a new QGLContext """
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # очистка буферов
        # glClear (GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
        glViewport(100, 10, self.width, self.height)
        glMatrixMode(GL_PROJECTION) # загрузка матрицы проекции
        gluOrtho2D(0, self.width, 0, self.height) 
        glMatrixMode(GL_MODELVIEW)
        glClearDepth(1.0)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glShadeModel(GL_SMOOTH)
        glLoadIdentity()

        # glutInitWindowPosition (100, 10)

    def paintGL(self):
        """It is called whenever the widget needs to be painted"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        basic_triangles = np.array([[-0.96, -0.48], [0, -0.48], [0, 0.48], [0.96, -0.48]])
        basic_lines = np.array([[-0.32, -0.16], [0.32, -0.16]])
        self.draw(basic_triangles, basic_lines)
        # glutSwapBuffers()

        # for testing
        PRIMITIVES['GL_POINTS']()



    def change_depth(self, value):
        self.order = value


    def draw(self, basic_triangles, basic_lines):
        triangles = basic_triangles
        lines = basic_lines
        if self.order-1:
            triangles, lines = self.get_objects(triangles, basic_lines, np.array([[0,0],[0,0]]), 1)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        for index in range(0, triangles.shape[0], 4):
            glVertex2f(*(triangles[index]))
            glVertex2f(*(triangles[index + 1]))
            glVertex2f(*(triangles[index + 2]))

            glVertex2f(*(triangles[index + 1]))
            glVertex2f(*(triangles[index + 2]))
            glVertex2f(*(triangles[index + 3]))
        glEnd()
        glColor4f(255,255,255,1.0)
        glBegin(GL_LINES)
        for index in range(0, lines.shape[0], 2):
            glVertex2f(*lines[index])
            glVertex2f(*lines[index+1])
        glEnd()


    def rotate(self, arr, angle = np.pi/2):
        rot = rotate_matrix(angle)
        print(rot)
        return np.matmul(arr, rot)


    def get_objects(self, basic_triangles, basic_lines, connections, depth):
        if depth != self.order:
            triangles = self.rotate(basic_triangles/2**(0.5), 3*np.pi/4)
            lines = self.rotate(basic_lines/2**(0.5), 3*np.pi/4)

            shift = triangles[3] - basic_triangles[0]
            triangles -= shift
            lines -= shift

            triangles_copy = np.matmul(triangles.copy(), mirror_matrix)
            lines_copy = np.matmul(lines.copy(), mirror_matrix)   

            triangles = np.append(triangles, triangles_copy, axis=0)
            lines = np.append(lines, lines_copy, axis=0)

            #add connection between copies
            if depth > 1:
                connections = self.rotate(connections/2**(0.5), 3*np.pi/4)
                connections -= shift
                connections_copy = np.matmul(connections.copy(), mirror_matrix)
                connections = np.append(connections, connections_copy, axis=0)
            point_index = 2**((depth-1) if (depth > 1) else 0) - 1
            connections = np.vstack((connections, lines[point_index]))
            connections = np.vstack((connections, np.matmul(connections[-1],mirror_matrix)))
            if depth == 1:
                connections = connections[2:]

            return self.get_objects(triangles, lines, connections, depth + 1)
        else:
            return basic_triangles, np.append(basic_lines, connections, axis=0)


    def resizeGL(self, w, h):
        self.width = w
        self.height = h

        glViewport(0, 0, w, h)
        glOrtho(0, w, 0, h, -1.0, 1.0)
        glLoadIdentity()
