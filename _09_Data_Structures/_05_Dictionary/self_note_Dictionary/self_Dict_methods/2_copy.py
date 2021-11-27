"""
The copy() method returns a copy of the specified dictionary.

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(("Dictionary before copy : ", car))

car_copy = car.copy()

print(("Dictionary copy : ", car_copy))

e_id = {101: "Ford", 102: "Mustang", 103: 'Ferrari'}

print(("Dictionary before copy : ", e_id, id(e_id)))

e_id_copy = e_id.copy()

print(("Dictionary after copy : ", e_id_copy, id(e_id_copy)))

print("................Normal Copy.......................")

e_id = {101: "Ford", 102: "Mustang", 103: 'Ferrari'}

print(("Dictionary before copy : ", e_id, id(e_id)))

e_id_copy = e_id

print(("Dictionary after copy : ", e_id_copy, id(e_id_copy)))
