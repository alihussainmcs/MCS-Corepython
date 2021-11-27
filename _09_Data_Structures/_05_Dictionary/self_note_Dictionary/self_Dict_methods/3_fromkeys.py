"""
The fromkeys() method returns a dictionary with the specified keys and the specified value.

Syntax

dict.fromkeys(keys, value)

"""

x = ('key1', 'key2', 'key3')
y = 0

this_dict = dict.fromkeys(x, y)

print("Using fromkeys for x = ('key1', 'key2', 'key3'), y = 0 ::: ", this_dict)

x = ('key1', 'key2', 'key3')
y = (1, 2, 3)

this_dict = dict.fromkeys(x, y)

print("Using fromkeys for x = ('key1', 'key2', 'key3'), y = (1, 2, 3) ::: ", this_dict)

x = ('key1', 'key2', 'key3')

this_dict = dict.fromkeys(x)

print("Using fromkeys for x = ('key1', 'key2', 'key3') ::: ", this_dict)
