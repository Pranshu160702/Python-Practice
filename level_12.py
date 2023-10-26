# Important modules

import time

t = time.localtime()
formattime = time.strftime("%D-%H-%M-%S", t)
print(formattime)
# print(time.time())

import argparse

# Walrus operator ( := )

a = True
print(a:=False)

fruits = []
while((fruit := input("Enter Fruit : ")) != "quit"):
    fruits.append(fruit)
    
import shutil

shutil.copy("ZZZ.py","ZZZ_copy.py")
# shutil.copy2("ZZZ.py","ZZZ_copy.py") # Same function a little more clean
# shutil.copytree(folder_to_copy, newfoldername) used to copy an entire folder
# shutil.move(path, newpath) used to move file from one place to another
# shutil.rmtree(folderpath) # to remove folder

# request module is important for get and post !

# Generators : Generates Value on the fly and does not keep storing previous values

def myGenerator():
    for value in range(10):
        yield value
        
a = myGenerator()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# lru_cache : stores computed values so that computation does not need to be repeated
# Memoization : Means to store value in cache so that computation does not need to be repeated

from functools import lru_cache

@lru_cache(maxsize=None)
def func(n):
    time.sleep(2)
    return n*10

print(func(10))
print(func(7))
print(func(8))
print(func(10)) # Skips and gives direct computation
print(func(10)) # Skips and gives direct computation
print(func(4))