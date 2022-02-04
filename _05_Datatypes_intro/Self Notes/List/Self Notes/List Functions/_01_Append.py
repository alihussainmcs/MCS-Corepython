# 1. append()---->method adds an item to the end of the list

print("*****Append*****")
print("append()--->adds an item to the end of the list")

list1 = ['lion', 'tiger', 'leopard']

print("Normal List:", list1)
list1.append("elephant")

print("list after adding the element:", list1)


# Adding List to a List

li1 = ['a', 'b', 'c', 'd', 'e']
print("Normal List li1:", li1)
li2 = ['f', 'g']
print("New List li2:", li2)

li1.append(li2)

print("After adding a new list to a list:", li1)

l1 = [1, 2, 3, 4, 5, 6, True, False]

print('List :', l1)

l1.append('True')

l1.append('False')

l1.append('ali')

l1.append('py')

print('List after append elements :', l1)

fruits = ["apple", "banana", "cherry", "mango"]

print('List :', fruits)

fruits.append('pineapple')

fruits.append('grapes')

fruits.append('orange')

fruits.append('kiwi')

print('List after append elements :', fruits)

fruits.append(li2)

print('List after append li2 list :', fruits)

fruits.append(l1)

print('List after append l1 list :', fruits)

l1.append(list1)

print('List l1 after append list1 list :', l1)
