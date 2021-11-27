"""
1_Basic

"""

# REQ: Print numbers from 1 to 10
# 1 2 3 4 5 6 7 8 9 10

# 1st
n = 1
while n < 11:
    print(n)
    n += 1

# REQ: Print even numbers
# 2 4 6 8 10 12 .....
# 1 2 3 4 5 6 7 8 9 10 ....
n = 1

while n < 21:
    if n % 2 == 0:
        print(n)
    n += 1

# REQ: Print numbers divisible  by 5
# 0 5 10 15 20 25 .....

n = 1

while n < 21:
    if n % 5 == 0:
        print(n)
    n += 1

# REQ: Print numbers divisible  by 3
# 3 6 9 12 .....
n = 1

while n < 21:
    if n % 3 == 0:
        print(n)
    n += 1

# REQ: Print numbers divisible  by 7
# 7 14 21 28 35 42 .......

n = 1

while n < 21:
    if n % 7 == 0:
        print(n)
    n += 1

# print first 500 to 600 prime numbers  10
# 501 507 509 511 521
# 1st
Number = 500

while Number <= 600:
    count = 0
    i = 2

    while i <= Number // 2:
        if Number % i == 0:
            count = count + 1
            break
        i = i + 1

    if count == 0 and Number != 1:
        print(" %d" % Number, end='')
    Number = Number + 1

# 2nd
# print first 500 to 600 prime numbers with while loop
# 503 509 521 523 541 547 557 563 569 571 577 587 593 599


n1 = 500
n2 = 600
while n1 < n2:
    for i in range(2, int(n1 / 2)):
        if n1 % i == 0:
            break
    else:
        print(n1)
    n1 += 1

# with for loop
# 503 509 521 523 541 547 557 563 569 571 577 587 593 599
for i in range(500, 601):
    count = 0
    for j in range(1, 601):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

'''
- Start printing the number 1
- Increment by 1 for current number
- If the new value is less than 10 then print it each time
- Else stop it
'''
# REQ: Print numbers from 1 to 10

# using while loop

n = 1
while n < 11:
    print(n)
    n += 1

# print numbers between 100 to 150

n = 100
count = 0
while n < 151:
    print(n)
    count += 1
    n += 1
print("Total numbers are : ", count)

''' 
_3_print_even_numbers.py
'''
# REQ : Print even numbers between 1 to 10
'''
  | 2  4          |   2)4(
'''
'''
# STATE    : num = 1

# BEHAVIOR : Print even numbers
             upper limit 10
'''
print("--------Print even numbers--------")
# STATE

n = 1
while n < 11:
    if n % 2 == 0:
        print(n)
    n += 1

# Print odd numbers betweeen 10 to 20

n = 10
while n < 21:
    if n % 2 == 0:
        print(n)
    n += 1

# Print numbers between 500 to 1000 and divisible by 5

n = 500
while n < 1001:
    if n % 5 == 0:
        print(n)
    n += 1

# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8

n = 500
while n < 1001:
    if n % 5 == 0 and n % 8 == 0:
        print(n)
    n += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
n = 500
while n < 1001:
    if n % 5 == 0 or n % 8 == 0:
        print(n)
    n += 1

'''
S1 : REQUIREMENT : Print numbers which are divisible by 4 between 0 to 100

S2,S3 :Analysis,Design:
-----------------------
Step1: Take the user input,iterate till upper limit
Step2: Check whether the value divisible by 4 or not
Step3: If True, print the value
'''

# 0 1 2 3 4 5 6 7 8 9 10... 100

n = 1
while n < 101:
    if n % 4 == 0:
        print(n, " is divisible by 4")
    n += 1

'''
# S1: REQUIREMENT : Print numbers which are divisible by 
                    either 3 or 8 between 1 to 1000
'''
print("-------------either 3 or 8 between 1 to 1000-------------")

n = 1
while n < 1001:
    if n % 3 == 0 or n % 8 == 0:
        print(n, " is divisible by 3 or 8")
    n += 1

'''
# S1: REQUIREMENT : Print numbers which are 
                    divisible by 5 and 10 between 1 to 100
'''
print("---------either 5 and 7 between 1 to 100-------------")

n = 1
while n < 101:
    if n % 5 == 0 or n % 10 == 0:
        print(n, " is divisible by 5 or 10")
    n += 1

'''
Print numbers f
1 - 5
2 - 10
3 - 15
4 - 20
5 - 25
6 - 30
'''
# 1 - 5
n = 1
while n < 6:
    print("Numbers betweeen 1 to 5 is :", n)
    n += 1

# 2 - 10

n = 2
while n < 11:
    print("Numbers between 2 and 10 is ", n)
    n += 1

# 3 - 15
n = 3
while n < 16:
    print("Nembers between 3 to 15 is :", n)
    n += 1

# 4 - 20
n = 4
while n < 21:
    print("Nember between 4 and 20 is : ", n)
    n += 1

# 5 - 25
n = 5
while n < 26:
    print("Number between 5 and 25 are : ", n)
    n += 1

# 6 - 30
n = 6
while n < 31:
    print("Number between 6 and 30 is : ", n)
    n += 1
