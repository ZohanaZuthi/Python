# join array
import numpy as np
# merging arrays
var=np.array([9,8,7,6])
var1=np.array([3,4,5,6])
# concatenate joins the elements through the column and make them into same row
var2=np.concatenate((var,var1))
print(var2)
var7=np.stack((var,var1))
print(var7)
# 2d
var3=np.array([[9,8],[7,6]])
var4=np.array([[3,4],[5,6]])
var5=np.concatenate((var3,var4),axis=1)
print(var5)
print(var5.shape)
var6=np.stack((var3,var4),axis=1)
print(var6)
print(var6.shape)
