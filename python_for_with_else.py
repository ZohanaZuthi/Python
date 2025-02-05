for i in range(5):
    print(i)
else:
    print("loop ended")
for i in []:
    print(i)
else:
    print("loop ended")
    
for i in range(5):
    print(i)
    if(i==3):
         break
    #  here else statement won't be executed as the loop is not ended but broken
else:
    print("loop ended")
# else can be used with other loops
i=0
while(i<3):
    print(i)
    i=i+1
else:
    print("Loop ended")
    
   