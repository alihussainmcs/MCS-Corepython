# Control statements : break continue pass
# Will use control statements in  while for loops
"""
REQ: Print first 7 even numbers betweeen 1 to 100
    1. Get all numbers from 1 to 100
    2. Filter only even numbers
    3. Get only first 7 even numbers

            1    2  3  4  5  6  7  8  9 10
            11  12 13 14 15 16 17 18 19 20
            21  22 23 24 25 26 27 28 29 30......

            first 3 even numbers
                    solution                   roguht work                      count
              | 2 4 6 8 10 12 14        | 1%2 == 0 2%2 == 0                  3
                                          3%2 == 0 4%2 == 0
                                          5%2 == 0 6%2 == 0  Stops here
                                          7%2 == 0  8%2 == 0  XXX
"""

'''Steps:     1. Get all numbers from 1 to 100
              2. Filter only even numbers
              3. Get only first 7 even numbers
1.  Print numbers  between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''

n = 1
count = 0
print(" The First 7 even numbers between 1 to 100 are : ")
while n <= 100:
    if n % 2 == 0:
        print(n)
        count += 1
    if count == 7:
        break
    n += 1

print("End of the while loop ")
"""
REQ : Print 7 even numbers between 50 to 80
Approach
    1. Print number between 50 to 80
    2. Get even number between 50 to 80
    3. break 7 number from seqence of even numbers 
"""

n = 50
count = 0
print("First 7 even numbers between 50 to 80 are : ")
while n <= 80:
    if n % 2 == 0:
        print(n)
        count += 1
    if count == 7:
        break
    n += 1
print("...........Loop End...............")

"""
REQ: Find first 3 numbers which are divisible by 3 between 500 to 1000
Approach : 
            1. Print all numbers between 500 to 1000
            2. Get all numbers which are divisible by 3 between 500 to 1000
            3. Get first 3 numbers divisible by 3 between 500 to 1000
            
"""


n = 500
count = 0
print("First 3 number divisible by 3 between 500 to 1000 are : ")
while n <= 1000:
    if n % 3 == 0:
        print(n)
        count += 1
    if count == 3:
        break
    n += 1
print("..............Loop End...............")