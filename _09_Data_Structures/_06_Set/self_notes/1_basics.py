print("......................Set..............................")

# State
# Behaviour
# CRUD ---- Retrieve

set_1 = {1, 10.5, 'Python', True, 10 + 40j}

print("Given set is :", set_1)  # 1 and True means 1 so it will print--- Given set is : {1, 10.5, 'Python', (10+40j)}

# Set is mutable data structure
# Elements of set are immutable

set_2 = {1, 1, 3, True, 'Hello', (1, 2, 3)}

print("Type of set_2 is ", type(set_2))

print("Set is Mutable : ", set_2)

print("length of set_2 is ", len(set_2))

# set_3 = {{1, 2, 3}, {1: 1, 2: 2}, [1, 2, 3]}

# print("Given set is :", set_3)  # TypeError: unhashable type: 'set'
