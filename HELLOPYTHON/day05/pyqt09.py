import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt09.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        # self.leMine.returnPressed.connect(self.myclick)
    
    def drawStar(self,cnt):
        ret =""
        for i in range(cnt):
            ret+="*"
        ret +="\n"
        
        
    def myclick(self):
        str_f = self.le_first.text()
        str_l = self.le_last.text()
        
        istr_f = int(str_f)
        istr_l = int(str_l)
        
        txt = ""
        for i in range(istr_f, istr_l+1):
            txt += self.drawStar(i)
        
        self.te.setText(txt)
        
    
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
