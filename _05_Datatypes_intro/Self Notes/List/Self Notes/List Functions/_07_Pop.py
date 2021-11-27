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