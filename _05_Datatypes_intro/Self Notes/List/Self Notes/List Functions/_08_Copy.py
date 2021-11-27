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
new_list.append("a")

print('New List:', new_list)
print('Old List:', old_list)

'''
if we need the original list unchanged when the new list is modified, you can use the copy() method.
'''
