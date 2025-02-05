import numpy as np
x=np.array([1,2,3,4])
print(x)
print(type(x))
print(x.ndim)
# to check dimension
y=[1,2,3,4]
print(y)
print(type(y))
# to convert list into array
k=np.array(y)
print(y)
# creating by using user input
l=[]
for i in range(1,5):
    n=int(input("enter: "))
    l.append(n)
np.array(l)
# 2d array
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.ndim)
# 3d array
arr=np.array([[[1,2,3,4],[5,6,7,8],[23,4,3,2]]])
print(arr)
print(arr.ndim)
# shortcut
ar3=np.array([1,2,3,4],ndmin=10)
print(ar3)