# P63. REQ :   that accepts a string and calculate the number of digits and letters
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = input("Enter a string : ")
count_1 = 0
count_2 = 0
count_3 = 0
for i in str_1:
    if i.isdigit():
        count_1 += 1
    elif i.isalpha():
        count_2 += 1
    else:
        count_3 += 1

print("number of digit in your string is :", count_1)
print("number of letter in your string is :", count_2)
print("number of non alphanumeric in your string is :", count_3)


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
