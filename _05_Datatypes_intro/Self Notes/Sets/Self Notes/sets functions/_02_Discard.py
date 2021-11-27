# Discard---> Used to remove an item.

'''
remove() method can also be used to remove the item.
The only difference is if the item to remove does not exist, remove() will raise an error
whereas discard() method will not raise the error'''




b = {9, 6, 10, 34}
# printing the set before deleting
print("The original Set:", b)
b.discard(34)
# printing the set after deleting
print("The updated set:", b)