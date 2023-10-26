# Method Overriding
# Same function name area in two different classes but perform different tasks

class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.breadth = b
        
    def area(self):
        return self.length * self.breadth
  
class Circle:
    def __init__(self, a):
        self.radius = a
        
    def area(self):
        return 3.14 * 2 * self.radius
    
rect1 = Rectangle(10,15)
print(rect1.area())
cir1 = Circle(9)
print(cir1.area())

# Operator Overloading : When an operator is overloaded with your function
# + is overloaded using __add__ method , - is overloaded using __sub__

# Multiple Inheritance

class A:
    def __init__(self, a, b):
        self.name = a
        self.lang = b
        
    def shownl(self):
        print(f"Name is {self.name} and language is {self.lang}")
    
class B:
    def __init__(self,c):
        # Calling parent classes init method
        self.id = c
        
    def showid(self):
        print(f"Id is {self.id}")
        
# The order of classes matter if method overriding : Ab(A, B) and Ab(B, A) are different
class Ab(B,A):
    def __init__(self, a, b, c):
        self.id = a
        self.name = b
        self.lang = c

obj1 = Ab(1, "Pranshu", "English")
obj1.showid()
obj1.shownl()

# Multilevel Inheritance 
# Basically when more child classes are derived from a child class thats multilevel
# https://www.youtube.com/watch?v=Il7XMJJeXiA&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=80&ab_channel=CodeWithHarry
# Refer this video if needed

# Hybrid Inheritance : Combination of simple, multiple and multilevel inheritance

# Hierarichal Inheritance -> Multiple child class from single parent class