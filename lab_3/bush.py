from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from numpy import pi, sin, cos

state = [0.8, -0.95, pi/2]
turn = pi/8
moves = 'LFRFRSRFLFLPLSLFRFRFP'
max_depth = 3
F = [2/84]*2
# L - Left
# R - Right
# F - Front
# S - Save(Push)
# P - Pop

def action(cur_depth):
    global state
    tmp = None
    if cur_depth  != 1:
        for symbol in moves:
            if symbol == 'F':
                if cur_depth == max_depth:
                    glVertex2f(state[0], state[1])
                    glVertex2f(state[0]+F[0]*cos(state[2]), state[1]+F[1]*sin(state[2]))
                    state = [state[0]+F[0]*cos(state[2]), state[1]+F[1]*sin(state[2]), state[2]]
                else:
                    action(cur_depth+1)
            elif symbol == 'L':
                # print(state)
                state[2] += turn
            elif symbol == 'R':
                # print(state)
                state[2] -= turn
            elif symbol == 'S':
                tmp = state.copy()
            elif symbol == 'P':
                if not (tmp is None):
                    state = tmp.copy()
                else:
                    raise ValueError("tmp state is None")

    else:
        if max_depth == 1:
            glVertex2f(state[0], state[1])
            glVertex2f(state[0]+F[0]*cos(state[2]), state[1]+F[1]*sin(state[2]))
            print('this way')
        else:
            action(cur_depth+1)


def display():
    glClearColor(255, 255, 255, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(255,0,0,1.0)
    glBegin(GL_LINES)
    action(1)
    glEnd()
    glFinish()


def keyboard(key, x, y):
    ESCAPE = '\027'
    if key == ESCAPE:
        exit(0)


if __name__ == '__main__':
    win_size = [933, 700]
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(*win_size)
    glutInitWindowPosition(100, 0)
    glutCreateWindow("test")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutMainLoop()
