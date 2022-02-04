# keys()------ method returns a view object that displays a list of dictionary's (key, value) tuple pairs

print("*****keys*****")
print("keys()--->Returns a list containing the dictionary's keys")

emp = {'name': "ali", 'eid': "0044", 'location': "Bangalore"}
print('Dictionary :', emp)
print("The keys of the dictionary:", emp.keys())

print("The keys are:")
for key in emp.keys():
    print(key)

d = {}

print('Dictionary :', d)

print('type :', type(d))

d[0] = 'zero'

d[1] = 'one'

d[2] = 'two'

d[3] = 'three'

d[4] = 'four'

print('Dictionary :', d)

print('keys of Dictionary :', d.keys())

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}

print(type(Employee))

print("printing Employee data .... ")

print(Employee)

print('keys of Dictionary :', Employee.keys())
