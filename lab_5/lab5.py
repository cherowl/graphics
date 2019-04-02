# -*- coding: utf-8 -*-
# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
# Из модуля random импортируем одноименную функцию random
from random import random
import numpy as np
from scipy.spatial import Delaunay
# объявляем массив pointcolor глобальным (будет доступен во всей программе)
global pointcolor

width, height = 600,600
star_lines = {
'first': [[-0.5, 0.30901699437494745],  #x_left, x_r
          0.1180339887498949,           #change y(x)
          [0, 0.16245984811645314],     #y_max_1
          [-587/191, 12526/23875],      #y_max_2
          [-587/809, -81221/404500]],   #y_min
'second':[[-0.30901699437494745, 0.5],  #x_left, x_r
          -0.1180339887498949,          #change y(x)
          [587/191, 12526/23875],       #y_max_1
          [0, 0.16245984811645314],     #y_max_2
          [587/809, -81221/404500]],    #y_min
'third': [[-0.1180339887498949, 0.1180339887498949],  #x_left, x_r
          0,          #change y(x)
          [587/191, 12526/23875],       #y_max_1
          [-587/191, 12526/23875],     #y_max_2
          [0, 0.16245984811645314]]
}

def gen_flag_points() :
    x = np.array(np.arange(-0.8, 0.8, 0.01))
    y = 0.13*np.sin(10*x)
    # y = np.zeros((len(x)))
    # z = np.array([0.8]*len(x))    
    coords = np.empty((len(x)*2,3))
    for i in range(len(x)):
        coords[2*i] = [x[i], y[i], 0.8]
        coords[2*i+1] = [x[i], y[i], -0.8]
    return coords


def gen_triangle_points(index):
        funcs = star_lines[index]
        f_y_max_1 = funcs[2]
        f_y_max_2 = funcs[3]
        f_y_min = funcs[4]
        # print(funcs[0][0], funcs[0][1])
        x = np.arange(funcs[0][0], funcs[0][1]+0.01, 0.01)
        if (len(x)%2):
            x = x[:-1]
        y = np.sin(x)
        change_point = funcs[1]
        triangle = np.empty((2*len(x), 3))
        # print(change_point)
        for i in range(len(x)):
            triangle[2*i] = [x[i], y[i], f_y_min[0]*x[i]+f_y_min[1]]
            if x[i] < change_point:
                triangle[2*i+1] = [x[i], y[i], f_y_max_1[0]*x[i]+f_y_max_1[1]]
            else:
                triangle[2*i+1] = [x[i], y[i],f_y_max_2[0]*x[i]+f_y_max_2[1]]
        return triangle


pointdata_flag = gen_flag_points()
# print(pointdata_flag)
# print('\n\n-------------------------\n\n')
point_triangle_1 = gen_triangle_points('first')
point_triangle_2 = gen_triangle_points('second')
point_triangle_3 = gen_triangle_points('third')
# point_triangle_1 = gen_triangle_points('first')
# print(point_triangle_1)
pointcolor = [0, 0.6, 0.6, 1]

def compile_shader(type, sourse) :
    id = glCreateShader(type)
    glShaderSource(id, sourse)
    glCompileShader(id)

    result = glGetShaderiv(id, GL_COMPILE_STATUS)
    if result == GL_FALSE :
        length = glGetShaderiv(id, GL_INFO_LOG_LENGTH)
        info = glGetShaderInfoLog(id)
        # print('error ! : ', info)
        glDeleteShader(id)
        return None
    return id

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
    glColorPointer(3, GL_FLOAT, 0, pointcolor)

    # glVertexPointer(3, GL_FLOAT, 0, pointdata_flag)
    # glDrawArrays(GL_QUAD_STRIP, 0, len(pointdata_flag))

    glVertexPointer(3, GL_FLOAT, 0, point_triangle_1)
    glDrawArrays(GL_QUAD_STRIP, 0, len(point_triangle_1))
    glVertexPointer(3, GL_FLOAT, 0, point_triangle_2)
    glDrawArrays(GL_QUAD_STRIP, 0, len(point_triangle_2))
    glVertexPointer(3, GL_FLOAT, 0, point_triangle_3)
    glDrawArrays(GL_QUAD_STRIP, 0, len(point_triangle_3))


    glDisableClientState(GL_VERTEX_ARRAY)        # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)         # Отключаем использование массива цветов

    vertexShader = """
    uniform float Time;
    uniform float  K;
    uniform float Velocity;
    uniform float Amp;

    void main(){
        vec4 pos = vec4(vec3(gl_Vertex), 1.0);
        pos.y = Amp * sin( K * (pos.x - Velocity * Time) );

        gl_Position = gl_ModelViewProjectionMatrix * pos;
    }
    """

    fragmentShader = """
    uniform vec4 color;
    void main() {
    	gl_FragColor = color;
    }"""

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)

    time = (glutGet(GLUT_ELAPSED_TIME)/1000.)
    K = 10.0
    Velocity = 1.0
    Amp = 0.13

    uniforms = {
        'time': glGetUniformLocation(shader, 'Time'),
        'K': glGetUniformLocation(shader, 'K'),
        'Velocity': glGetUniformLocation(shader, 'Velocity'),
        'Amp': glGetUniformLocation(shader, 'Amp'),
        'color': glGetUniformLocation(shader, 'color')
        }
    glUniform1f(uniforms['time'], time)
    glUniform1f(uniforms['K'], K)
    glUniform1f(uniforms['Velocity'], Velocity)
    glUniform1f(uniforms['Amp'], Amp)
    glUniform4f(uniforms['color'], *pointcolor)


    glutSwapBuffers()

def main():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutInit(sys.argv)
    glutCreateWindow(b"Shaders!")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glClearColor(0.2, 0.2, 0.2, 1)

    glRotatef(-70, 1, 0, 0)     # Поворот шейдера в нужную проекцию
    # glRotatef(5, 0, 1, 0)

    glutMainLoop()


if __name__ == '__main__': 
    main() # указываем что этот фаил является главным