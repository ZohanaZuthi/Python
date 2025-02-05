# start:stop:step
import numpy as np
var=np.array([1,2,3,4,5,6,7])
#             0 1 2 3 4 5 6
#            -7-6-5-4-3-2-1
print(var)
print(var[1:5])
print(var[1:])
print(var[1:5:2])
print(var[:5])
print(var[::2])
# for 2 dimensional
var1=np.array([[1,2,3,4,5],[4,5,6,7,4],[3,4,7,8,9]])
print(var1)
print(var1[2,2::2])
