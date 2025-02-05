# rand() produce numbers in between 0 to 1
import numpy as np
var=np.random.rand(4)
print(var)
# multidimension
var1=np.random.rand(2,5)
print(var1)
# randn() random numbers close to zero positive and negative
var2=np.random.randn(5)
print(var2)
# ranf() random numbers in between 0 to 1 including 0 and not included 1
var3=np.random.ranf(4)
print(var3)
# randint() generate random numbers in between a range given by users (min,max,total)
var5=np.random.randint(2,5,3)
print(var5)