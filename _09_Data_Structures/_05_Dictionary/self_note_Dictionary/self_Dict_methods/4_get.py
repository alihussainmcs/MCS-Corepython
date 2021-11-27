"""
The get() method returns the value of the item with the specified key.

Syntax

dictionary.get(keyname, value)

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print("Dictionary car is : ", car)

print("""Dictionary with x = car.get("model") """, x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)
print("""Dictionary with x = car.get("price", 15000) """, x)

y = car.get("Ali")

print("""Dictionary with y = car.get("Ali") """, y)
