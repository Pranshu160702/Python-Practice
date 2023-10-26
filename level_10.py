# Static Methods -> Self is not used in argument and can be used same way

class Numbers:
    def __init__(self):
        print("Constructor")
        
    @staticmethod
    def square(z):
        return z*z
    
number = Numbers()
print(number.square(7))

# Instance variable means the variable values for a particular object/instance
# Class variable means value of a variable for all the objects created
# First priority is instance vairable, if it is not given than the default vairable is class variable

# We can also change class variable like this

class NewClass:
    company = "Microsoft" #class variable
    def __init__(self):
        pass
    
    @classmethod
    def changeCompany(cls, a): #cls is used conventionally describing a class
        cls.company = a
        
obj1 = NewClass()
print(obj1.company)
obj2 = NewClass()
obj2.changeCompany("Apple")
print(obj2.company)
print(obj1.company) # Class variable has changed

# A class method is also used as alternative or additional contructor

# dir
a = [1,2,3,4,5]
print(dir(a)) # List of all the attributes and methods available including dunder methods

# dict (For objects) returns a dictionary of attributes only
# help (For objects) returen descriptions of methods/functions only

class Person:
    def __init__(self):
        self.name = "Pranshu"
        self.age = 21
        self.profession = "Student"
    # self is used to access current class or any current instance
    def print_info(self):
        print(self.name + " is a " + str(self.age) + " years old " + self.profession)
        
a = Person() 
print(a.__dict__) # Gives a dictionary of all attributes
#print(help(a)) # Gives help for documentation of this object with methods and attributes

# Super keyword -> Used to call methods of parent class from child class

class A:
    def __init__(self, a, b):
        self.name = a
        self.lang = b
        
class B(A):
    def __init__(self,c ,d , e):
        # Calling parent classes init method
        super().__init__(c, d)
        self.id = e
        
object1 = B("ASDF", "GHY", 1)
print(object1.name)
print(object1.lang)
print(object1.id)

# Dunder or Magic Methods are called automatically
# __init__, __str__, __repr__ (if str is not available then repr is called)
# __call__ -> Object can become callable i.e can be passed as a function parameter
