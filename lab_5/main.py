# -*- coding: utf-8 -*-
import sys  # sys нужен для передачи argv в QApplication
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout) 

from controller import GLWidget


class GLInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.widget = GLWidget(self)
        main_layout = QGridLayout()
        main_layout.addWidget(self.widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Laboratory work #5")
        self.setFixedSize(620, 600)


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = GLInterface()  # Создаём объект класса GLInterface
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()