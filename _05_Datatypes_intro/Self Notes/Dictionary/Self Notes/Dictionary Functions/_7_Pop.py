# pop()------ method removes and returns an element from a dictionary having the given key


print("*****Pop*****")

print("pop()--->Removes the element with the specified key")

emp = {'name': "ALI", 'eid': "0044", 'location': "Bangalore"}

a = emp.pop("location")

print("Popped Element is:", a)

print("After removing:", emp)

# b = emp.pop("number")  -----> Error

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}

print(type(Employee))

print("printing Employee data .... ")

print(Employee)

print("Popped Element Employee.pop('Address' :", Employee.pop('Address'))

print("After removing:", Employee)

print("Popped Element Employee.pop('Age' :", Employee.pop('Age'))

print("After removing:", Employee)

print("Popped Element Employee.pop('Company' :", Employee.pop('Company'))

print("After removing:", Employee)

print("Popped Element Employee.pop('salary' :", Employee.pop('salary'))

print("After removing:", Employee)
