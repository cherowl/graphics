# -*- coding: utf-8 -*-
import sys  # sys нужен для передачи argv в QApplication
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout) 

from controller import GLWidget


class GLInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        self.label = QLabel("Magic value that only Maks knows:")
        self.value_holder = QSpinBox()
        self.value_holder.setRange(1 , 13)
        self.value_holder.setValue(5)
        self.widget = GLWidget(self)

        self.value_holder.valueChanged.connect(self.activate)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.value_holder)
        main_layout.addWidget(self.widget)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Laboratory work #3")
        self.setMinimumSize(self.widget.width, self.widget.height+100)


    def activate(self, value):
        self.value = value
        self.widget.change_depth(self.value)


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = GLInterface()  # Создаём объект класса GLInterface
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()