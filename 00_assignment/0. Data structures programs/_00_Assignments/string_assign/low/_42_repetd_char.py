# P01. REQ : count repeated characters in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =    |
"""

# 0. Mathematics
"""
1. Initialize the string
2. count repeated characters in a string

check_string = "i am checking this string to see how many times each character appears"
                | || ||...............................................................
                
                5 73 55............................................................... 
"""
# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function count(), will found number of repeat of the substring and Retrieve the count() value 
"""
print("--------1 Builtin Functions      ----------")

chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"
print("String :", check_string)
for char in chars:
    count = check_string.count(char)
    if count > 1:
        print(char, count)

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
