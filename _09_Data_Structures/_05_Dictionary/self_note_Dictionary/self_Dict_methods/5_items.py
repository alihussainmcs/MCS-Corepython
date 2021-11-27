"""
The items() method returns a view object.The view object contains the key-value pairs of the dictionary,
as tuples in a list.
The view object will reflect any changes done to the dictionary.

Syntax
dictionary.items()

"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Dictionary car items are : ", car.items())

car = {"brand": "Ford", "model": "Mustang", "year": 2018}

print("Dictionary car items are ", car.items())

car["Owner"] = 'Alan'

print("Dictionary car items are ", car.items())

car[1001] = True

print("Dictionary car items are ", car.items())

car[1002] = 100.9999

print("Dictionary car items are ", car.items())
