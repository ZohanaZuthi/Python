import numpy as np
var=np.array([1,2,3,4,5,6,7])
for i in var:
    print(i)
var1=np.array([[1,2,3,4,5],[4,5,6,7,4],[3,4,7,8,9]])
for i in var1:
    print(i)
for i in var1:
    for j in i:
        print(j)
var2=np.array([[[1,2,3,4,5],[4,5,6,7,4]]]) 
for i in var2:
    for j in i:
        for k in j:
            print(k)    
# shortcut:
for i in np.nditer(var2):
    print(i)  
# changing data type
for i in np.nditer(var2,flags=['buffered'],op_dtypes=["d"]):
    print(i)  
# iter with index
for i,d in np.ndenumerate(var2):
    print(i,d)  