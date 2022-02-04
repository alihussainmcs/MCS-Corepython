# setdefault()------ Returns the value of the specified key. If the key does not exist: insert the key, with the
#                     specified value

print("*****setdefault*****")
print("setdefault()--->Returns the value of the specified key. If the key does not exist: insert the key, "
      "with the specified value")

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

emp = {'name': "ali", 'eid': "0044", 'location': "Bangalore"}

print('Dictionary :', emp)

emp.setdefault('sal', '100000')

print(emp)
