class person:
    def __init__(self,fname,fage):
        self.firstname=fname
        self.firstage=fage
    def __str__(self):
        return f"{self.firstname} ,{self.firstage}"
x=person("Nazifa",22)
print(x)
# creating a child class
class student(person):
    # pass
    # when you don't add init function the child class will inherit parent init
    # if you add init the child class no longer inherit parent init
    def __init__(self,name,age,year):
        # as the same init is in parent class and child class it called overrides
        # to keep the inheritance of the parent's init add a call to the parent init
        # person.__init__(self,name,age)
        # or python has another way of inheriting parent's class by using super()
        super().__init__(name,age)
        # while using super do not use self word
        self.firstyear=year
        def show(self):
            print("my name ",self.name,"my age ",self.age,"year ",self.year)
y=student("sara",15,23)
print(y)
        
