import numpy as np
# all elements 0
arr=np.zeros(4)
print(arr)
# all element 0 and also multi dimensional(dimension,elements)
arr1=np.zeros((3,4))
print(arr1)
# all elements are 1
arr2=np.ones((4,2))
print(arr2)
arr3=np.ones(4)
print(arr3)
# empty array
# previous memory will be shown
arr4=np.empty(4)
print(arr4)
# an array with a range of elements
arr5=np.arange(4)
print(arr5)
# diagonal element is 1
arr6=np.eye(3)
print(arr6)
arr7=np.eye(3,5)
print(arr7)
# lins pace
arr8=np.linspace(1,10,num=5)
print(arr8)