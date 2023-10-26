# Import

import math # math is a module
# To get all the functions in a module
print(dir(math))

import customModule
from customModule import welcome as wlc

customModule.welcome()
wlc()

# https://www.youtube.com/watch?v=y_CX2Rvitk8&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=46&ab_channel=CodeWithHarry
# For explanation refer this link (if name = main)

# There is a file name main.py
# if(__name__="__main__"):
#     some_function()

# OS module

import os

if(not os.path.exists("dates")):
    os.mkdir("dates")

# for i in range(0,51):
#     os.mkdir(f"dates/Day{i}")
    # os.rename(f"dates/Day{i}", f"dates/Day {i} of Python")

# cur_dir = str(os.getcwd())

# folders = os.listdir(cur_dir + "/dates")
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"dates/{folder}"))
    
# Local Global Variable (Generally Avoided)

x = 5
print(x)
def rand_func():
    global x
    x = 10
    global y
    y = 7

rand_func()
print(x)
print(y)