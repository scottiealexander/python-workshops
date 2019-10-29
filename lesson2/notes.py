# ============================================================================ #
# LESSON 2
# ============================================================================ #

# what we covered last time in brief:
#   1. data types
#       a. int: 1
#       b. float: 3.14
#       c. str: "this is a string"
#           * indexing: "foo"[1] -> "o"
#           * slicing: "hello world"[0:5] -> "hello"
#       d. list: [1,2,3]
#           * indexing: [1,2,3][1] -> 2
#           * slicing: [1,2,3,4][0:2] -> [1,2]
#   2. functions
#       a. len() -> get the length of a string or list
#       b. type() -> get the type of any python object
#       c. <various function that operate on lists>: sorted([3,1,2])

# ============================================================================ #
# Analyzing inflamation data
# ============================================================================ #

# we'll need to use the numpy libiray, we import it like this:
import numpy

# you will need to change this based on where your data is located
# datafile = "../data/inflammation-01.csv"

# load the data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

# ---------------------------------------------------------------------------- #
# numpy array basics

# <data> is a numpy ndarray
print(type(data))
print(data)

# unlike lists, numpy arrays can only contain items of the same data type
print(data.dtype)

# query the shape of our data (size of each dimention)
print(data.shape)

# ---------------------------------------------------------------------------- #
# numpy array indexing

# indexing works very similarly to lists, just with multiple dimentions
print("data[0,0] =", data[0,0])

# as does slicing
print(data[5:10, 0:10])

small = data[:3, 36:]
print("small is:")
print(small)

# ---------------------------------------------------------------------------- #
# numpy array math...

# unlike lists, numpy ndarrays behave more like math objects
print("small * 2:\n", small * 2)

# NOTE that [*, /, +, -] all operate element-wise
print("small * 2 + small:\n", small * 2 + small)

# ---------------------------------------------------------------------------- #
# array construction

# arrays sizes must be compatible for element-wise operations
x = np.array([[1,2,3],[4,5,6]])

# this is another way to create a 2d array...
y = np.array([1,1,2,2]).reshape(2,2)

# but note the order!
print("y =\n", y)

# ---------------------------------------------------------------------------- #
# broadcasting et al.

# this will cause an error...
x + y

z = np.array([1,1,1])

# this will not... what is numpy doing?
print("x =\n", x)
print("z =\n", z)
print("x + z =\n", x + z)

# ---------------------------------------------------------------------------- #
# numpy functions that operate on arrays

print(numpy.mean(data))

maxval, minval, stdval = numpy.max(data), numpy.min(data), numpy.std(data)

print("maximum inflammation:", maxval)
print("minimum inflammation:", minval)
print("standard deviation:", stdval)

# NOTE: that the above does not respect which data came from which patient, which
# is often important, how do we deal with that?
# recall that our data is DAY x PATIENT

# method 1: one patient at a time
patient0 = data[0,:]
print("Max for patient 0 =", numpy.max(patient0))

print("Max for patient 2 =", numpy.max(data[2,:]))

# method 2: all patients at once (max within patient / across days)
patient_max = numpy.max(data, axis=1)

# this works for min, mean, std as well
patient_mean = numpy.mean(data, axis=1)
print("mean across axis 1:\n", patient_mean)

# or, we can average within day (across patients)
day_mean = numpy.mean(data, axis=0)
print("mean across axis 0:\n", day_mean)

# ============================================================================ #
# Visualizations
# ============================================================================ #

# first, we need to load the plotting library
from matplotlib import pyplot

# display data as an image
image = pyplot.imshow(data)

# but we need to "show()" to actually see the figure
pyplot.show()

# we can also plot some of the summaries that we calculated above
pyplot.plot(day_mean)
pyplot.show()

# or some others, such as daily maximum and minimum
pyplot.plot(numpy.max(data, axis=0))
pyplot.show()

pyplot.plot(numpy.min(data, axis=0))
pyplot.show()


# ---------------------------------------------------------------------------- #
# subplots

# create a figure that is 10" wide by 3" tall
fig = pyplot.figure(figsize=(10.0, 3.0))

# add three subplots, arguments are (nrow, ncol, index)
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

# plot daily mean in first plot
axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

# plot daily max in second
axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

# plot daily min in third
axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

# make it look a little nicer
fig.tight_layout()

# show!
pyplot.show()

# ============================================================================ #
# Exercises
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# #1
first, second = 'Grace', 'Hopper'
third, fourth = second, first

# what will this print?
print(third, forth)

# ---------------------------------------------------------------------------- #
# #2
x = "hello"
y = x[3:3]

# what will this print?
print("y =", y)

# what about this?
print("data[3:3,:] =", data[3:3,:])

# ---------------------------------------------------------------------------- #
# #3
# make a plot of the daily variability (standard deviation)

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
filenames = sorted(glob.glob('../data/inflammation*.csv'))

# but we only want the first 3
filenames = filenames[0:3]

# "loop over" the files
for f in filenames:
    print(f)

    # load the data
    data = numpy.loadtxt(fname=f, delimiter=',')

    # create our 10x3" figure
    fig = pyplot.figure(figsize=(10.0, 3.0))

    # create our 3 axes
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # plot the daily mean, max, and min
    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
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

filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))
for f in filenames:
    # sum each new file's data into composite_data as it's read
    #

# and then divide the composite_data by number of samples
composite_data /= len(filenames)

# Then use pyplot to generate average, max, and min for all patients