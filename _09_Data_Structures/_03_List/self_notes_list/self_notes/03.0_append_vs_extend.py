# append vs extend

list_5 = [1, 2, 3, 100, 89, True]

list_5.append([10])

list_5.append(99)

list_5.append(({18}))

list_5.append({1: 'a', 2: 56})

list_5.append([11000, 12000])

print("List after append : ", list_5)

list_5.extend([100, 200])

list_5.extend(['x', 'y', True])

print("List after extend : ", list_5)
