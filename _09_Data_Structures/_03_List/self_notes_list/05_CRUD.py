# CRUD Operations

# 1. CREATE
list1 = [17, 29, [300, 400, 500], (110, 220, 330), {1, 2, 3}, {10: 100, 20: 200}]

# 2. RETRIEVE
print('List values : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])

# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2]
print('List values3 : ', list1)
del list1
# print('List values4 : ', list1)
