# Access set items:

'''
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
by using the in keyword.
'''


a = {"apple", "banana", "cherry"}
print("The Items Present in the sets are:")
for x in a:
  print(x)

# Checking the items:

a = {"apple", "banana", "cherry"}

if "cherry" in a:
  print("Cherry is present in the set")
else:
  print("Cherry is not present in the list")




