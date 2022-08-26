class Animal:
    def __init__(self):
        self.flagMove = True
    
    def die(self):
        self.flagMove = False

ani = Animal()
print(ani.flagMove)
ani.die()
print(ani.flagMove)

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_tool= 0
    def momstouch(self,stroke):
        self.skill_tool += stroke
        
hum = Human()
print(hum.skill_tool)
print(hum.flagMove)
hum.die()
hum.momstouch(5)
print(hum.skill_tool)
print(hum.flagMove)
print(hum.flagMove)

