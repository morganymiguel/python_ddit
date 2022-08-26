import random
from plotly.validators.layout.yaxis import _rangebreaks

arr = list(range(1,45+1))
arr2 =[]
while True:
    rnd = int(random.random()*45)
    if arr[rnd] != -99:
        arr2.append(arr[rnd])
        arr[rnd] = -99
        
    if (len(arr2) >= 7):
        break    
        
print(arr2)

arr4 = [1,2,3,4]
arr3 = []

while True:
    rnd = int(random.random()*4)
    if arr4[rnd] == -1:
        print("skip")
    else:
        arr3.append(arr4[rnd])
        arr4[rnd] = -1
        
    if len(arr3) >=2:
        break
print(arr3)