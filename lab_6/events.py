from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

scalar_matrix = np.array([[1., 0., 0., 0.],[0., 1., 0., 0.],[0., 0., 1., 0.,],[0., 0., 0., 1.]])
scalar_matrix_change = np.array([[0.05, 0., 0., 0.],[0., 0.05, 0., 0.],[0., 0., 0.05, 0.,],[0., 0., 0., 0.]])
is_key_pressed = False
position = np.array([0, 0, 5])
horizontalAngle = np.pi
verticalAngle = 0.
initialFoV = 45.0 # np.pi/4 ????
speed = 3.0
mouseSpeed = 0.005
ModelMatrix = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]])

def mouse(button, state, x, y):
    global scalar_matrix
    global is_key_pressed
    if button == 0:
        is_key_pressed = bool(state)
    if button == 3:
        if all(scalar_matrix[i][i] < 2 for i in range(3)):
            scalar_matrix += scalar_matrix_change
    elif button == 4:
        if all(scalar_matrix[i][i] >0.5 for i in range(3)):
            scalar_matrix -= scalar_matrix_change

def LookAt(eye, center, up):
    Matrix = np.zeros((4,4))
    Z = eye - center
    Z = Z / np.linalg.norm(Z)
    Y = up
    X = np.cross(Y, Z)
    Y = np.cross(Z, X)
    X = X / np.linalg.norm(X)
    Y = Y / np.linalg.norm(Y)
    l = np.array([np.dot(-X, eye ), np.dot(-Y, eye ), np.dot(-Z, eye ), 1.0])
    X = np.append(X, 0.)
    Y = np.append(Y, 0.)
    Z = np.append(Z, 0.)
    
    return np.array([X, Y, Z, l])


def move_around_camera(x, y):
    print('passive', x, y)

def move_camera(x, y):
    print('active', x, y)