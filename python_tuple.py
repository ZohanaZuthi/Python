# tuple is immutable and ordered, allows duplicate
# to change a tuple we first have to change a tuple to a list
tuple1=("why","you","Bully","me")
list1=list(tuple1)
list1.append("?")
list1.pop(3)
list1[3]="her"
tuple1=tuple(list1)
print(tuple1)
tuple2=("stop","bullying")
# when two tuple is concatenate then another tuple gets created
tuple3=tuple1+tuple2
print(tuple3)
tuple4=(0,1,2,3,4,4,4,5,4,4)
countonum=tuple4.count(4)
print(countonum)
# first occurence index
# if the value is not present it will produce error
res=tuple4.index(4)
print(res)
# num,start,end
res1=tuple4.index(4,4,8)
print(res1)
res2=len(tuple4)
print(res2)
# to delete a tuple
del res2
# unpacking tuple
(a,*c,d)=tuple1
print(a)
print(d)
# by using asterisk the rest of the elements until another value are passed as list
print(c)
# to multiply the elements of tuple
tuple5=tuple1*2
print(tuple5)