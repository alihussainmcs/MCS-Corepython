"""
 1. append(): It appends element(any value) at end of the list
             list1.append(obj) Appends any object obj to list
"""

list1 = [11, 27, 39, 40, 25, 67]

print("Before append : ", list1)

for ind, val in enumerate(list1):
    print(ind, "----", val)

list1.append(10)

print("After append  : ", list1)

list1.append(10.4)

list1.append(True)

list1.append('Hello')

list1.append([1, 2, 3])

list1.append((10, 20, 30))

list1.append({1: 1})

list1.append({100, 200, 300})

print("After all append  : ", list1)

for ind, val in enumerate(list1):
    print(ind, "----", val)
