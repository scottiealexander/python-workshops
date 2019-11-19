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
# PART I: scope
x = 99
y = 88

# ------------------------------------ #
def test1(x):
    y = 2
    print("In test1, x =", x)
    print("In test1, y =", y)

# ------------------------------------ #

test1(1)

# note that we did not change the value of x and y outside of the function
print("In base, x =", x)
print("In base, y =", y)

z = 77

# ------------------------------------ #
def test2(x):
    y = 2
    print("In test2, x =", x)
    print("In test2, y =", y)
    
    # note, z is not defined in the function, what will happen?
    print("In test2, z =", z)

# ------------------------------------ #

test2(1)

# note that return statements matter!
# ------------------------------------ #
def add_print(x, y):
    print(x + y)

# ------------------------------------ #
def add_return(x, y):
    return x + y

# ------------------------------------ #

# they appear to be identical...
add_print(1, 2)
add_return(1, 2)

# but when you actually "capture" the output they are not
output1 = add_print(3, 4)
output2 = add_return(3, 4)

print("output1 =", output1)
print("output2 =", output2)

# note that passing the output directly to another function has an analogous
# effect
print("5 + 6 =", add_print(5, 6))
print("5 + 6 =", add_return(5, 6))

# ---------------------------------------------------------------------------- #
# PART II: syntax

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
    return helpers.show_func(sub, ["x", "y"], [x, y])


def show_add(x, y):
    return helpers.show_func(add, ["x", "y"], [x, y])


def show_addsub(x, y, z):
    return show_sub(show_add(x, y), z)

# ---------------------------------------------------------------------------- #
# more complex syntax

# default arguments
def sum_iter(itr, start=0):
    total = start
    for item in itr:
        total += item
        
    return total


sum_iter([1,2,3])
sum_iter([1,2,3], 0)
sum_iter([1,2,3], start=0)

sum_iter(["Hello", "World"], start="")


# multiple positional args:
def sum_args(*args, start=0):
    total = start
    for item in args:
        total += item
    
    return total


sum_args(1, 2, 3, 4)
sum_args(1, 2, 3, 4, start=10)
sum_args("This","Is","A","String", start="")


# functions are "first class"
def foreach(f, itr):
    for item in itr:
        f(item)


foreach(print, [1, 2, 3, 4])


def doeach(f, itr):
    l = list()
    for item in itr:
        l.append(f(item))
    
    return l

doeach(str, [1, 2, 3])

# function annotation
def my_function(input1, input2):
    """my_function(input1, input2)
    calculates the foo of bar and then squares it
    """
    return 1


# ============================================================================ #
# EXERCISES
# ============================================================================ #
# 1. write a function named fence() that takes 2 arguments (strings) and returns
# a string that is the first string "flanked" by the second string, so:
# fence("name", "*") -> "*name*"

# 2. write a function rescale() that takes a numpy array as input and rescales
# each element to lie between 0.0 and 1.0 (make sure to test your
# implementation to make sure it's correct)

# 3. change your implementation of rescale() from above to take a lower and an
# upper limit as optional arguments (default to 0.0 and 1.0 respectivly) and
# have the function rescale the input array to lie between lower and upper
# don't forget to test it!

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
