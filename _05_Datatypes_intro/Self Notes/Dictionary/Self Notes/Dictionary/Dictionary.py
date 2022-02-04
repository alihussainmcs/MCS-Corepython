"""
Dictionary:
-----------
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values."""

'''Creating a Dictionary:
----------------------
'''
x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(x)

'''Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.'''

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict["brand"])

'''Dictionary Methods:
-------------------

-->clear()	    Removes all the elements from the dictionary
-->copy()	    Returns a copy of the dictionary
-->fromkeys()	Returns a dictionary with the specified keys and value
-->get()	    Returns the value of the specified key
-->items()	    Returns a list containing a tuple for each key value pair
-->update()	    Updates the dictionary with the specified key-value pairs
-->pop()	    Removes the element with the specified key
-->popitem()	Removes the last inserted key-value pair
-->values()	    Returns a list of all the values in the dictionary
-->keys()	    Returns a list containing the dictionary's keys
-->setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the
                    specified value
'''

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
