# string in python is immutable
a="Harry Good Boy"
# following string creats another string but doesn't change the previous one
print(a.upper())
print(a.lower())
print(a.rstrip("r"))
# rstrip doesn't strip character in between or from the begining
# it only strips from the last
print(a.rstrip("y"))
print(a.replace("Harry","Jhon"))
print(a.split(" "))
print(a.split("o"))
# following capitalize make the first character uppercase and other in lowercase
print(a.capitalize())
# following center moving the string to the center
print(len(a))
print(len(a.center(50)))
print(a.count("y"))
# if the string ends with the character
print(a.endswith("???"))
print(a.startswith("H"))
# following if the string endswith the certain character.thw last digit should be the character's end point
print(a.endswith("Boy",4,14))
print(a.find("Boy"))
print(a.find("shut"))
# print(a.index("shut"))
print(a.isalpha())
print(a.isalnum())
# if there is any character which is not in lowercase the output will be false
print(a.islower())
# to see if the string contains space or tab
print(a.isspace())
b=" "
print(b.isspace())
# if the title contains first letter in uppercase
print(a.istitle())
print(a.swapcase())
c="den is not a guy"
print(c.title())

