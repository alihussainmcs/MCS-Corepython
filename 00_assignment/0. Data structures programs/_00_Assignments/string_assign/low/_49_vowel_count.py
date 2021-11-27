# P49. REQ : count and display the vowels of a given text
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
str_1 = 'asgtr1645jhgoi'
            ^^
            ||
         1           23
         vowel = 4

1. Initialize the string
2. Count the vowels 

"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")
str_1 = 'asgtr1645jhgoi'
print("String :", str_1)
vow = 'aeiou'
count = 0
for i in str_1:
    if i in vow:
        count += 1

print('Vowel count in String : ', count)

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
