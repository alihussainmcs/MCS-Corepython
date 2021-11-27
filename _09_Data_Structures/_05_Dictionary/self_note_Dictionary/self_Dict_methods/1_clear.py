"""
The clear() method removes all the elements from a dictionary.

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(("Dictionary before clear : ", car))

car.clear()

print(("Dictionary after clear : ", car))


e_id = {101: "Ford", 102: "Mustang", 103: 'Ferrari'}

print(("Dictionary before clear : ", e_id))

e_id.clear()

print(("Dictionary after clear : ", e_id))
