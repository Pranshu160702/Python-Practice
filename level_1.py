# IN PYTHON EVERYTHING IS AN OBJECT *** VARIABLES, DATATYPES, ETC. EVERYTHING

print("Hello World")
print(10)
print("Hello",6,"Hehehe")
print(5*5)

# This is not part of the code
'''
Not even these
2 lines
'''
print("Move Down\nMove Up")
print("This also \"Works\"")
print(5,10,15,20, sep=" + ", end=" = Total : 50 ")
print("Done")

a = 100
b = "Pranshu"
c = True
d = 1.12
e = None
f = complex(9,3)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Some more datatypes include lists, tuples and dictionaries

# Strings are immutable
string_var = "this Is a senTENCe!!!!"

# Slicing 
print(string_var[0:5]) # end is exclusive and start is inclusive
print(string_var[:4])
print(string_var[10:])
print(string_var[:-7])

# Methods
print(string_var.lower())
print(string_var.upper())
print(string_var.rstrip("!"))
print(string_var.replace("sentence","string"))
print(string_var.split(" "))
print(string_var.capitalize())
print(len(string_var))
print(len(string_var.center(50)))
print(string_var.count("i"))
print(string_var.find("senTence"))
print(string_var.swapcase())
print(string_var.startswith("this"))