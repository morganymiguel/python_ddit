import random
arr = []

for i in range(0, 6):
    rnd = int((random.random()*45+1))
    
    arr.append(rnd)

print(arr)
   
arr2= list(range(1,45+1))
for i in range(1000):
    rnd = int((random.random()*45))
    a = arr2[0]
    b = arr2[rnd]
    arr2[0] =b
    arr2[rnd] = a
print(arr2)