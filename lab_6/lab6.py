# -*- coding: utf-8 -*-
# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

from generate import parallels, meridians, arcs, cuts
from events import mouse, move_camera, move_around_camera, scalar_matrix, ModelMatrix
from shaders import vertexShader, fragmentShader




def compile_shader(type, sourse) :
    shader = glCreateShader(type)
    glShaderSource(shader, sourse)
    glCompileShader(shader)

    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if result == GL_FALSE :
        length = glGetShaderiv(shader, GL_INFO_LOG_LENGTH)
        info = glGetShaderInfoLog(shader)
        glDeleteShader(shader)
        return None
    return shader

def create__shader(vertexShader, fragmentShader) :
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vertexShader)
    fs = compile_shader(GL_FRAGMENT_SHADER, fragmentShader)

    glAttachShader(program, vs)
    glAttachShader(program, fs)

    glLinkProgram(program)
    glValidateProgram(program)
    glDeleteShader(vs)
    glDeleteShader(fs)

    return program

def draw():
    glClear(GL_COLOR_BUFFER_BIT)                    # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)            # Включаем использование массива вершин
    glEnableClientState(GL_COLOR_ARRAY)
    
    for arc in parallels:
        glVertexPointer(3, GL_FLOAT, 0, arc)
        glDrawArrays(GL_LINE_STRIP, 0, len(arc))

    for arc in arcs:
        glVertexPointer(3, GL_FLOAT, 0, arc)
        glDrawArrays(GL_LINE_STRIP, 0, len(arc))
    

    glVertexPointer(3, GL_FLOAT, 0, meridians)
    glDrawArrays(GL_LINES, 0, len(meridians))

    glVertexPointer(3, GL_FLOAT, 0, cuts)
    glDrawArrays(GL_LINES, 0, len(cuts))
    
    glDisableClientState(GL_VERTEX_ARRAY)        # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)         # Отключаем использование массива цветов

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)

    modelMatIdx = glGetUniformLocation(shader, "modelMatrix")
    # print(ModelMatrix)
    glUniformMatrix4fv(modelMatIdx, 1, GL_FALSE, ModelMatrix)

    glutSwapBuffers()

def main():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 0)
    glutInit(sys.argv)
    glutCreateWindow(b"Shaders!")
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    glutMotionFunc(move_camera)
    glutPassiveMotionFunc(move_around_camera)
    
    glutIdleFunc(draw)
    glClearColor(0.2, 0.2, 0.2, 1)


    glRotatef(-50, 1, 0, 0)     # Поворот фигуры в нужную проекцию
    glRotatef(5, 0, 1, 0)
    glRotatef(45, 0, 0, 1)

    glutMainLoop()


if __name__ == '__main__': 
    main() # указываем что этот фаил является главным