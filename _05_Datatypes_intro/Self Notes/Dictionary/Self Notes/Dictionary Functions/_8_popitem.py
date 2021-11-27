# popitem()------ method removes and returns the last element (key, value) pair inserted into the dictionary


print("*****popitem*****")
print("popitem()--->Removes the last inserted key-value pair")

# The popitem() method removes and returns the (key, value) pair from the
# dictionary in the Last In, First Out (LIFO) order.

marks = {'Physics': 67, 'Maths': 87, 'Hindi': 70, 'French': 45}
a = marks.popitem()
print("The popped item is:", a)
print("Updated entries:", marks)

# The popitem() method raises a KeyError error if the dictionary is empty

