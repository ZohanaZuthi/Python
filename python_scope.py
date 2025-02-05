# A variable is only available from inside the region it is created. This is called scope.
# ther are two scope: local scope,global scope
# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)
# by using global keyword we can classify that variable to global variable
def myfunc():
  global x
  x = 300

myfunc()

print(x)