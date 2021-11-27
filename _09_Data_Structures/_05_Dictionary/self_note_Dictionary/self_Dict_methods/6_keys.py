"""
The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

Syntax
dictionary.keys()

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("Dictionary car : ", car)

x = car.keys()

print("Dictionary car keys are ", x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print("Dictionary car : ", car)

print("Dictionary car keys are ", x)
