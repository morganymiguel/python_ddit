import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb.clicked.connect(self.mycall)
        # self.leMine.returnPressed.connect(self.myclick)
        
    def mycall(self):
        print("clicked")
        str_tel = self.le.text()
        QMessageBox.about(self,'전화번호',str_tel)

        
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new)
        
        
        
        
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
