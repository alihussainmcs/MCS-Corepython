# P01. REQ : Find length of given string   ie., "Hello World"

'''
Topics:
--------
Operators
DM vs Loops
Data structure
'''

# 0. Mathematics
# Implement the solutions in white paper

# 1.Builtin functions

print("*****1. Built Functions*******")

message = 'Hello World'  # static way
# message = input("Enter any string : ")

print("Length of given string : ", len(message))


# 2. Algorithm

print("--------2. Algorithm----------")  # 150

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)


# 3 Using Functions  ==> 10
print("--------3 Using Functions----------")
    # I. STATE
message = 'Hello World'
    # BEHAVIOR
def get_str_len(msg):
    leng = 0
    for char in msg:
        leng += 1
    print("Length of given string : ", leng)
get_str_len(message)

# With return type
message = 'Hello World' # Global
def get_str_len(msg):   # msg -> local scope
    print("String is : ",message)  # Global variable can be accesssed from anywhere
    lent = 0            # lent -> Local scope
    for char in msg:
        lent += 1
    return lent
# print(msg, lent) # Local variables cant be accessed from outside fuction

str_len = get_str_len(message)   # x = 10 print(x)
print("Length of given string : ", str_len)

print("Length of given string : ", get_str_len(message))   # print(10)



# 4 OOPS  ==> 5

print("--------4 Object Oriented----------")  # 50


# 5 Exception handling  ==> 25

print("--------5 Exception handling----------")


# 6 File Handling  ==> 15

print("--------6 File Handling----------")


# 6 Database interaction MVC  ==> 5

print("--------6 Database interaction----------")


# 7 UI Interaction   ==> 3

print("--------7 UI Interaction----------")
