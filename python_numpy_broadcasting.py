import numpy as np
var=np.array([1,2,3,4])
var1=np.array([1,2,3])
# for broadcasting there are 2 conditions:
# the dimenseions should be same
# one of the dimensions should be one =new matrix will have max row and max column
var2=np.array([[1],[2],[3]])
var3=var+var2
print(var3) 
