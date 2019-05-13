from PyQt5.QtOpenGL import QGLWidget

from OpenGL.GL import *
from OpenGL.GL.shaders import *
from glm import radians, perspective, vec3, mat4, lookAt
from generate import parallels, meridians, arcs, cuts
from shader_sources import vertexShader as vs, fragmentShader as fs
import numpy as np


class GLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)

        self.vertexShader = vs
        self.fragmentShader = fs

        self.polarEye = vec3(0, 0, 4)
        self.polarCenter = vec3(0, 0, 0)
        self.startX = 0
        self.startY = 0

        self.program = None
        self.mvp_id = 0
        self.color_id = 0

    def initializeGL(self):
        glClearColor(0, 0, 0, 1.0)
        glEnable(GL_DEPTH_TEST)

        vs = compileShader(self.vertexShader, GL_VERTEX_SHADER)
        fs = compileShader(self.fragmentShader, GL_FRAGMENT_SHADER)
        self.program = compileProgram(vs, fs)
        glUseProgram(self.program)

        self.mvp_id = glGetUniformLocation(self.program, 'MVP')
        self.color_id = glGetUniformLocation(self.program, 'fragmentColor')

    def paintGL(self):
        MVP = np.array(self.Projection() * self.View() * self.Model(), np.float32)

        glUniformMatrix4fv(self.mvp_id, 1, GL_FALSE, MVP)
        glUniform4f(self.color_id, 0.0, 0.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnableClientState(GL_VERTEX_ARRAY)  # Включаем использование массива вершин
        for arr_ in parallels:
            glVertexPointer(3, GL_FLOAT, 0, arr_)
            glDrawArrays(GL_LINE_STRIP, 0, len(arr_))

        for arr_ in arcs:
            glVertexPointer(3, GL_FLOAT, 0, arr_)
            glDrawArrays(GL_LINE_STRIP, 0, len(arr_))
        
        for arr_ in meridians:
            glVertexPointer(3, GL_FLOAT, 0, arr_)
            glDrawArrays(GL_LINE_STRIP, 0, len(arr_))

        for arr_ in cuts:
            glVertexPointer(3, GL_FLOAT, 0, arr_)
            glDrawArrays(GL_LINES, 0, len(arr_))


        glDisableClientState(GL_VERTEX_ARRAY)  # Отключаем использование массива вершин

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def toNormal(self, p):
        a = p[0] * np.pi / 180
        b = p[1] * np.pi / 180
        r = p[2]


        x = r * np.cos(a) * np.cos(b)
        y = r * np.sin(a)
        z = -r * np.cos(a) * np.sin(b)
        return vec3(x, y, z)


    def keyPressed(self, key):
        p = self.polarEye
        step = 5
        if key == 87 or key == 16777235:
            if p[0] > 85:
                p[0] = 85
            p[0] += step
        if key == 83 or key == 16777237:
            if p[0] < -85:
                p[0] = -85
            p[0] -= step
        if key == 65 or key == 16777234:
            p[1] -= step
        if key == 68 or key == 16777236:
            p[1] += step
        self.update()

    def wheelEvent(self, event):
        p = self.polarEye
        ang = event.angleDelta().y()
        step = 0.1
        if p[2] > 0.1 and ang > 0:
            p[2] -= step
        if ang < 0:
            p[2] += step
        self.update()

    def Projection(self):
        near = 0.1
        far = 20
        angel = 45.0
        return perspective(radians(angel), self.width() / self.height(), near, far)

    def View(self):
        eye = self.toNormal(self.polarEye)
        center = self.toNormal(self.polarCenter)
        up = vec3(0, -1, 0)
        return lookAt(eye, center, up)

    def Model(self):
        return mat4(1)
