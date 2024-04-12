from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
import json
import os


class MyWindow(QMainWindow):

	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(500, 200, 1000, 750)
		self.setWindowTitle("Arduino Prog")
		self.initUI()

	def initUI(self):
		self.b1 = QPushButton(self)
		self.b1.setText("1")
		self.b1.move(100, 350)
		self.b1.clicked.connect(self.clicked)

		self.b2 = QPushButton(self)
		self.b2.setText("2")
		self.b2.move(400, 350)
		self.b2.clicked.connect(self.clicked)

		self.b3 = QPushButton(self)
		self.b3.setText("3")
		self.b3.move(700, 350)
		self.b3.clicked.connect(self.clicked)
		a =1
		while a == 1:
			json_file_path1 = os.path.join(r"E:\metakod\qtbutton\1.json")
			with open(json_file_path1, "r") as data1:
				dosya_1 = json.load(data1)
			if dosya_1["status"] == True:
				self.b1.setStyleSheet("background-color:green")
			else:
				self.b1.setStyleSheet("background-color:red")

			json_file_path2 = os.path.join(r"E:\metakod\qtbutton\2.json")
			with open(json_file_path2, "r") as data2:
				dosya_2 = json.load(data2)
			if dosya_2["status"] == True:
				self.b2.setStyleSheet("background-color:green")
			else:
				self.b2.setStyleSheet("background-color:red")

			json_file_path3 = os.path.join(r"E:\metakod\qtbutton\3.json")
			with open(json_file_path3, "r") as data3:
				dosya_3 = json.load(data3)
			if dosya_3["status"] == True:
				self.b3.setStyleSheet("background-color:green")
			else:
				self.b3.setStyleSheet("background-color:red")
				return a == 0

	def clicked(self):
		print("you clicked")
		return a == 1

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec())


#if __name__ == "__main__":
window()
