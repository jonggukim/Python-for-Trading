'''
# GUI Tool : Pyqt 사용하기
--------------------------------------------
# Step 1.
import sys
from PyQt5.QtWidgets import *


# 윈도우 창 생성
app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()

# 위도우 창 안에 버튼 생성
button = QPushButton("Quit")
button.show()
app.exec_()
--------------------------------------------
# Step 2. :  QMainWinodw 생성하기.

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")              # windows name 설정하기
        self.setGeometry(300, 300, 300, 400)        # windows size 설정하기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


--------------------------------------------
# Step 3: 이벤트 추가 하기

import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)          # click 버튼 생성
        btn1.move(20, 20)                             # 버튼의 크기 지정
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):                           # 버튼 클릭시 응답창 생성
        QMessageBox.about(self, "message", "what are you doing    ??? "  ) # 응답창의 메시지 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
--------------------------------------------
# Step 4. :  QMainWinodw 생성하기.


import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btn1 = QPushButton("Login", self)                   # 버튼 생성 " Login "
        btn1.move(20, 20)                                   # 버튼의 크기 설정
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Check state", self)             # 버튼 생성 " Login "
        btn2.move(20, 70)                                   # 버튼의 크기 설정
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")

    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

--------------------------------------------

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)

    def OnEventConnect(self, ErrCode):
        if ErrCode == 0:
            self.statusBar().showMessage("로그인 성공")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()