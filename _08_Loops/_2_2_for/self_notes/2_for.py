"""
Syntax :
------------
# for loop syntax
        for <var> in <sequence>:
           # statements

string list tuple
"""

'''
numbers system -1,-2/4, 34.4, 56, 3 4/5, 0 ,00
advanced concepts : Sequence,Series  1 to 100 -- n(n+1)/2
                  : Sets {1,2,3} U {2,3,4}
                  : Matrix []


'''

# 1. Find sum of numbers from 1 to 100
# Using while
n = 1
sum_1 = 0
while n < 101:
    sum_1 += n
    n += 1

print(' Sum of numbers from 1 to 100 is : ', sum_1)

#  Using for loop
sum_1 = 0
for i in range(1, 101):
    sum_1 += i
print('Sum of numbers from 1 to 100 is : ', sum_1)

# Data Types
x_1 = 10  # integer
x = 10.5  # float  complex long
is_male = True  # boolean

# Data structures
message = "Hello World"  # String
numbers_1 = [1, 2, 3, 4, 5]  # list
numbers = (1, 2, 3, 4, 5)  # tuple
emp_details = {'eid': 100, 'name': 'Madhu', 'sal': 1000}  # Dictionary
emp_ids = {1, 2, 3, 4, 5, 6}  # Set

print("---------String--------------")
# for loop with strings


# String
message_1 = 'Hello hi how are you '
for i in message_1:
    print(i)

print("End of the loop..........")

# List
numbers_2 = [1, 2, 3, 4, 5, 6, 7]
for i in numbers_2:
    print(i)
print("End of the loop ...........")

# Tuple
numbers_3 = (1, 2, 5, 6, 7, 8)
for i in numbers_3:
    print(i)
print("End of the loop .............")

# Set
print(" Set .............")
numbers_5 = {1, 2, 4, 2, 1, 4, 9, 10}
for i in numbers_5:
    print(i)
print(" End of the loop ...........")

# Dictionary
print("...........Dictionary............")
d = {101: 'a', 102: 'b', 103: 'c'}
for i in d.keys():
    print(i)
print(" End of the loop ..............")

for i in d.values():
    print(i)
print(" End of the loop ..............")

for i in d.items():
    print(i)
print(" End of the loop ..............")

list1 = [1, 2, 3, 4, 5]
# Output : Find square of each number  1, 4, 9, 16, 25
'''
  = [1, 2, 3, 4, 5]
  = [1**1, 2*2, 3*3, 4*4, 5*5]
'''
print("-------Square of list----------")
for i in list1:
    print(i * i, end=' ')

print(" End of loop ................", end='\n ')

print(".................Member of the list ..............")

list_1 = [1, 2, 4, 5, 6, 8, 9, 10]
list_2 = [2, 4, 6, 8]
for i in list_2:
    if i in list_1:
        print("%i is same in list_1" % i)

print(".....................Patterns......................")

for i in range(1, 6):
    for j in range(1, 6):
        print('*', end=' ')
    print(end='\n')

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

for i in range(1, 6):
    for j in range(i, 6):
        print('*', end=' ')
    print(end='\n')

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=' ')
    print('\n')

'''
1 1 1 1 1 

2 2 2 2 2 

3 3 3 3 3 

4 4 4 4 4 

5 5 5 5 5 

'''

for i in range(6):
    for j in range(i):
        print(i, end=' ')
    print('\n')

'''
1  

2 2  

3 3 3  

4 4 4 4  

5 5 5 5 5

'''

for i in range(6, 1, -1):
    for j in range(i):
        print(j + 1, end=' ')
    print('\n')

'''
1 1 1 1 1 

2 2 2 2 

3 3 3 

4 4 

5

'''

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print('\n')

'''
5 5 5 5 5 

4 4 4 4 

3 3 3 

2 2 

1 
'''
