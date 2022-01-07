# P13. REQ : Remove duplicates from Dictionary
"""
1. CRUD       -->  Update
2. STATE      -->  Dictionary
3. BEHAVIOR   -->  dict  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

student_data = {1:
                    {'name': ['Sara'],
                     'subject': ['PCM']
                     },
                2:
                    {'name': ['David'],
                     'subject': ['PCM']
                     },
                3:
                    {'name': ['Sara'],
                     'subject': ['PCM']
                     }
                }

print('Original Dictionary :', student_data)
result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

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
