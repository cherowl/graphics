from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from additional import keyboard, mouse, reshape
import lab1
import lab2
width = 512
height = 512

if __name__ == '__main__':

    glutInit(argv)
    # Create a double-buffer RGBA window.   (Single-buffering is possible.
    # So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGBA) #GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH
    glutInitWindowSize(width, height)
    # Create a window, setting its title
    glutCreateWindow('Lab_1&2')

    # Set the display callback.  You can set other callbacks for keyboard and
    # mouse events.
    glutDisplayFunc(lab2.alpha)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()