from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import numpy as np
order = 1 # main variable

rotate_matrix = lambda angle: np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
h_mirror_matrix = np.array([[-1, 0], [0, 1]])
v_mirror_matrix = np.array([[1, 0], [0, -1]])


def rotate(arr, angle = np.pi/2):
    rot = rotate_matrix(angle)
    return np.matmul(arr, rot)

def get_objects(basic_triangles, basic_lines, connections, depth):
    if depth != order:
        triangles = rotate(basic_triangles/2**(0.5), 3*np.pi/4)
        lines = rotate(basic_lines/2**(0.5), 3*np.pi/4)

        shift = triangles[3] - basic_triangles[0]
        triangles -= shift
        lines -= shift

        triangles_copy = np.matmul(triangles.copy(), h_mirror_matrix)
        lines_copy = np.matmul(lines.copy(), h_mirror_matrix)   

        triangles = np.append(triangles, triangles_copy, axis=0)
        lines = np.append(lines, lines_copy, axis=0)

        #add connection between copies
        if depth > 1:
            connections = rotate(connections/2**(0.5), 3*np.pi/4)
            connections -= shift
            connections_copy = np.matmul(connections.copy(), h_mirror_matrix)
            connections = np.append(connections, connections_copy, axis=0)
        point_index = 2**((depth-1) if (depth > 1) else 0) - 1
        connections = np.vstack((connections, lines[point_index]))
        connections = np.vstack((connections, np.matmul(connections[-1],h_mirror_matrix)))
        if depth == 1:
            connections = connections[2:]
    
        return get_objects(triangles, lines, connections, depth + 1)
    else:
        basic_lines = np.append(basic_lines, connections, axis=0)
        shift = np.array([[0, 0.48]])
        basic_triangles += shift
        basic_lines += shift

        added = np.array([[0,0]])
        # print(basic_lines)
        # print(2**(order-1)-1, 2**(order)-1)
        added = np.vstack((added, basic_lines[2**(order-1)-1]))
        added = added[1:]
        added = np.vstack((added, np.matmul(added[0], v_mirror_matrix)))
        added = np.vstack((added, basic_lines[2**(order)-1]))        
        added = np.vstack((added, np.matmul(added[-1], v_mirror_matrix)))
        # print(added)

        
        basic_triangles = np.append(basic_triangles, rotate(basic_triangles.copy(), np.pi), axis=0)
        basic_lines = np.append(basic_lines, rotate(basic_lines.copy(), np.pi), axis=0)
        basic_lines = np.append(basic_lines, added, axis=0)
        

        return basic_triangles, basic_lines, added

def draw(basic_triangles, basic_lines):
    triangles = basic_triangles
    lines = basic_lines
    triangles, lines, added = get_objects(triangles, basic_lines, np.array([[0,0],[0,0]]), 1)
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

    # glPointSize(3)
    # glBegin(GL_POINTS)
    #---------------------------------------------
    # for point in added:
    #     glVertex2f(*point)
    # glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    basic_triangles = np.array([[-0.96, -0.48], [0, -0.48], [0, 0.48], [0.96, -0.48]])
    basic_lines = np.array([[-0.32, -0.16], [0.32, -0.16]])
    draw(basic_triangles, basic_lines)
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
