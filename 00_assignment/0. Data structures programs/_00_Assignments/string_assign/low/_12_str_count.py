# REQ : Count words in a string

"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int   | = | +=
"""

# 0. Mathematics
"""
str_1 = 'adsfretasrtfsar'
         find : a count
         1      2     3 
         a count is 3

"""

# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function count(), will found number of repeat of the word and Retrieve the count() value 
"""
print("--------1 Builtin Functions      ----------")

str_1 = 'adsfretasrtfsar'
print("String : ", str_1)

str_1.count('a')
print("String element 'a' count is: ", str_1.count('a'))

# 2. Algorithm
"""
1. Initialize the string
2. Initialize the count variable with zero value
3. Use Loop (for loop) with string and start iteration and increment value of count variable with every iteration
4. Retrieve count variable 

"""
print("--------2 Algorithm              ----------")

str_1 = 'adsfretasrtfsar'
print("String : ", str_1)
count = 0
for i in str_1:
    if i == 'a':
        count += 1
print("String element 'a' count is: ", count)

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
