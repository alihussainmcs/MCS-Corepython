# Dictionary is mutable

# CREATE
print("......................Create.........................")
data = {1: True, 2: 'Two', 3: 3, 'id': 100}

# RETRIEVE
print("......................Retrieve.........................")
print("Dictionary data : ", data, type(data))
print("Dict item data[2] :", data[2])
print("Dict item data['id'] :", data['id'])

# UPDATE
print("......................Update.........................")
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update data[2] = 'Twenty' , data['id'] = 200: ", data)

# DELETE
print("......................Delete.........................")
del data[3]
del data['id']
print("Dictionary delete  del data[3] , del data['id']: ", data)

data.clear()
print("Dictionary delete: ", data)

x = 10
print("X : ", x)
# del x
# print("X : ", x)  # NameError: name 'x' is not defined

# del data
# print("Dictionary delete: ", data) # NameError: name 'data' is not defined
