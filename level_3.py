# LISTS ARE
# MUTABLE
# ORDERED COLLECTION
# MULTIPLE DATATYPES
# SQUARE BRACKETS

list1 = [5,2,7,8,4,6,"P","R","A","N",True]
print(type(list1))
print(list1)
print(list1[6])
print(list1[2:9]) # Index starts with 0 , end is exclusive
print(list1[4:10:2]) # Jump / step = 2  

# List Comprehenssion
list2 = [i*i for i in range(1, 11) if i*i<100]
print(list2)

list1.append(6)
list1.remove(2)
list2.sort(reverse=True)
print(list1)
print(list2)
print(list1.index("R"))
print(list1.count(6))
list1.insert(1,900)
print(list1)
list2.extend(list1)
print(list2)
list3 = list1 + list2
print(list3)

# TUPLES ARE
# IMMUTABLE
# MULTIPLE DATATYPES
# PARENTHESIS

tuple1 = (1,7,3,8,2,2,2,2,"green",True)
print(tuple1[2])
print(tuple1.index(7))
print(tuple1.count(2))

#Sets

# Values not repeated
# Unordered

set1 = {2,4,5,8,2,4,"hello",False}
print(set1)

#Empty set 
set2 = set()
print(type(set2))
set2 = {}
print(type(set2))

s1 = {1,3,5,6,7,7,8,9}
s2 = {1,5,2,8,9,4,0}

print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1)

# There are many other methods of sets like intersection_update, symmetric_difference, difference
# isdisjoint, issuperset, issubset, remove, pop, del, clear, etc.

# Dictionaries

dict1 = {
    "Name" : "pranshu",
    "Age" : 21,
    1 : "Sakshi",
    2 : "Mishika",
    3 : "Parshu",
}

print(dict1)
print(dict1[1])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# For dictionary methods
# https://www.youtube.com/watch?v=LmbFwaLjT9k&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=34&ab_channel=CodeWithHarry