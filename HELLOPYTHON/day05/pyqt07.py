import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        # self.leMine.returnPressed.connect(self.myclick)
        
    def myclick(self):
        dan = self.le.text()
        print(dan)
        idan = int(dan)
        val=""
        result =[0,0,0,0,0,0,0,0,0]
        print(result)
        for i in range(1, 9+1):
            result[i-1] = idan * i
        print(result)
        print(val+dan)
        dan1 = str(result[0])
        dan2 = str(result[1])
        dan3 = str(result[2])
        dan4 = str(result[3])
        dan5 = str(result[4])
        dan6 = str(result[5])
        dan7 = str(result[6])
        dan8 = str(result[7])
        dan9 = str(result[8])
    
        val = val + dan +" * 1"+  + " = "+dan1+ swappedString
        val = val + dan +" * 2"+  + " = "+dan2+ swappedString
        val = val + dan +" * 3"+  + " = "+dan3+ swappedString
        val = val + dan +" * 4"+  + " = "+dan4+ swappedString
        val = val + dan +" * 5"+  + " = "+dan5+ swappedString
        val = val + dan +" * 6"+  + " = "+dan6+ swappedString
        val = val + dan +" * 7"+  + " = "+dan7+ swappedString
        val = val + dan +" * 8"+  + " = "+dan8+ swappedString
        val = val + dan +" * 9"+  + " = "+dan9+ swappedString
            
        print(val)   
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
