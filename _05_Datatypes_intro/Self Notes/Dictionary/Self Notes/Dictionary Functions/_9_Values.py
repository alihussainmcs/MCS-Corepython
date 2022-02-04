# Values()------ method returns a view object that displays a list of dictionary's (key, value) tuple pairs

print("*****Values*****")
print("keys()--->Returns a list of all the values in the dictionary")

emp = {'name': "ali", 'eid': "0044", 'location': "Bangalore"}
print("The Values of the dictionary:", emp.values())

print("The Values are:")
for val in emp.values():
    print(val)


d = {}

print('Dictionary :', d)

print('type :', type(d))

d[0] = 'zero'

d[1] = 'one'

d[2] = 'two'

d[3] = 'three'

d[4] = 'four'

print('Dictionary :', d)

print('Values of Dictionary :', d.values())

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}

print(type(Employee))

print("printing Employee data .... ")

print(Employee)

print('Values of Dictionary :', Employee.values())
