# P55. REQ :  find the first repeated word in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |   for, if/else
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
str_1 = "ab ca bc ab ca ab"
print("String :", str_1)
str_2 = str_1.split(' ')
print("String :", str_2)
count = 0
for i in set(str_2):
    print("%s" % i, 'count', str_2.count(i))
    count += 1

# 3 Using Functions
print("--------3 Using Functions        ----------")


def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return 'None'


print(first_repeated_word(str_1))

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
