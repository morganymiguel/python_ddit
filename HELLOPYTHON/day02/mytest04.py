import random
arr = []

for i in range(0, 6):
    rnd = int((random.random()*45+1))
    
    arr.append(rnd)

print(arr)
   
arr2=[1,2,3,4,5]
for i in range(1000):
    rnd = int((random.random()*5))
    a = arr2[0]
    b = arr2[rnd]
    arr2[0] =b
    arr2[rnd] = a
print(arr2)