class Acamedy:
    def __init__(self):
        print("constructor")
        self.cnt_student = 0
    
    def openClass(self):
        self.cnt_student += 20
    
    def __del__(self):
        print("destoryer")
    
    def __str__(self):
        return "self.cnt_student:"+str(self.cnt_student)

if __name__ == '__main__':
    print()
    a = Acamedy()
    a.openClass()
    print(a)
    
