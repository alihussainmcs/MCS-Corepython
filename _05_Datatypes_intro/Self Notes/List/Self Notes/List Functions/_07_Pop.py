# Pop()------ method removes the item at the given index from the list and returns the removed item.

print("*****Pop*****")
print("pop()--->Removes the element at the specified position")

numbers = [2, 3, 5, 7, 9, 11]

r1 = numbers.pop(3)
print("Removed element:", r1)
print("List after removing:", numbers)


# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
r2 = languages.pop(3)


print('Return Value:', r2)

print('Updated List:', languages)

fruits = ['Mango', 'Banana', 'Grapes', 'Kiwi', 'Pineapple', 'apple']

print('List :', fruits)

fruits.pop()

print('List after pop :', fruits)

fruits.pop()

print('List after pop :', fruits)

print('fruits.pop() :', fruits.pop())

print('List after pop :', fruits)

fruits.pop(0)

print('List after pop(0) :', fruits)

# fruits.pop(4) IndexError: pop index out of range

fruits.pop(-1)

print('List after pop(-1) :', fruits)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

print('List :', my_list)

my_list.pop()

print('List after pop :', my_list)

my_list.pop()

print('List after pop :', my_list)

my_list.pop()

print('List after pop :', my_list)

my_list.pop(0)

print('List after pop(0) :', my_list)

my_list.pop(-1)

print('List after pop(-1) :', my_list)
