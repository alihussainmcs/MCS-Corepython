# update()------ method updates the dictionary with the elements from another
# dictionary object or from an iterable of key/value pairs

print("*****Update*****")
print("update()--->Updates the dictionary with the specified key-value pairs")


a = {
  "brand": "MRF",
  "wood": "Willow",
  "year": 1995
}

a.update({"wood": "Teakwood"})
print("After Updating:", a)