# python is an object-oriented programing language
# class is like a blueprint for creating object
# calling a class with class word
# class zuthi:
#     x=5
# d=zuthi()
# a=d.x
# print(a)
# every class has __init()__function and it gets called automatically when an object is created
# it assigns value for name and age
class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}-{self.age}"
    def myfunc(self):
        print("Hello I'm "+self.name)
p=myclass("zuthi",22)
print(p)
print(p.name)
print(p.age)
p.myfunc()
# self parameter is a reference to the current instance of the class and use to access the variable to the class
# it is the first parameter of the function can be named anything besides self
p.age=32
# updating
# deleting object properties
del p.age
del p
# class defination can not be empty, so when we really need to keep them empty w can use pass
class what():
    pass