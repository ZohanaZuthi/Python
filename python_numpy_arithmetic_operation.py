import numpy as np
var=np.array([1,2,3,4])
var2=var+3
print(var2)
var1=np.array([3,4,5,6])
var3=var+var1
print(var3)
print(np.add(var,var1))
print(np.subtract(var,var1))
print(np.multiply(var,var1))
print(np.divide(var,var1))
print(np.mod(var,var1))
print(np.power(var,var1))
print(np.reciprocal(var))
# 2 dimension
var4=np.array([[1,2,3,4],[5,6,7,8]])
var5=np.array([[5,2,2,4],[5,0,7,9]])
var6=np.add(var4,var5)
print(var6)
# max,min
print(np.min(var))
print(np.max(var))
print(np.min(var))
print(np.max(var))
# axis=0 through coloum and 1 for row
print(np.min(var4,axis=0))
print(np.max(var4,axis=1))
# position of max and min
print(np.argmin(var))
print(np.argmax(var))
print(np.sin(var))
print(np.cos(var))
print(np.sqrt(var))
# the first two number will be added and create 3rd elements
print(np.cumsum(var))
