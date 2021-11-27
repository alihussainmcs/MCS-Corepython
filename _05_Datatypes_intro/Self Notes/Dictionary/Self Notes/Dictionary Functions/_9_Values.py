# Values()------ method returns a view object that displays a list of dictionary's (key, value) tuple pairs

print("*****Values*****")
print("values()--->Returns a list of all the values in the dictionary")

emp = {'name': "Karthick", 'eid': "0037", 'location': "Bangalore"}
print("The Values of the dictionary:", emp.values())

print("The Values are:")
for val in emp.values():
    print(val)