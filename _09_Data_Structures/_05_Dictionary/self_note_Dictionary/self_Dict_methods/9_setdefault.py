"""
The setdefault() method returns the value of the item with the specified key.

Syntax
dictionary.setdefault(keyname, value)

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print("Dictionary setdefault value :", x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print("Dictionary setdefault value :", x)

x = car.setdefault("Language", True)

print("Dictionary setdefault value :", x)
