#홀/짝을 고르시오. 홀/짝
import random

# arr=["홀", "짝"]

myturn = input("홀/짝을 고르시오>> ")
rnd = int(random.random()*2+1)
if("홀" == myturn):
    turna = 1
elif("짝" ==myturn):
    turna = 2
com = rnd

print("나: {}, 컴: {}".format(turna,com))
if(com == turna):
    print("결과: 승리")
if(com !=turna):
    print("결과: 패배")


# 쌤풀이
import random
mine = input("홀/짝을 고르시오.")
com =""
result = ""

rnd = random.random()
if rnd > 0.5:
    com = "홀"
else :
    com = "짝"
if mine == com:
    result = "이김"
else: 
    result = "짐"
print("나: ",mine)
print("컴: ", com)
print("결과: ", result) 
