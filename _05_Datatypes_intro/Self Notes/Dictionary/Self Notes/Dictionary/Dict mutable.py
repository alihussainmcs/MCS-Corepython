"""
Change Values
You can change the value of a specific item by referring to its key name.
"""

a = {
    "brand": "MRF",
    "wood": "Willow",
    "year": 1995
}

print("Before changing the year value:", a)  # Before changing the values

a["year"] = 2000

print("After Changing the year Value:", a)  # value of Year is changed

'''
Update Dictionary
-----------------
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
'''
a = {
    "brand": "MRF",
    "wood": "Willow",
    "year": 1995
}

# we can use update method also to change the values

a.update({"wood": "Kashmir willow"})
print("After Updating the wood value:", a)

'''
Adding Items
------------
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
'''
a = {"brand": "MRF", "wood": "Willow", "year": 1995, "player": "Sachin"}
print(a)
a['play'] = 'cricket'
print("After adding new item", a)

'''
Deleting Items in dictionary
----------------------------
'''

# The del keyword can also delete the dictionary completely

a = {
    "brand": "MRF",
    "wood": "Willow",
    "year": 1995
}

del a["wood"]
print("After Deleting wood:", a)

d = {}

print(d)

d['a'] = 1

d['b'] = 2.9

d['c'] = 'string'

d['d'] = True

d['e'] = 10+19j

print('Dictionary :', d)

print('Keys :', d.keys())

print('Values :', d.values())
