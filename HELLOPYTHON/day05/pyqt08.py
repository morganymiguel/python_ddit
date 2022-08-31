import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        # self.leMine.returnPressed.connect(self.myclick)
        


        
    def myclick(self):
        print("click")
        rnd = random.random()
        mine = ""
        com=""
        result = ""
        mine = self.le_mine.text()
        if(rnd>0.66):
            com = "가위"
        elif(rnd>0.33):
            com ="바위"
        else:
            com = "보"
        
        if(mine =="가위" and com =="가위"):
            result ="무승부"
        if(mine =="가위" and com =="바위"):
            result ="패배"        
        if(mine =="가위" and com =="보"):
            result ="승리"        

        if(mine =="바위" and com =="가위"):
            result ="승리"
        if(mine =="바위" and com =="바위"):
            result ="무승부"        
        if(mine =="바위" and com =="보"):
            result ="패배"        

        if(mine =="보" and com =="가위"):
            result ="패배"
        if(mine =="보" and com =="바위"):
            result ="승리"        
        if(mine =="보" and com =="보"):
            result ="무승부"        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
