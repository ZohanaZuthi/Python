# elif=else if
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#   shorthand if
print("A") if a > b else print("=") if a == b else print("B")
# to avoid getting any error pass
a = 33
b = 200

if b > a:
  pass
# we also have break and continue just like c++
for x in range(2, 6):
  print(x)
# incrementing with 3
for x in range(2, 30, 3):
  print(x)
