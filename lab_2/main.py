# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui

import design

class GLInterface(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.onActivated)
        self.comboBox_2.activated[str].connect(self.onActivated_2)
        self.comboBox_3.activated[str].connect(self.onActivated_3)
        self.comboBox_4.activated[str].connect(self.onActivated_4)
        self.horizontalSlider.valueChanged.connect(self.valuechange)
        self.horizontalSlider_2.valueChanged.connect(self.valuechange_2)
        self.horizontalSlider_3.valueChanged.connect(self.valuechange_3)

    def onActivated(self, text):
        self.openGLWidget.changeFigure(text)
        # self.openGLWidget.updateGL()

    def onActivated_2(self, text):
        self.openGLWidget.changeTransparency(text)
        # self.openGLWidget.updateGL()

    def onActivated_3(self, text):
        self.openGLWidget.changeSfactor(text)
        # self.openGLWidget.updateGL()

    def onActivated_4(self, text):
        self.openGLWidget.changeDfactor(text)
        # self.openGLWidget.updateGL()

    def valuechange(self):
        self.openGLWidget.changeRef(self.horizontalSlider.value())
        # self.openGLWidget.updateGL()

    def valuechange_2(self):
        self.openGLWidget.changeX(self.horizontalSlider_2.value())
        # self.openGLWidget.updateGL()

    def valuechange_3(self):
        self.openGLWidget.changeY(self.horizontalSlider_3.value())
        # self.openGLWidget.updateGL()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = GLInterface()  # Создаём объект класса GLInterface
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()