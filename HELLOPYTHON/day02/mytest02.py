a = int(input("첫번째 수를 입력하시오>> "))
b = int(input("둘번째 수를 입력하시오>> "))
sum = 0
for i in range(a, b+1):
    sum += i
    
print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))
