# get()------ method returns the value for the specified key if the key is in the dictionary

print("*****Get*****")
print("get()--->Returns the value of the specified key")

'''
get() method returns:
the value for the specified key if key is in the dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.

'''

a = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

b = a.get(2)
print(b)

person = {'name': 'karthick', 'age': 22}

print('Name: ', person.get('name'))


print('Age: ', person.get('age'))

# value is not provided

print('Salary: ', person.get('salary'))  # Here the value for salary is none

# value is provided
print('Salary: ', person.get('salary', 0.0))

