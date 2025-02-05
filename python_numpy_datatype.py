import numpy as np
var=np.array([1.9,2,3,4,5])
print(var.dtype)
var1=np.array(['w','d','d'])
print(var1.dtype)
var2=np.array([1.9,2.8,3,4,5,'d','k','e'])
print(var2.dtype)
# conversion of datatype
var3=np.array([1,2,3,4,5],dtype=np.int8)
print(var3)
print(var3.dtype)
# some characters represents datatype
var4=np.array([1.9,2.8,3,4,5],dtype="f")
print(var4)
print(var4.dtype)
# we can convert using function
var5=np.int32(var)
var6=np.float_(var5)
print(var5.dtype)
print(var6.dtype)
print(var6)
var7=var.astype(int)
print(var7)