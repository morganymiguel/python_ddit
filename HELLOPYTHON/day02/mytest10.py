import random
# 가위/바위/보
mine = input("안내면 진다 가위/바위/보>>")
com = ""
result = ""

rnd = int((random.random()*3)+1)

if rnd == 1:
    com="가위"
elif rnd ==2:
    com = "바위"
else:
    com = "보"

if mine == com:
    result ="비김"
if mine == "가위" and com =="바위":
    result = "짐"
elif mine == "가위" and com =="바위":
    result = "짐"
elif mine == "보" and com =="가위":
    result = "짐"
else:
    pass

if mine == "바위" and com =="가위":
    result = "이김"
elif mine == "보" and com =="바위":
    result = "이김"
elif mine == "가위" and com =="보":
    result = "이김"
else:
    pass

print("나:",mine)
print("컴:",com)
print("결과:",result)


#쌤풀이
mine = input("가위/바위/보")
com =""
result = ""

rnd = random.random()
if rnd > 0.66:
    com = "가위"
elif rnd >0.33:
    com = "바위"
else: 
    com = "보"

if com == "가위" and mine == "가위": result ="비김"
if com == "가위" and mine == "바위": result ="이김"
if com == "가위" and mine == "보": result ="짐"

if com == "바위" and mine == "가위": result ="짐"
if com == "바위" and mine == "바위": result ="비김"
if com == "바위" and mine == "보": result ="이김"

if com == "보" and mine == "가위": result ="이김"
if com == "보" and mine == "바위": result ="짐"
if com == "보" and mine == "보": result ="비김"



print("나: ",mine)
print("컴: ", com)
print("결과: ", result) 

