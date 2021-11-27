# pop()------ method removes and returns an element from a dictionary having the given key


print("*****Pop*****")
print("pop()--->Removes the element with the specified key")

emp = {'name': "Karthick", 'eid': "0037", 'location': "Bangalore"}
a = emp.pop("location")
print("Popped Element is:", a)
print("After removing:", emp)


# b = emp.pop("number")  -----> Error