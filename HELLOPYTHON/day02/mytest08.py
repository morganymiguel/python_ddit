import random

# arr4 = [1,2,3,4]
# arr=[]
# print(arr)
#
# a = arr4.pop(0)
# print("a",a)
# print(arr4)

# arr4 = [1,2,3,4]
# arr2 =[]
#
# print(arr4)
#
# a = arr4.pop(int(random.random()*len(arr4)))
# arr2.append(a)
# a = arr4.pop(int(random.random()*len(arr4)))
# arr2.append(a)
#
# print(arr2)


arr2 = [1,2,3,4,5,        6,7,8,9,10,
      11,12,13,14,15,   16,17,18,19,20,
      21,22,23,24,25,   26,27,28,29,30,
      31,32,33,34,35,   36,37,38,39,40,
      41,42,43,44,45
      ]
arr3 = []

a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
a = arr2.pop(int(random.random()*len(arr2)))
arr3.append(a)
print(arr3)
