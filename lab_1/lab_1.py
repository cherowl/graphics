from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from additional import keyboard, reshape
import display
width = 512
height = 512

if __name__ == '__main__':

    glutInit(argv)
    # Create a double-buffer RGBA window.   (Single-buffering is possible.
    # So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGB) #GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH
    glutInitWindowSize(width, height)
    # Create a window, setting its title
    glutCreateWindow('Primitives')

    # Set the display callback.  You can set other callbacks for keyboard and
    # mouse events.
    glutDisplayFunc(display.triangle_fan)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()