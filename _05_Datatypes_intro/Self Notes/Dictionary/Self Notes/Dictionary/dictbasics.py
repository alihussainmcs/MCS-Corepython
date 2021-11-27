
# Creating and printing the dictionary

emp = [1, 'karthick', 30000, 'Male', 'Bangalore', '098766']
print("Employee data : ", emp)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

a = {
  "brand": "MRF",
  "wood": "Willow",
  "year": 1995
}
print(a["wood"]) # printing the wood value here wood is key

print(a.get("wood")) # printing the wood value using get() method

# Accessing the Keys----First Method

print(a.keys())

# Accessing the Keys----Second Method

print("The Keys are:")
for i in a.keys():
  print(i)

# Accessing the values----First Method
print(a.values())

# Accessing the Keys----Second Method

print("The Values are:")
for i in a.values():
  print(i)

# Adding a new items in dictionary

a = {
  "brand": "MRF",
  "wood": "Willow",
  "year": 1995
}

print("Before changing the value:", a)  # Before changing the values

a["year"] = 2000

print("After Changing the Value:", a) # value of Year is changed
