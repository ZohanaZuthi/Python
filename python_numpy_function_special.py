import numpy as np
var=np.array([1,4 ,3,4,5,6,7])
np.random.shuffle(var)
print(var)
var1=np.unique(var)
print(var1)
var2=np.unique(var,return_index=True,return_counts=True)
print(var2)
var3=np.resize(var,(2,3))
print(var3)
# order C=ROW MAJOR,F=COLUMN MAJOR,A=FLAT row MAJOR,K=ACCORDING TO MEMORY FLATTEN
print(var3.flatten('A'))
print(np.ravel(var3))