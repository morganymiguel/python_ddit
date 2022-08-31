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
        
    def myclick(self):
        firstStar =""
        lastStar = ""
        firstStar = self.le_first.text()
        lastStar = self.le_last.text() 
        result = ""
        ifirstStar = int(firstStar)
        ilastStar =int(lastStar)
        
        for i in range(ifirstStar):
            result = result + "*"
        
        print(firstStar)
        print(result)
        
        
        public void mycick() {
        String f = tf_first.getText();
        String l = tf_last.getText();
        String txt ="";
        int ff = Integer.parseInt(f);
        int ll = Integer.parseInt(l);
        for(int i = ff; i<=ll;i++) {
            txt += drawStar(i);
        }
        
        ta.setText(txt);
    }

    public String drawStar(int cnt) {
        String ret ="";
        for(int i = 0; i<cnt; i++) {
            ret += "*";
        }
        ret +="\n";
        return ret;
    }
        
    
        
#코드 실행시 GUI 창을 띄우는 부분
#__name__ == "__main__" : 모듈로 활용되는게 아니라 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
