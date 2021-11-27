# P01. REQ : Find length of given string   ie., "Hello World"

'''
Topics:
--------
  I. CRUD            :  Retrieve
 II. Datatypes       :  integer string
III. State(variable) :  str = 'Hello World'
 IV. Behavior        :  +=   for loops
        (Operators,
         DM,
         Loops)
'''

# 0. Mathematics                          # 150 programs
# Implement the solutions in white paper
'''
- Hello World
- count each character 
- initialize the counter to 0
- while counting incrementing counter value from 0 to +1 in each iteration
'''

# 1.Builtin functions
print("*****1. Built Functions*******")   # 150 programs

message = 'Hello World'  # static way
# message = input("Enter any string : ")  # Dynamic way

print("Length of given string : ", len(message))


# 2. Algorithm

print("--------2. Algorithm----------")   # 150 programs

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)


# 3 Using Functions                         # 50 Programs
print("--------3 Functions----------")

# 4 OOPS

print("--------4 Object Oriented----------")  # 50 programs


# 5 Exception handling                        ==> 25 programs

print("--------5 Exception handling----------")


# 6 File Handling                            ==> 15 programs

print("--------6 File Handling----------")


# 6 Database interaction MVC                ==> 5 programs

print("--------6 Database interaction----------")


# 7 UI Interaction                          ==> 3 programs

print("--------7 UI Interaction----------")
