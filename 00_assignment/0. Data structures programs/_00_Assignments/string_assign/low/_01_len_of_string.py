# P01. REQ : Find length of given string   ie., "Hello World"

"""
1. CRUD       -
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS | Operators |  Decision Making or Loops
"""
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =       |      
'''

# 0. Mathematics 80%
'''
1. Define the string 
2. Take initial count as 0
3. Start reading it. 
4. While reading each char, increase the count
'''

# 1.Builtin functions 80%

print("--------1 Builtin Functions      ----------")

message = 'Hello World'  # static way
# message = input("Enter any string : ")

print("Length of given string : ", len(message))


# 2. Algorithm  80%

print("--------2 Algorithm              ----------")

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)

# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions        ----------")

# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented        ----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling     ----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling          ----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction   ----------")

# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction         ----------")
