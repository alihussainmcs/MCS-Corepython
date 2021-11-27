# 3. Index()---> method returns the index of the specified element in the list.

print("*****Index*****")

print("extend()--->method returns the position at the first occurrence of the specified value")

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
