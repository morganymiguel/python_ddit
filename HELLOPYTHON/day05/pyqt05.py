import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)
        
        
    def myclick(self):
        print("click")
        mine = self.leMine.text()
        print(mine)
        com =""
        result =""
        
        rnd = random.random()
        if rnd > 0.5:
            com = "홀"
        else:
            com ="짝"
        print("mine", mine)
        print("com",com)
        
        self.leCom.setText(com)
        
        
        if mine == com:
            print("승리")
            result="승리"
            self.leResult.setText(result)
        else:
            print("패배")
            result="패배"
            self.leResult.setText(result)
            
        
        
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()