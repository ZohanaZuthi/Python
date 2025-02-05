# list are used to store multiple items in a single variable. list are created using square bracket
# same as array.
# it has three data type=int,string,boolean
# list is ordered,changeable and allows duplicate
mylist=["kuku","pupu","tutu","thuthu","gugu","tutu"]
print(mylist)
print(mylist[:])
print(mylist[:3])
print(mylist[1:-2])
print(mylist[1:8:2])
# type of list <class 'list'>
print(type(mylist))
# length of list
print(len(mylist))
list1=["string",23,True,40,False]
list1.append(90)
list1.append("ear")
print(list1)
print(len(list1))
print(type(list1))
# printing list by using for loop
for i in list1:
    print(i)
if "kuku" in mylist:
    print("Yes")
else:
    print("No")
list2=[i for i in range(4)]    
print(list2)
list2.append(30)
print(list2)
print(list2.reverse())
list3=[3,56,3,78,12,4555]
print(list3.sort())
print(list3.sort(reverse=True))
m=list3
m[0]=12000
print(m)
print(list3)
n=list3.copy()
n[0]=12000
print(n)
print(list3)
list3.insert(1,30000)
# list2.extend(list3)
# print(list2.extend(list3))
# joining to list
k=list2+list3
print(k)
list4=["we","love","what","we","do","what"]
# deleting the first matching
list4.remove("what")
print(list4)
# to remove a specified index element we use pop()
list4.pop(1)
print(list4)
# to delete a list competely
del list4
# to clear a list contents
list3.clear()
print(list3)
list5=["abc","rbcd","bcab","wdar","ef"]
# sorting list alphanumerically
# this sort function is case sensitive resulting ia all uppercase letter before lower case letter
# to make case insesitive we can use key=str.lower
list5.sort()
print(list5)
list5.sort(key=str.lower)
print(list5)
# to sort in decending order
list5.sort(reverse=True)
print(list5)
# to reverse the order of a list items 
list5.reverse()
print(list5)
# for i in range(len(list5)):
#     print(list5[i])
i=0
# while i<len(list5):
#     print(list5[i])
#     i=i+1
# in short hand for loop
# [print(i) for i in list5]
# list coprehension = making list from existing list with some constraints
list6=[ i.upper() for i in list5 if "a" in i]
print(list6)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#sort the list according to the elements that are close to 50
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 20]
thislist.sort(key = myfunc)
print(thislist)
# to copy a list
list0=list4.copy()
# or
list0=list(list4)
