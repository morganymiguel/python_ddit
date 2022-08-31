import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        print("click")
        arr45  = [1,2,3,4,5,      6,7,8,9,10,
                  11,12,13,14,15, 16,17,18,19,20,
                  21,22,23,24,25, 26,27,28,29,30,
                  31,32,33,34,35, 36,37,38,39,40,
                  41,24,43,44,45]
        lotto = [0,0,0,0,0,0,0]
        for i in range(10000):
            rnd = int(random.random()*45)
            tempA = arr45[rnd]
            tempB = arr45[0]
            arr45[rnd] = tempB
            arr45[0] = tempA
        
        lotto[0] = arr45[0]
        lotto[1] = arr45[1]
        lotto[2] = arr45[2]
        lotto[3] = arr45[3]
        lotto[4] = arr45[4]
        lotto[5] = arr45[5]
        lotto[6] = arr45[6]
        
        for i in range(7):
            pass
        print("바보")
        self.le1.setText(str(lotto[0]))
        self.le2.setText(str(lotto[1]))
        self.le3.setText(str(lotto[2]))
        self.le4.setText(str(lotto[3]))
        self.le5.setText(str(lotto[4]))
        self.le6.setText(str(lotto[5]))
        self.le7.setText(str(lotto[6]))
        
            
        
        
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
