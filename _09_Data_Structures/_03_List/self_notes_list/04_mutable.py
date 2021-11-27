# String is immutable
print('..............string mutability .................')

msg = 'Python'

print("Before changing the string, address: ", msg, 'Address', id(msg))

msg = 'String Immutable'

print("After changing the string, address : ", msg, 'Address', id(msg))

print('..............list immutability .................')

# List is mutable
list1 = [321, 123, 351, 786, 430, 572, 1115]
print("Before changing the list , address: ", list1, id(list1))

print("Before changing the list , address of list1[1] : ", list1, id(list1[1]))

list1[1] = 1000
print('.............................................................................')

print("After changing the list , address : ", list1, id(list1))

print("Before changing the list , address of list[1] : ", list1, id(list1[1]))



print("........................second list.............................")

list2 = [[1, 2, 3, 4], 123, 351, 786, 430, 572, 1115]
print("Before changing the list , address: ", list2, id(list2))

print("Before changing the list , address of list2[1] : ", list2, id(list2[0]))

list2[0] = [10, 20, 30, 40]
print('.............................................................................')

print("After changing the list , address : ", list2, id(list2))

print("Before changing the list , address of list[2] : ", list2, id(list2[0]))
