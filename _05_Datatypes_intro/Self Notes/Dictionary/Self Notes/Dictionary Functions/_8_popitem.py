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

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}

print(type(Employee))

print("printing Employee data .... ")

print(Employee)

print('popitem is :', Employee.popitem())

print('Dictionary after popitem :', Employee)

print('popitem is :', Employee.popitem())

print('Dictionary after popitem :', Employee)

print('popitem is :', Employee.popitem())

print('Dictionary after popitem :', Employee)

d = {}

print('Dictionary :', d)

print('type :', type(d))

d[0] = 'zero'

d[1] = 'one'

d[2] = 'two'

d[3] = 'three'

d[4] = 'four'

print('Dictionary :', d)

print('popitem is :', d.popitem())

print('Dictionary after popitem :', d)

print('popitem is :', d.popitem())

print('Dictionary after popitem :', d)

print('popitem is :', d.popitem())

print('Dictionary after popitem :', d)
