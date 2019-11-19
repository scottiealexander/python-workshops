# ============================================================================ #
# LESSON 4
# ============================================================================ #


# ============================================================================ #
# A brief recap from lesson 3
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# FOR LOOPS: 3 common patterns
x = [1,2,3,4]
for item in x:
    print(item)

print()
    
for k in range(len(x)):
    print("x[" + str(k) + "] =", x[k])

print()

for k, item in enumerate(x):
    print("x[" + str(k) + "] =", item)

print()

# ---------------------------------------------------------------------------- #
# CONDITIONALS
if 1 > 2:
    print("Really? That can't be right...")
elif 1 == 2:
    print("Well that's not right either")
else:
    print("Yep, 1 is still NOT > 2")
    
print()

# ---------------------------------------------------------------------------- #
# a complicated example that illustrates many useful operations
import time

now = time.localtime()

# hour of the day: 0-23
hour = int(time.strftime("%H", now))

# day of the week, 0=Sunday, 6=Saturday
day = int(time.strftime("%w", now))

# name of the day of the week
day_string = time.strftime("%A", now)


if hour < 6 and (day == 0 or day == 6):
    # it's before 6am on Saturday or Sunday
    print("Why on earth are you up so early on a weekend?")

elif hour > 23 and day < 5:
    # it's after 11pm on Sunday-Thursday night
    print("Shouldn't you be getting to sleep? You have to work tomorrow...")

elif (hour > 9 and hour < 17) and (day > 0 and day < 6):
    # it between 9am and 5pm on a week day
    print("Really, shouldn't you be working?")

else:
    print("Today is", day_string, "and the time is between", hour, "and", hour + 1)

# ---------------------------------------------------------------------------- #
# PROBLEM:
# sort the following list of files into small files, larger files, and other files
# small files have names that begin with "small", large file names begin with
# "inflammation" all other files are "others"


# Use the following Python code as your starting point:

files = ['inflammation-01.csv',
         'myscript.py',
         'inflammation-02.csv',
         'small-01.csv',
         'small-02.csv']
large_files = []
small_files = []
other_files = []

# Your solution should:

# loop over the names of the files
# figure out which group each filename belongs to
# append the filename to that list

# ============================================================================ #
# FUNCTIONS
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# PREAMBLE
import sys, os

lesson4_dir = "<PUT_YOUR_PATH_HERE>/python-workshops/lesson4"

if os.path.isdir(lesson4_dir):
    if not (lesson4_dir in sys.path):
        sys.path.append(lesson4_dir)
else:
    print("[ERROR]:", lesson4_dir, "is not a valid directory")

import helpers

# ---------------------------------------------------------------------------- #
# function definition syntax examples
def add(x, y):
    z = x + y
    return z
    
def sub(x, y):
    z = x - y
    return z
    
def addsub(x, y, z):
    return sub(add(x, y), z)
    
# ---------------------------------------------------------------------------- #
# helper fuctions to inspect what is happending
def show_sub(x, y):
    return show_func(sub, ["x", "y"], [x, y])
    
def show_add(x, y):
    return show_func(add, ["x", "y"], [x, y])
    
def show_addsub(x, y, z):
    res = show_add(x, y)
    return show_sub(res, z)

# ---------------------------------------------------------------------------- #
# more complex syntax

# default arguments
def sum_iter(iter, start=0):
    total = start
    for item in iter:
        total += item
        
    return total
    
# multiple positional args:
def sum_vars(*args, start=0):
    total = start
    for item in args:
        total += item
    
    return total

# functions are "first class"
def foreach(f, iter):
    for item in iter:
        f(item)

        
def doeach(f, iter):
    l = list()
    for item in iter:
        l.append(f(item))
    
    return l
        

# function annotation
def my_function(input1, input2):
    """my_function(input1, input2)
    calculates the foo of bar and then squares it
    """
    return 1
    

# ============================================================================ #
# Plotting inflammation data via a function
# ============================================================================ #

import numpy, glob
from matplotlib import pyplot

# ---------------------------------------------------------------------------- #
def visualize(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    pyplot.show()
# ---------------------------------------------------------------------------- #

filenames = sorted(glob.glob('./data/inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    visualize(f)
