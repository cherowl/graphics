from OpenGL.GL import *
from PyQt5.QtOpenGL import QGLWidget
from scipy.interpolate import lagrange



class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)     
        self.flag = [[100, 100], [400,100], [400,400], [100,400]]
        self.star = [[-0.19098301, -0.06205414],[-0.30901699437494745, -0.4253254041760194],[0, -0.200811415886227],[0.30901699437494745, -0.4253254041760194],[0.19098301, -0.06205414],[0.5, 0.16245984811645314],[0.1180339887498949, 0.16245984811645314],[0, 0.5257311121191336],[-0.1180339887498949, 0.16245984811645314],[-0.5, 0.16245984811645314]
]


    def initializeGL(self):
        """It is called once before the first call to paintGL() or resizeGL(),
        and then once whenever the widget has been assigned a new QGLContext """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glLoadIdentity()
        glLineWidth(2)
        glColor3f(1,0,0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glBegin(GL_POLYGON)
        for point in self.star:
            glVertex2f(*point)
        glEnd()
        
    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glLoadIdentity()
        