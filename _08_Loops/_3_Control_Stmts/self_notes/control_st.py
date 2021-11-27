# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:43:34 2021

@author: ali hussain
"""

# Control statements : break continue pass
# Will use control statements in  while for loops
'''
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
'''

'''Steps:     1. Get all numbers from 1 to 100
              2. Filter only even numbers
              3. Get only first 7 even numbers
1.  Print numbers  between 1 to 100
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
print("..........Break..........................")
count=0
for i in range(1,101):
    if i%2==0:
       count+=1
       print(i)       
       if count==7:
           break
    else:
        pass


# Print even numbers between 50 to 80
for i in range(50,81):
    if i%2==0:
        print("The even number between 50 and 80 are : ", i)
    else:
        pass
    

'''
REQ: Find first 3 numbers which are divisible by 3 between 500 to 1000
501
504
507                  500 501 502 503 504 505 506 507 508   3



1. Print numbers bw 500 to 1000
2. Filter divisible by 3 
3. Break the loop once we get 15 count
'''
print(".......Printing 1st three number divisible by 3 between 500 to 1000 ............")
count=0
for i in range(500,1001):
    if i%3==0:
        count+=1
        print(i)
        if count==3:
            break
print("........End of loop ..................")        
    

print("------Continue---------")
# continue
'''
REQ:  # Numbers between 1 to 1000 which are divisble by 5.
      # If value is also divisible by 10 don't display it.
'''

for i in range(1,1001):
    if i % 5 == 0 :
        if i % 10 == 0 :            
            continue
        print(i)
        
'''
break    : 1. Remaining stmts will not be executed
           2. It breaks the loop and come out of it 
           
continue : 1. It will skip remaining stmts, will go to next iteration
pass     :
'''
'''
if True:
    pass

while True:
    pass

for each in range(1,100):
    pass

print("Hello")
'''


# if elif else while for break continue pass

print("-------- Even numbers -------------")
# Print only first 3 even numbers between 1 to 50
#1st
count=0
lst=[]
for i in range(1,51):
    if i % 2 == 0:
        lst.append(i)
        count+=1
   # if count==3:
print(lst[0:3])
 
#2nd
count=0
for i in range(1,51):
    if i % 2 == 0:
        count+=1
        print(i)
        if count==3:
            break
 


print("------Both continue break -----")

# Print even numbers.Skip first 3 even numbers and after 7th even number onwards
count=1
for i in range(1,51):
    if i%2==0:
        count+=1
        if count<=4:
            continue
        print(i)
        if count>7:
            break
        
        
# Find even numbers count in list and print it
print("----Even number count---------")
list1 = [3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2]
count=0
for i in list1:
    if i%2==0:
        count+=1
print(" Total even number in list1 are : ",count)



print("----Even number count tuple---------")
count=0
tupl1 = (3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8)
for i in tupl1:
    if i%2==0:
        count+=1
print(" Total even number in tupl1 are : ",count)

        




if 10 < 20:
    pass


# pass can be used in all blocks
'''
if 
elif 
else 
while 
for 
function blocks 
class 
file handling 
expception hanlding
'''















