# In general python takes string as input. so you have to typecast other input type
num=int(input("Enter a number: "))
# print(num)
# taking multiple values at a time
a,b,c=input("Enter three values= ").split()
print(a,b,c)
# by using format method
name,position= input("Enter your name and where you live ").split()
letter="My name is {} and I live in {}."
print(letter.format(name,position))
letter1=("Secondly My name is {positon} and I live in {name}")
print(letter1)
print(type(f"{2 * 30}"))
# using f-string
salary=92.49999
letter3=f"I want {salary} this much salary"
print(letter3)
x=list(int(input("Enter multiple numbers:").split()))
print("List of students: ",x)