# update()------ method updates the dictionary with the elements from another
# dictionary object or from an iterable of key/value pairs

print("*****Update*****")
print("update()--->Updates the dictionary with the specified key-value pairs")

a = {
    "brand": "MRF",
    "wood": "Willow",
    "year": 1995
}

a.update({"wood": "Deadwood"})
print("After Updating:", a)

d = {}

print('Dictionary :', d)

print('type :', type(d))

d[0] = 'zero'

d[1] = 'one'

d[2] = 'two'

d[3] = 'three'

d[4] = 'four'

print('Dictionary after adding values :', d)

d.update({0: 'ZERO'})

d.update({1: 'ONE'})

d.update({2: 'TWO'})

d.update({3: 'THREE'})

d.update({4: 'FOUR'})

print('Dictionary after update values :', d)
