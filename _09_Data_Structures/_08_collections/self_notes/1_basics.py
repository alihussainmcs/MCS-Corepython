"""
Collections
Python ships with a module that contains a number of container data types called Collections. 
We will talk about a few of them and discuss their usefulness.

The ones which we will talk about are:

defaultdict
OrderedDict
Counter
deque
namedtuple
enum.Enum (outside of the module; Python 3.4+)
"""

"""
1. defaultdict
Unlike dict, with defaultdict you do not need to check whether a
 key is present or not. So we can do:
"""

# https://book.pythontips.com/en/latest/collections.html

from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# Python program to demonstrate
# defaultdict

print()


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = '1'
d["b"] = '2'

print(d["a"])
print(d["b"])
print(d["c"])
