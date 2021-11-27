"""
The update() method inserts the specified items to the dictionary.

The specified items can be a dictionary, or an iterable object with key value pairs.

Syntax
dictionary.update(iterable)

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary before update : ", car)

car.update({"color": "White"})

car.update({101: True})

# car.update({101: False}) # key should unique

car.update({102: False})

print("Dictionary after update : ", car)

car.update({103: 'Alan'})

print("Dictionary after update : ", car)
