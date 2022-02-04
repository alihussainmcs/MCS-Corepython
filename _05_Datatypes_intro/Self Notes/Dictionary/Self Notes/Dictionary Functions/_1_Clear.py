# clear()------method removes all items from the dictionary

print("*****Clear*****")
print("Clear()--->removes all items from the dictionary")

a = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

a.clear()
print("Empty dictionary:", a)

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)

print('Dictionary after using clear method :', Employee.clear())

print('after clear the Employee dictionary :', Employee)
