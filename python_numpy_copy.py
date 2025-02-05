# copy vs view
import numpy as np
var=np.array([1,2,3,4])
var1=var.copy()
var[1]=40
print(var1)
print(var)
var2=var.view()
var[1]=44
print(var2)
print(var)
# copy creates new array and copys the elements but view takes the original elements or arrays