import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le.returnPressed.connect(self.myclick)
        self.com = ""
        self.setComRandom()
        
    def setComRandom(self):
        arr9 =['1','2','3','4','5',     '6','7','8','9']
        for i in range(10000):
            rnd = (int)(random.random()*9)
            a = arr9[0]
            b = arr9[rnd]
            arr9[0] = b
            arr9[rnd] = a
        self.com = arr9[0]+arr9[1]+arr9[2]
        print(arr9)
        print(self.com)
        
    
    def getBall(self,com,mine):
        cnt = 0
        if com[0:1] == mine[1:2] or com[0:1] == mine[2:3]:
            cnt += 1
        if com[1:2] == mine[0:1] or com[1:2] == mine[2:3]:
            cnt += 1
        if com[2:3] == mine[1:2] or com[2:3] == mine[0:1]:
            cnt += 1
        return cnt
        
    def getStrike(self,com,mine):
        cnt = 0
        if com[0:1] == mine[0:1]:
            cnt += 1
        if com[1:2] == mine[1:2]:
            cnt += 1
        if com[2:3] == mine[2:3]:
            cnt += 1
        
        return cnt
        
    def myclick(self):
        print("click")
        mine = self.le.text()
        int_s = self.getStrike(self.com, mine)
        int_b = self.getBall(self.com,mine)
        str_old = self.te.toPlainText()
        self.te.setText("{}{}-{}S{}B\n".format(str_old,mine,int_s,int_b))
        self.le.setText("")
        
        if int_s ==3:
            QMessageBox.about(self,"야구게임","당신이 이겼습니다.")
        
        
    

#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
