# 3. Index()---> method returns the index of the specified element in the list.

print("*****Index*****")

print("extend()---> method returns the index of the specified element in the list.")

a = ["an", "are", "was", "were"]

print("Normal List is:", a)

b = a.index("are")  # shows the index of are

print("The index of are is:", b)

# list.index(value, start, end)

'''
element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index
'''

'''
The index() method returns the index of the given element in the list.
If the element is not found, a ValueError exception is raised
'''

list1 = ["a", "e", "i", "o", "u"]

print("Normal List is:", list1)

ind = list1.index("i")

ind2 = list1. index("o")

print("The index of i is:", ind)

print("The index of o is:", ind2)

list2 = ['lion', 'tiger', 'leopard']

print('List :', list2)

print("The index of lion is:", list2.index('lion'))

print("The index of leopard is:", list2.index('leopard'))

print("The index of tiger is:", list2.index('tiger'))

fruits = ["apple", "banana", "cherry", "mango"]

print('List :', fruits)

print("The index of apple is:", fruits.index('apple'))

print("The index of banana is:", fruits.index('banana'))

print("The index of cherry is:", fruits.index('cherry'))

print("The index of mango is:", fruits.index('mango'))

# print("The index of kiwi is:", fruits.index('kiwi'))    # ValueError: 'kiwi' is not in list

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

print('List :', my_list)

print("The index of m is:", my_list.index('m'))
