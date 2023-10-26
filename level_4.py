# F-strings

name = "Pranshu"
age = 18
price = 98.385613874

print(f"Hello my name is {name} and my age is {age} and I will buy it for ${price:.2f}")

# Docstrings

def square(n):
    '''This is a doc string'''
    return n*n

print(square(5))
print(square.__doc__)

# Recurrsion

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
a = int(input("Enter Digits : "))
print("The fibonnaci series goes like : ", end="")
for i in range(0,a):
    print(fibonacci(i), end=", ")
print()
# Exception Handling

a = input("Enter Number : ")

try:
    if(a>0 or a<=0):
        print("Valid Input")
except Exception as e:
    print("Invalid Value")
finally:
    print("I am always executed")
    
# Custom Errors 

class CustomError(Exception):
    print("Custom Error Raised")
    pass

a = 0
try:
    if(a!=0):
        raise ValueError("Value is not 5")
except CustomError:
    pass