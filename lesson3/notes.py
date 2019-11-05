# ============================================================================ #
# LESSON 3
# ============================================================================ #


# ============================================================================ #
# Analyzing inflamation data
# ============================================================================ #

# we'll need to use the numpy libiray, we import it like this:
import numpy


# ============================================================================ #
# flow control: looping
# ============================================================================ #

# what if we want to print each character of a string individually?
word = "lead"
print(word[0])
print(word[1])
print(word[2])
print(word[3]) # but not print(word[4])...!

# that would be terribly annoying, instead we can write:
for char in word:
    print(char)
    
# which will work for any string!
word = "oxygen"

for char in word:
    print(char)
    
# and we can do all kinds of useful things like:
vowels = "aeiou"
n = 0
for char in vowels:
    n = n + 1

print("There are", n, "vowels!")

# NOTE that the "looping variable" is just an ordinary variable
for k in [0,1,2,3,4]:
    print(k)
    
print("k =", k)

# a very often used pattern uses the range() function to construct a "range" of indicies
x = [1,2,4,8,16]

for k in range(len(x)):
    print("x[" + str(k) + "] =", x[k])

# ---------------------------------------------------------------------------- #
# a few notes about ranges...

# so a range can be visualized as kind of like a list:
print(list(range(4)))

# ranges follow the same conventions as slice indicies:
# range(first, last+1)
print(list(range(2, 5)))

# and "skipping" works the same as well
print(list(range(2, 9, 2)))

# ---------------------------------------------------------------------------- #
# enumerate is a bit more pythonic...
for k, item in enumerate(x):
    print("x[" + str(k) + "] =", item)

# ============================================================================ #
# Exercises
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# #1
# write a loop that calculates 5 ** 3 WITHOUT using the ** operator (and then print the result)

# #2
# write a loop that reverses the following string: (and then print the result)
name = "Newton"

# #3 given the following list, create a string from it's contents
chars = ["M","a","x","w","e","l","l"]


# ============================================================================ #
# Analyzing data from multiple files
# ============================================================================ #

# we're going to need the glob library for querying file paths
import glob
import numpy
from matplotlib import pyplot

# get a list of files that start with "inflammation" and have a ".csv" extension
filenames = sorted(glob.glob("./data/inflammation*.csv"))

# but we only want the first 3
filenames = filenames[0:3]

# "loop over" the files
for f in filenames:
    print(f)

    # load the data
    data = numpy.loadtxt(fname=f, delimiter=",")

    # create our 10x3" figure
    fig = pyplot.figure(figsize=(10.0, 3.0))

    # create our 3 axes
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # plot the daily mean, max, and min
    axes1.set_ylabel("average")
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel("max")
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel("min")
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    pyplot.show()
    
# ============================================================================ #
# Exercises
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# #1
# Plot the difference between the average inflammations reported in the first and
# second datasets (stored in inflammation-01.csv and inflammation-02.csv,
# correspondingly), i.e., the difference between the leftmost plots of the first
# two figures.

# ---------------------------------------------------------------------------- #
# #2
# Use each of the files once to generate a dataset containing values averaged over
# all patients:

filenames = glob.glob("inflammation*.csv")
composite_data = numpy.zeros((60,40))
for f in filenames:
    print(f)
    # sum each new file's data into composite_data as it's read
    #

# and then divide the composite_data by number of samples
composite_data /= len(filenames)

# Then use pyplot to generate average, max, and min for all patients

# ============================================================================ #
# Flow control: conditionals
# ============================================================================ #

# basic syntax
num = 37
if num > 100:
    print("greater")
else:
    print("not greater")

print("done")

# else is not required
num = 53
print("before conditional...")
if num > 100:
    print(num," is greater than 100")

print("...after conditional")

# we can also use elif...
num = -3

if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")
    
    
# and we can have compound statements
if (1 > 0) and (-1 > 0):
    print("both parts are true")
else:
    print("at least one part is false")
    
# also with "or"
if (1 < 0) or (-1 < 0):
    print("at least one test is true")
    
# also not
if not 1 > 0:
    print("really?")
else:
    print("whew...")
    
# truth beyond logicals
if "":
    print("empty string is true")
else:
    print("empty string is false")

if "word":
    print("word is true")
else:
    print("word is false")

if []:
    print("empty list is true")
else:
    print("empty list is false")

if [1, 2, 3]:
    print("non-empty list is true")
else:
    print("non-empty list is false")

if 0:
    print("zero is true")
else:
    print("zero is false")

if 1:
    print("one is true")
else:
    print("one is false")
    

# ============================================================================ #
# Exercises
# ============================================================================ #

# 1:

# HINTS:
# you can use the function / method startswith() to get if a string starts with
# a substring, as in:
print("String".startswith("Str"))

# or

print("String".startswith("str"))

# also, you can use the method append() to append an item to a list, as in:
x = [1,2,3]
print("x =", x)
x.append(4)
print("now x =", x)

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

def show_input(x):
    print("x =", x, "which is a", type(x))

# function definition syntax
def add(x, y):
    print("*"*5)
    print("add(x, y):", end=" ")
    print("x =", x, end=", ")
    print("y =", y)
    
    z = x + y
    print("z =", z)
    print("*"*5)
    
    return z

    
def sub(x, y):
    print("*"*5)
    print("sub(x, y):", end=" ")
    
    print("x =", x, end=", ")
    print("y =", y)
    
    z = x - y
    print("z =", z)
    print("*"*5)
    
    return z

    
def addsub(x, y, z):
    return sub(add(x, y), z)


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

        
def domap(f, iter):
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
    

# ---------------------------------------------------------------------------- #
import numpy
from matplotlib import pyplot

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
    

filenames = sorted(glob.glob('./data/inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    visualize(f)
# ---------------------------------------------------------------------------- #