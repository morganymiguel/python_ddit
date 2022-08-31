import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        print("click")
        vl = self.le.text()#값을 가져오는 메서드
        print("vl",vl)
        vl_new = int(vl) *2
        str(vl_new)
        self.le.setText(str(vl_new))
        
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
