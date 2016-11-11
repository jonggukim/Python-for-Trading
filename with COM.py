import sys
from PyQt5.QtWidgets import *
'''
app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()
'''
'''
app = QApplication(sys.argv)
print(sys.argv)
button = QPushButton("Quit")
button.show()
app.exec_()
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

''' add from my laptop'''
# add information