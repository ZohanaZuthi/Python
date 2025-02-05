import numpy as np
# search
arr=np.array([1,6,3,4,3,6,4])
x=np.where(arr==4)
print(x)
y=np.where((arr%2)==0)
print(y)
# to put a number in sorted position ,searchsorted just tells the position
x1=np.searchsorted(arr,0)
print(x1)
y1=np.searchsorted(arr,7)
print(y1)
print(arr)
x2=np.searchsorted(arr,[4,2,3])
print(x2)
x3=np.searchsorted(arr,[4,2,3],side="right")
print(x3)
# sorting array
print(np.sort(arr))
var=np.array(["apple","tormuj","banana","angur"])
print(np.sort(var))
# 2d
var2=np.array([[9,8],[7,6],[9,0]])
print(np.sort(var2))
# filter=new array with desitre elements from old array
f=[True,False,True,False]
var3=var[f]
print(var3)
