"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
Getting the Data Type
You can get the data type of any object by using the type() function:

Example
Print the data type of the variable x:

x = 5
print(type(x))
Setting the Data Type
In Python, the data type is set when you assign a value to a variable:
"""
# Example	Data Type	Try it
x = str("Hello World")  # str
print(x)
x = int(20)	 # int
print(x)

x = float(20.5)	 # float
print(x)

x = 11+10j	 # complex
print(x)

x = list(("apple", "banana", "cherry")) 	# list
print(x)

x = tuple(("apple", "banana", "cherry"))  # tuple
print(x)

x = range(6)  # range
print(x)

x = dict(name="John", age=36)  # dict
print(x)

x = {"apple", "banana", "cherry"} 	# set
print(x)

x = frozenset(("apple", "banana", "cherry"))  # frozenset
print(x)

x = bool(5)	 # bool
print(x)

x = bytes(5)  # bytes
print(x)

x = bytearray(5)  # bytearray
print(x)

x = memoryview(bytes(5))  # memoryview
print(x)


print('These are data types ...........')
