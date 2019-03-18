from OpenGL.GL import *
from PyQt5.QtOpenGL import QGLWidget
from scipy.interpolate import lagrange



class GLWidget(QGLWidget):
    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)     
        self.in_move = False
        self.focus_point = -1
        self.int_points = [[100., 100.], [200., 200.], [300., 300.], [400., 400.], [500., 500.], [550., 550.]]
        self.polinomial = self.get_polynomial()


    def initializeGL(self):
        """It is called once before the first call to paintGL() or resizeGL(),
        and then once whenever the widget has been assigned a new QGLContext """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width(), self.height(), 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glLoadIdentity()
        glLineWidth(2)
        interp_x = [value for value in range(1, self.width())]
        glColor3f(1,0,0)
        glBegin(GL_LINE_STRIP)
        for i in range(len(interp_x)):
            glVertex2f(interp_x[i], self.polinomial(interp_x[i]))
        glEnd()
        glPointSize(10)
        glEnable(GL_POINT_SMOOTH)
        glBegin(GL_POINTS)
        glColor3f(1,1,1)
        for point in self.int_points:
            glVertex2f(*point)
        glEnd()
        

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glOrtho(0, w, 0, h, -1.0, 1.0)
        glLoadIdentity()


    def mousePressEvent(self, event):
        on_pressed = event.pos()
        for index, point in enumerate(self.int_points):
            if not self.in_move and abs(point[0]-on_pressed.x()) < 5 and \
                    abs(point[1]-on_pressed.y()) < 5:
                self.focus_point = index
                self.in_move = True


    def mouseMoveEvent(self, event):
        if self.in_move:
            new_position = event.pos()
            self.int_points[self.focus_point] = [new_position.x(), new_position.y()]
            self.polinomial =  self.get_polynomial()
            self.update()


    def mouseReleaseEvent(self, *args, **kwargs):
        self.in_move = False
        self.focus_point = -1


    def get_polynomial(self):
        points_x = [point[0] for point in self.int_points]
        points_y = [point[1] for point in self.int_points]
        return lagrange(points_x, points_y)
