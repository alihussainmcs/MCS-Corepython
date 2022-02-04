# copy()------ Returns a copy of the list

print("*****Copy*****")
print("copy()--->Returns a copy of the list")


numbers = [2, 3, 5, 7, 9, 11]
print("Original List:", numbers)
a = numbers.copy()

print("Copied List:", a)

old_list = [1, 2, 3]

# copy list using =
new_list = old_list
# add an element to list
new_list.append(10)

print('New List:', new_list)
print('Old List:', old_list)

'''
if we need the original list unchanged when the new list is modified, you can use the copy() method.
'''

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

print('Original list :', my_list)

new_lst = my_list.copy()

print('Copy list :', new_lst)

new_lst.append('xyz')

print('List after append a element :', new_lst)

fruits = ['Mango', 'Banana', 'Grapes', 'Kiwi', 'Pineapple', 'apple']

print('List :', fruits)

copy_fruits = fruits.copy()

print('Copy list :', copy_fruits)

lst = [1, True, '1', 1.0]

print('List :', lst)

copy_lst = lst.copy()

print('Copy list :', copy_lst)

print(id(lst))  # 2067644090496

print(id(copy_lst))  # 2067644090560

l1 = [0, 1]

l2 = l1

print(id(l1))  # 2067644090624

print(id(l2))  # 2067644090624
