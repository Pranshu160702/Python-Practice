#Conditional Operators : >,<,>=,<=,==,!=

# a = int(input("Enter Age : "))
# b = str(input("Enter Gender : "))

a = 5
b = "M"

# In python && = and and // = or keyword

if(a>5 and b=="M"):
    print("Big Boy")
elif(a==5):
    if(b=="M"):
        print("Medium Boy")
    else:
        print("Female")
else:
    print("Small Boy")
    
# match a:
#     case 0:
#         print("Zero")
#     case 1:
#         print("One")
#     case _:
#         print("Default / Empty Case")

#loops

for i in range(1,6):
    print(i)

name = "PRANSHU"
for letter in name:
    print(letter, end=" ... ")
print() 

i = 1
while(i<=3):
    print(i, end=" + ")
    i += 1
else:
    print(" = ", 1+2+3)

# Break and continue

for i in range(0,10):
    if(i == 5):
        break
    if(i == 2):
        print("Skip", end=" , ")
        continue
    print(i, end=" , ")
print()

# for else loop

for i in range(5):
    print("Loop")
else:
    print("Else Execution")

# Functions

def addNo(a = 10, b = 20):
    c = a + b 
    print(a, " + ", b, " = ", c)
    return c

def subNo(a, b):
    pass # Means we will write the code of this function later on ... Empty Function

addNo()         #Default Arg
addNo(b = 5)    #Keyword Arg
ans = addNo(5,4)      #User Input Arg
print("Returned Value = " , ans)

def function1(*tuplename):
    pass
    
def function2(listname):
    pass

def function3(**dictname):
    pass