class Acamedy:
    def __init__(self):
        print("constructor")
        self.cnt_student = 0
    
    def openClass(self):
        self.cnt_student += 20
    
    def __del__(self):
        print("destoryer")



Acamedy()