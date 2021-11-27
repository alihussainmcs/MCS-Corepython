print("..................Set....................")

s = {}

print("Type of s is : ", type(s))

set_1 = set(s)

print("Type of set_1 is ", type(set_1))

print("................Iteration through set............................")

set_2 = {1, 2, 1, 2, 3, True, False, 10.1, 'Python', 'World', 10 + 11j}

print("Set_2 is ", set_2)

for i in set_2:
    print("Element of set_2 is :", i)

print("...................Update......................")
set_2.add(1001)
# set_2.add(101, 102)  # TypeError: add() takes exactly one argument (2 given)
set_2.add('True')
# set_2.add([1, 2]) # TypeError: unhashable type: 'list'
print("Set_2 after adding element is :", set_2)

print("..........Set element removing....................")

set_2.discard('True')
set_2.discard('World')
set_2.discard('A')  # 'A' element is not in set_2 but not get any error
set_2.discard(1001)
set_2.discard(1)

print("Set_2 after element removal ", set_2)

print('.................Union..................')
s_1 = {1, 2, 3, 4, 5, 6, 7}
s_2 = {5, 6, 7, 8, 9, 10, 11}
print("Set s_1 is ", s_1)
print("Set s_2 is ", s_2)
print('Union of s_1, s_2 is :', s_1.union(s_2))

print('.................Intersection..................')

print('Intersection of s_1, s_2 is :', s_1.intersection(s_2))

print(".......................Difference.......................")

print("Difference of s_1, s_2 is :", s_1.difference(s_2))

print(".................Pop.......................")
print('Element pop in s_1 ', s_1.pop())

print('Element pop in s_1 ', s_1.pop())
