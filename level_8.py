# Lambda Functions : Small functions

cube = lambda x: x*x*x
print(cube(3))

avg = lambda x,y,z: (x+y+z)/3
print(avg(10,20,45))

x = 10
y = lambda x: x*x
print(y(x))

# Higher Order Functions : Map, Filter and Reduce

# map -> apply something to all things in a list

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(map(cube, list1))
print(list2)

# filter -> Returns the values of original list for which we get true in return

filter_func = lambda x: x>=5

list3 = list(filter(filter_func, list1))
print(list3)

# reduce -> Reduce to single value i.e repeats with the first arguments (2 or more) and the proceeds
# until it reaches to just one value answer

from functools import reduce

sum = reduce(lambda x,y: x+y, list1)
print(sum)

# is and ==

# List created different locations
a = [1,2,3]
b = [1,2,3]

print(a is b) # Location
print(a == b) # Value

# Constant stored same location
a = 10
b = 10

print(a is b) # Location
print(a == b) # Value