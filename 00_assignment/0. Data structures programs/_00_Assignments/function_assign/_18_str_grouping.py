# P18. REQ :   function to display group of strings
"""
1. CRUD       -->  Update
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
sentence_list = "I love cat. I love dog.I love fish.I hate banana.I hate apple.I hate orange"
exp. o/p --> ["I love cat", "I love dog", "I love fish", "I hate banana", "I hate apple", "I hate orange"]

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
sentence_list = "I love cat. I love dog.I love fish.I hate banana.I hate apple.I hate orange"
print(sentence_list.split('.'))
# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")


def str_group(str_1):
    print(str_1.split('.'))


str_group("I love cat. I love dog.I love fish.I hate banana.I hate apple.I hate orange")
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
