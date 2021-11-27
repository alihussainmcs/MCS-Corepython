"""
The values() method returns a view object. The view object contains the values of the dictionary, as a list.

Syntax

dictionary.values()

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary  : ", car)

x = car.values()

print("Dictionary value : ", x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

car["id"] = 4400

print("Dictionary  : ", car)

print("Dictionary value : ", x)
