"""
The pop() method removes the specified item from the dictionary.

Syntax
dictionary.pop(keyname, defaultvalue)

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary before pop : ", car)

car.pop("model")

print("Dictionary after pop : ", car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary before pop : ", car)

x = car.pop("model")

print("Dictionary value after pop : ", x)
