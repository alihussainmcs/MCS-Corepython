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