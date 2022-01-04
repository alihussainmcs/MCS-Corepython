# P14. REQ :  accepts a string and calculate the number of upper case letters and lower case letters
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = 'I am the PYTHON Developer.'
lvr = 0
upr = 0
for i in str_1:
    if i.islower():
        lvr += 1

    elif i.isupper():
        upr += 1

print('Given string :', str_1)

print('Lower chars count :', lvr)

print('Upper chars counts :', upr)

# 3 Using Functions
print("--------3 Using Functions        ----------")


def lower_upper(str_2):
    lvr_1 = 0
    upr_1 = 0
    for j in str_2:
        if j.islower():
            lvr_1 += 1

        elif j.isupper():
            upr_1 += 1

    print('Given string :', str_2)

    print('Lower chars count :', lvr_1)

    print('Upper chars counts :', upr_1)


lower_upper('I am ALI')
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
