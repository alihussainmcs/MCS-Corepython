# Items()------ method returns a view object that displays a list of dictionary's (key, value) tuple pairs

print("*****Items*****")
print("items()--->Returns a list containing a tuple for each key value pair")

marks = {'Physics': 67, 'Maths': 87}

print(marks.items())

for i in marks.items():
    print(i)
