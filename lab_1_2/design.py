# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from controller import GLWidget

class Ui_GLInterface(object):
    def setupUi(self, GLInterface):
        GLInterface.setObjectName("GLInterface")
        GLInterface.resize(700, 600)

        self.centralwidget = QtWidgets.QWidget(GLInterface)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.openGLWidget = GLWidget(self)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout.addWidget(self.openGLWidget)
        GLInterface.setCentralWidget(self.centralwidget)

        self.retranslateUi(GLInterface)
        QtCore.QMetaObject.connectSlotsByName(GLInterface)

    def retranslateUi(self, GLInterface):
        _translate = QtCore.QCoreApplication.translate
        GLInterface.setWindowTitle(_translate("GLInterface", "Lab 1. Dobrohvalov (6303), Cherkasova (6382)"))

        self.comboBox.setItemText(0, _translate("GLInterface", "GL_POINT"))
        self.comboBox.setItemText(1, _translate("GLInterface", "GL_LINES"))
        self.comboBox.setItemText(2, _translate("GLInterface", "GL_LINE_STRIP"))
        self.comboBox.setItemText(3, _translate("GLInterface", "GL_LINE_LOOP"))
        self.comboBox.setItemText(4, _translate("GLInterface", "GL_TRIANGLES"))
        self.comboBox.setItemText(5, _translate("GLInterface", "GL_TRIANGLE_STRIP"))
        self.comboBox.setItemText(6, _translate("GLInterface", "GL_TRIANGLE_FAN"))
        self.comboBox.setItemText(7, _translate("GLInterface", "GL_QUADS"))
        self.comboBox.setItemText(8, _translate("GLInterface", "GL_QUAD_STRIP"))
        self.comboBox.setItemText(9, _translate("GLInterface", "GL_POLYGON"))
