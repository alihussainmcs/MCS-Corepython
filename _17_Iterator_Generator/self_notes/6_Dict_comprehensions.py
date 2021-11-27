"""
Python Dictionary Comprehension

Like List Comprehension, Python allows dictionary comprehensions. We can create dictionaries using simple expressions.
A dictionary comprehension takes the form {key: value for (key, value) in iterable}

Let’s see a example,lets assume we have two lists named keys and value now,

"""
# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# but this line shows dict comprehension here
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print(myDict)

print("---------------------------------------------------------------------------------------------")

# Python code to demonstrate dictionary
# creation using list comprehension
myDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(myDict)

print("------------------------------------------------------------------------------------------------")

sDict = {x.upper(): x * 3 for x in 'Python!'}
print(sDict)

print("-------------------------------------------------------------------------------------")

# Python code to demonstrate dictionary
# comprehension using if.
new_dict = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(new_dict)

print("----------------------------------------------------------------")

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Identify odd and even entries
dict1_tripleCond = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict1.items()}

print(dict1_tripleCond)
