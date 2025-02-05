import numpy as np
var=np.array([[1,2],[2,1]])
print(var)
print()
# matrix row x column
print(var.shape)
var1=np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.shape)
# conversion of dimensions
# 1d to 2d
var2=np.array([1,2,3,4,5,6])
x=var2.reshape(3,2)
print(x)
# 1d to 3d
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1=var3.reshape(2,3,2)
print(x1)
var4=x1.reshape(-1)
print(var4)
var5=var.reshape(-1)
print(var5)