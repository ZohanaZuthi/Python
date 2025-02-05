# shortcut of function kind of
# lambda function is a small anonymous function
# lambda can take any number of arguments but can only return one expression
# def cube(x):
#     return x*x*x
cube=lambda x:x*x*x
print(cube(2))
# we can also pass a function into a lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))