"""
The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7,
 the popitem() method removes a random item.

The removed item is the return value of the popitem() method, as a tuple.

Syntax
dictionary.popitem()

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary before popitem : ", car)

car.popitem()

print("Dictionary after popitem : ", car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print("Dictionary value after popitem : ", x)
