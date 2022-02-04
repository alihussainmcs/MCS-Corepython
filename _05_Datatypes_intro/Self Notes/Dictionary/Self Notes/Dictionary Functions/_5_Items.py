# Items()------ method returns a view object that displays a list of dictionary's (key, value) tuple pairs

print("*****Items*****")
print("items()--->Returns a list containing a tuple for each key value pair")

marks = {'Physics': 67, 'Maths': 87}

print(marks.items())

for i in marks.items():
    print(i)

d = {}

print('Dictionary :', d)

print('type :', type(d))

d[0] = 'zero'

d[1] = 'one'

d[2] = 'two'

d[3] = 'three'

d[4] = 'four'

print('Dictionary after adding values :', d)

print('d.items()', d.items())

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE", 'Address': 'HP'}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)

print('Employee.items() ', Employee.items())
