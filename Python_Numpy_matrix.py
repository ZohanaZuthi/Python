import numpy as np
var=np.matrix([[1,2,3],[1,3,5]])
var1=np.matrix([[1,2,3],[1,3,5]])
var2=np.matrix([[1,2],[1,3],[4,7]])
print(var)
print(type(var))
print(var+var1)
print(var-var1)
# for multiplicaation dot function
print(var.dot(var2))
# transpose
print(np.transpose(var))
print(var.T)
# swapaxes
print(np.swapaxes(var2,0,1))
# inverse matrix
var3=np.matrix([[1,2],[3,4]])
print(np.linalg.inv(var3))
# power
print(np.linalg.matrix_power(var3,-1))
# determinant
var4=np.matrix([[1,2,3],[1,3,5],[2,3,4]])
print(np.linalg.det(var4))

