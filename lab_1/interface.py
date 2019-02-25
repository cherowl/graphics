# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui

import design



class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.openGLWidget.changeFigure(text)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()





# class InterfaceOpenGL(QtWidgets.QMainWindow, design.Ui_TabWidget):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)  # Это нужно для инициализации нашего дизайна

#         self.btnDraw.clicked.connect(self.draw)
#         self.btnQuit.clicked.connect(self.close)

#     def draw(self):
#         print("DRAW")

#     def close(self):
#         pass
    

    
#     def addTab(self, ):
#         pass

# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = InterfaceOpenGL()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     sys.exit(app.exec_())  # и запускаем приложение


# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()