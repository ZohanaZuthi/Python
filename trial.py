a=input()
# a=int(a)
print(a)
# printing in the same line
print(3 + 4, 2 + 1)
# function writing methods
def sum(a,b):
    return a+b
sum(1,2)
def summation(a=2,b=9):
    return a+b
print(summation(6))
print(summation(7,8))
print(summation())
def sum_mation(*numbers):
    i=0
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
print(sum_mation(1,2,3,4,5))
 
    
     

   