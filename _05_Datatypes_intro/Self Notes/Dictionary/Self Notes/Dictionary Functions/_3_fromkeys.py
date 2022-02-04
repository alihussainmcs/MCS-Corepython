# fromkeys()------method creates a new dictionary from the given sequence of elements with a value provided by the user

print("*****Fromkeys*****")
print("fromkeys()--->Returns a dictionary with the specified keys and value")

'''
With Specifying the Value:
--------------------------
'''
x = ('1', '2', '3')
values = "numbers"

a = dict.fromkeys(x, values)
print(a)

'''
Without Specifying the Value:
-----------------------------
'''
x = ('1', '2', '3')
b = dict.fromkeys(x)  # without specifying the value none will be stored for every key
print(b)

"""
Syntax
dict.fromkeys(keys, value)


Parameter	    Description
keys	        Required. An iterable specifying the keys of the new dictionary
value	        Optional. The value for all keys. Default value is None
"""

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squares.fromkeys(squares.keys()))

print(squares.fromkeys(squares.keys(), squares.values()))

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data before copy .... ")
print(Employee)

print(Employee.fromkeys(Employee))

print(Employee.fromkeys(Employee.values()))

print(Employee.fromkeys(Employee.values(), Employee.keys()))
