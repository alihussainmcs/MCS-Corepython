# P01. REQ : Find length of given string   ie., "Hello World"
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=    |   for
"""

# 0. Mathematics
"""
1. Initialize the string
2. count the element of the string
3. At last found length of string
a = 'afsat143'
     12345678
     length is 8
"""

# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function lem(), will found len of the string and Retrieve the lem() value 
"""
print("--------1 Builtin Functions      ----------")
print(".........     Static way         ..........")
a = 'afsat143'  # static way
print("The given string is :", a)
print('Length of the string is ', len(a))

"""

print("......... Taking String from user .........")
a = input("Enter the string which length you want to know :")
print("The length of the string is ", len(a))

"""

# 2. Algorithm
"""
1. Initialize the string
2. Initialize the count variable with zero value
3. Use Loop (for loop) with string and start iteration and increment value of count variable with every iteration
4. Retrieve count variable 

"""
print("--------2 Algorithm              ----------")

a = 'afsat143'
print("The given string is :", a)
count = 0
for i in a:
    count += 1

print("Length of the String is ", count)

# 3 Using Functions
print("--------3 Using Functions        ----------")

# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
