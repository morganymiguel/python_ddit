dan = int(input("출력할 단수를 입력하시오>> "))

arr = range(1,9+1)

for i in arr:
    print("{}*{}={}".format(dan,i,(dan*i))) 

#쌤 풀이 소스를 보고 파악은 나랑 일하는 사람이 본다.
#상대방의 코드를 보고 왜 그렇게 짰을까를 생각해라.


print("{}*{}={}".format(dan,1,dan*1))
print("{}*{}={}".format(dan,2,dan*2))
print("{}*{}={}".format(dan,3,dan*3))
print("{}*{}={}".format(dan,4,dan*4))
print("{}*{}={}".format(dan,5,dan*5))
print("{}*{}={}".format(dan,6,dan*6))
print("{}*{}={}".format(dan,7,dan*7))
print("{}*{}={}".format(dan,8,dan*8))
print("{}*{}={}".format(dan,9,dan*9))