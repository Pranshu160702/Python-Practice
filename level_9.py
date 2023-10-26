# Object Oriented Programming
# Class is a blurprint & objects are its entities and functions/methods are actions to perform on entity

class Person:
    name = "Pranshu"
    age = 21
    profession = "Student"
    # self is used to access current class or any current instance
    def print_info(self):
        print(self.name + " is a " + str(self.age) + " years old " + self.profession)
        
a = Person()
a.print_info()

b = Person()
b.name = "Shubham"
b.profession = "Artist"
b.age = 20
b.print_info()

# Constructor (__init__(self))

class Form:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.occupation = c

    def print_info(self):
        print(self.name + " is " + str(self.age) + " years old and a " + self.occupation)

a = Form("Pranshu",100,"Legend")
a.print_info()
            
# Decorators -> Used to create a function that appiles some line of code before and after a function

def greet(func):
    def mfunc():
        print("****************")
        func()
        print("________________")
    return mfunc

@greet # Greet is the decorator function for hello function
def hello():
    print("Hello User!")

hello() # I have only called hello and not greet

# Getter -> @property
# Setter -> @anyfunc.setter 
# Getter & Setter both should have the same function name

class MyClass:
    def __init__(self, a):
        self.value = a
        
    def show_value(self):
        print(f"The Value is : {self.value}")
        
    @property
    def get_value(self):
        return self.value
    
    @get_value.setter
    def get_value(self, b):
        self.value = b*b*b
        
obj1 = MyClass(9)
obj1.show_value()
obj1.get_value = 5
print(obj1.get_value)

# Inheritance

class Father(Person):
    def hitPerson(self):
        print("Only Father can hit the person because person is child inherited from father")

father1 = Father()
father1.name = "Akhilesh"
father1.age = 40
father1.profession = "CS"
father1.print_info()
father1.hitPerson()

# By default everything is public access in python
# For private: we use double underscore ( _ _ ) 
# The private variables are still accessible but not directly
# protected access is conventitionally defined using single underscore ( _ ) eg. _age

class Access:
    def __init__(self):
        self.name = "Pranshu"
        self.age = 20
        self.__occupation = "Student"
        
access1 = Access()
print(access1.name + str(access1.age)) # Public
# print(access1.__occupation) # Private thats why not accesiible this way directly
print(access1._Access__occupation) # Private can be accessed using [ _Class__pvt ]
# This process of changing private's name to make it not directly accessible is called
# Name Mangling (Used to protect private class attributes)

print(access1.__dir__()) # List All attributes that can be accessed and their way of accessing