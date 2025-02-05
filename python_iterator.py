# mylist=("apple","banana","orange")
# my=iter(mylist)
# print(next(my))
# print(next(my))
# print(next(my))
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
class iterkori:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a 
            self.a += 1
            return x
        else:
            raise StopIteration
        
first=iterkori()
mymy=iter(first)
print(next(mymy))
print(next(mymy))
