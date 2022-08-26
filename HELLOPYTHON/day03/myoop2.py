from day02.myfor04 import cnt
class LeeJY:
    def __init__(self):
        self.money = 10
    def phonepari(self):
        self.money += 5

class Byden:
    def __init__(self):
        self.cnt_war = 1
    def bubkyu(self,cnt):
        self.cnt_war += cnt

class HyungJ(LeeJY, Byden):
    def __init__(self):
        LeeJY.__init__(self)
        Byden.__init__(self)

hj = HyungJ()

print(hj.money)
print(hj.cnt_war)
hj.bubkyu(1)
hj.phonepari()
print(hj.money)
print(hj.cnt_war)

