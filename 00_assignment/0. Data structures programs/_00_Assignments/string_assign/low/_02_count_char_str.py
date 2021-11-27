# REQ 2. Count characters in string

"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=    |   for
"""

# 0. Mathematics
"""
1. Initialize the string
2. count the char of the string
3. At last found length of char of the string

a = 'agftr14325afrt'
     12345     6789
     count of char is 9
"""


# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

"""
1. Initialize the string
2. Initialize the count variable with zero value
3. Use Loop (for loop) with string and start iteration and increment value of count variable with every iteration
   for char value
4. Retrieve count variable 

"""

a = 'agftr14325afrt'
print("The String is :", a)
count = 0
for i in a:
    if i.isalpha():
        count += 1

print('Length of char in the string are : ', count)

# 2. Algorithm
print("--------2 Algorithm              ----------")

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
