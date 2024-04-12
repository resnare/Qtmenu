from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 1000, 750)
        self.setWindowTitle("Menu Program")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label !")
        self.label.move(50, 300)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click here")
        self.b1.move(100, 350)
        self.b1.setStyleSheet("background-color:yellow")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button.")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()



    win.show()
    sys.exit(app.exec())


window()
