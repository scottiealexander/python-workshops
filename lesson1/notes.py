# ============================================================================ #
# Ultra-introductory python nothes with lots of printing...
# ============================================================================ #


# ============================================================================ #
# VARIABLES
# ============================================================================ #

# ---------------------------------------------------------------------------- #
# integers

# assign value of 1 to "name" x
x = 1

# check the value via print
print("x =", x)

# check the type of x
type(x)

# we can reassign x to another value
x = 2
print("now x =", x)

# we can do somple math as well
x = 2 + 5
print("x =", x)

z = x + 3
print("z =", z)

# ---------------------------------------------------------------------------- #
# floats
y = 3.14
print("y =", y)
type(x)

# division always -> float
x = 2/1
print("x =", x)

# ---------------------------------------------------------------------------- #
# strings
s = "hello"
type(s)

# both single and double quotes work
s2 = 'world'
type(s2)

print(s, s2)

# ============================================================================ #
# LISTS
# ============================================================================ #

# lists are a series of comma seperated values enclosed in square brackets []
x = [1, 2, 3]
print(x)

# the 2 principal operations on lists: extract and insert

# ---------------------------------------------------------------------------- #
# extract
x[0]
x[1]
x[2]
#x[3] # -> error list index out of range

z = x[1]
print("z =", z)

# extract and modify
z = x[2] * 2
print("z =", z)

# doesn't change the value contained within x (in this case)
print("x[2] =", x[2])

# ---------------------------------------------------------------------------- #
# insert
x[2] = 4
print("x =", x)

x[1] = x[2] * 2
print("now x =", x)

# ---------------------------------------------------------------------------- #
# slicing

x = [1,2,3,4,5,6]
print("x =", x)

# we use the colon ':' to get a sub-list aka a slice
print("x[0:2] =", x[0:2])

# note, x[0:2] gives us [x[0], x[1]], so the syntax ~= <first>:(<last>+1)
print("x[2] =", x[2])

print("x[1:3] =", x[1:3])

# if we omit <first> it defaults to 0
print("x[:4] =", x[:4])

# if we omit <last>, is defaults to the last item
print("x[4:] =", x[4:])

# we can also uses slicing to insert
x[2:4] = [9, 16]
print("x =", x)

# we can also slice non-contiguous sections via : <first>:(<last>+1):<step>
print("x[1:6:2] =", x[1:6:2])

# ---------------------------------------------------------------------------- #
# concatenation
x = [1,2,3]
y = [4,5,6]
print("x =", x)
print("y =", y)

# hopefully this is pretty self-explanatory
print("x + y =", x + y)
print("x + y[:2] =", x + y[:2])

# ---------------------------------------------------------------------------- #
# repetition / duplication
print("x =", x)

xpx = x + x
print("xpx =", xpx)

# if x + x repeats x twice, then (by analogy) x * 2 should do the same thing...?
x2 = x * 2
print("x2 =", x2)

print("x * 3 =", x * 3)

# ============================================================================ #
# STRINGS
# ============================================================================ #

s = "hello world"
print("s =", s)

# strings behave like a list in many ways
print("s[0] =", s[0])
print("s[1] =", s[1])
print("s[-1] =", s[-1])
print("s[:5] =", s[:5])
print("s[6:] =", s[6:])

# but string cannot be modified
# s[0] = "f" # ERROR

# but you can reassign them
s = "f" + s[1:]
print("s =", s)

# ============================================================================ #
# LIST OF STRINGS
# ============================================================================ #

s = ["this","is","a","list"]
print("s =", s)

# slicing works as you might guess
print("s[1:3] =", s[1:3])

# we can't modify the strings, but we can modify the list
s[-1] = "list o' strings"
print("s =", s)

# can if a string is kind of like a list, a list of string is kind of like a
# list of lists...

# here we extract second word (s[1]) first letter (s[1][0])
c = s[1][0]
print("c =", c)

# ============================================================================ #
# FUNCTIONS
# ============================================================================ #

s = "hello world"

# we can use the len() function to get the length of a string
print("length of s:", len(s))

# and the type() function to get the "type" of anything
print("type of s:", type(s))

# len() also works on lists...
x = [1,2,3]

print("length of x:", len(x))

# note that we can "capture" the output of the len() function by assigning it
# to a new variable
y = len(x)
print("length of x:", y)

print("type of x:", type(x))

# again, type works on anything
print("type of 1:", type(1))
print("type of 3.14:", type(3.14))

# a few useful functions that operate on lists, max(), min(), sum(), sorted()
x = [6,3,7,9,2]
print("x =", x)
print("max(x) =", max(x))
print("min(x) =", min(x))
print("sum(x) =", sum(x))
print("sorted(x) =", sorted(x))

# you can convert between int, float, and strings using conversion functions:
# int(), float(), and str()
a = 3
print("str(a) =", str(a))
print("type(str(a)) =", type(str(a)))
