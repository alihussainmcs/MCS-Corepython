# OOPs concepts:
"""
1. Data structures  - 3. STATE
2. CRUD operation   - 4. BEHAVIOR
"""

# REQ: Find length of the given string
print("-------1. Using builtin function-------")
str1 = 'hello world'
print("Length of string : ", len(str1))

print("-------2. Using algorithm i.e, Without functions-------")

# 1. STATE
str1 = 'Python world'

# 2. BEHAVIOR
lent = 0
for char in str1:
    lent += 1
print("Length of string : ", lent)

print("-------2. With functions-------")

# 1. STATE
str1 = 'Python world'


# 2. BEHAVIOR


def find_length(in_str=None):
    le = 0
    for _ in in_str:
        le += 1
    return le


print("Length of string : ", find_length(str1))  # 1. single time usage  print(10)
str_len = find_length(str1)  # 2. multiple places    x = 10 print(x)
print("Length of string : ", str_len)


# 3. print responsibility is taken by function only


def find_length(in_str):
    le = 0
    for _ in in_str:
        le += 1
    print("Length of string : ", le)


find_length(str1)

print("Value of x : ", 10)
x = 10
print("Value of x : ", x)


def find_length(in_str, domain=None):
    le = 0
    for _ in in_str:
        if domain == 'Bank':
            le += 1
        elif domain == 'Mobile':
            pass
        elif domain == 'Heathcare':
            pass
        else:
            return 10

    print("Length of string : ", le)


# Hello $%#@ World 123
# 100 places
# 50 modules(banking) with space    - 20
# 50 modules(mobile) without space  - 17
# 50 modules(healthcare) without special characters - 16


'''
Solutions   1. Create new function for without space func.  => 3 functions
            2**. Pass the respective attributes to function   => 1 function       

'''
str1 = 'Hello $%#@ World 123'
# Unknown sector
find_length(str1)
# Banking
find_length(str1, 'Bank')
# Mobile
find_length(str1, 'Mobile')
# Healthcare
find_length(str1, 'HealthCare')

print(".............................................")


def my_function():
    print("Hello from a function")


my_function()
print("............................................")


def my_function(f_name):
    print(f_name + " Refines")


my_function("Petrol")
my_function("Diesel")
my_function("Oil")

print("...................................................")


def my_function(child3, child2, child1):
    print("3rd child is : " + child3)
    print('1st child is :', child1)
    print('2nd child is :', child2)


my_function(child1="Emil", child2="Tobias", child3="Linus")
