from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import numpy as np
order = 7

rotate_matrix = lambda angle: np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
mirror_matrix = np.array([[-1, 0], [0, 1]])

def rotate(arr, angle = np.pi/2):
    rot = rotate_matrix(angle)
    return np.matmul(arr, rot)

def get_triangles(basic_triangles, order):
    if order:
        triangles = rotate(basic_triangles/2**(0.5), 3*np.pi/4)
        triangles -= triangles[3] - basic_triangles[0]
        triangles_copy = np.matmul(triangles.copy(), mirror_matrix)
        triangles = np.append(triangles, triangles_copy, axis=0)
        return get_triangles(triangles, order - 1)
    return basic_triangles


def get_lines(triangles, order):
    lines = np.array([[0,0]])
    for index in range(0, triangles.shape[0], 4):
        shift = (triangles[index+2] - triangles[index+1])/3
        lines = np.vstack((lines, triangles[index] + (triangles[index+3] - triangles[index])/3 + shift))
        lines = np.vstack((lines, triangles[index] + (triangles[index+3] - triangles[index])*2/3 +shift))
    lines = lines[1:]
    print(lines)
    # temp_len = lines.shape[0]
    # half_temp = int(temp_len/2)
    # lines = np.vstack((lines, lines[int(temp_len/4-1)]))
    # lines = np.vstack((lines, lines[int(3*temp_len/4-1)]))
    # for i in range(0, temp_len, 4):
    #         lines = np.vstack((lines, lines[i]))
    #         lines = np.vstack((lines, lines[i+2]))
    # if order % 2:
    #     pass
    # else:
    #     pass
    #     for i in range(1, half_temp, order*2):
    #         lines = np.vstack((lines, lines[i]))
    #         lines = np.vstack((lines, lines[i+4]))
    #         lines = np.vstack((lines, lines[half_temp+i]))
    #         lines = np.vstack((lines, lines[half_temp+i+4]))
    return lines


def draw(basic_triangles):
    triangles = basic_triangles
    triangles = get_triangles(triangles, order-1)
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
    lines = get_lines(triangles, order)
    glBegin(GL_LINES)
    for index in range(0, lines.shape[0], 2):
        glVertex2f(*lines[index])
        glVertex2f(*lines[index+1])
    glEnd()
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(-0.2, -0.16)
    # glVertex2f(-0.32, 0.08)
    glEnd()
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    basic_triangles = np.array([[-0.96, -0.48], [0, -0.48], [0, 0.48], [0.96, -0.48]])
    draw(basic_triangles)
    glutSwapBuffers()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize (700, 700)
    glutInitWindowPosition (100, 10)
    glutCreateWindow("OpenGL Test")
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glShadeModel(GL_SMOOTH)
    glutMainLoop()
