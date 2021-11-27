# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:11:28 2021

@author: ali hussain
"""
# P01. REQ : Find length of given string   
# 1.Builtin functions

strg='hello string length : '
print(len(strg))


# 2. Algorithm

l=0
for i in strg:
    l+=1
print(l)    


# 3 Using Functions  ==> 10
   #3.0 without return
def len_str(strg):
    l=0
    for i in strg:
        l+=1
    print('length of string is : ',l)    


len_str(strg)

   #3.1 with return
def len_str(strg):
    l=0
    for i in strg:
        l+=1
    return l


len_str(strg)



'''
Python program to check whether the string is Symmetrical or Palindrome
Difficulty Level : Easy
Last Updated : 25 Sep, 2021
Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

Example: 

 Attention geek! Strengthen your foundations with the Python Programming Foundation Course and learn the basics.  

To begin with, your interview preparations Enhance your Data Structures concepts with the Python DS Course. And to begin with your Machine Learning Journey, join the Machine Learning - Basic Level Course

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
Approach 1: The approach is very naive. In the case of palindrome, a loop is run to the mid of the string and the first and last characters are matched. If the characters are not similar then the loop breaks and the string is not palindrome otherwise the string is a palindrome. In the case of symmetry, if the string length is even then the string is broken into two halves and the loop is run, checking the characters of the strings of both the half. If the characters are not similar then the loops break and the string is not symmetrical otherwise the string is symmetrical. If the string length is odd then the string is broken into two halves in such a way that the middle element is left unchecked, and the above same step is repeated.

Below is the implementation.
'''

# Python program to demonstrate
# symmetry and palindrome of the
# string
 
 
# Function to check whether the
# string is palindrome or not
def palindrome(a):
  
    # finding the mid, start
    # and last index of the string
    mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign in line 21 
    start = 0                #so that you can compare the middle elements also.
    last = len(a)-1
    flag = 0
 
    # A loop till the mid of the
    # string
    while(start <= mid):
  
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             
    # Checking the flag variable to
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
         
# Function to check whether the
# string is symmetrical or not       
def symmetry(a):
     
    n = len(a)
    flag = 0
     
    # Check if the string's length
    # is odd or even
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start1 = 0
    start2 = mid
     
    while(start1 < mid and start2 < n):
         
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
      
    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
         
# Driver code
string = 'kalkal'
palindrome(string)
symmetry(string)
'''
Output
The entered string is palindrome
The entered string is symmetrical
'''

'''
Approach 2:

We use slicing in this method.

'''
string = 'amaama'
half = int(len(string) / 2)
 
if len(string) % 2 == 0:  # even
    first_str = string[:half]
    second_str = string[half:]
else:  # odd
    first_str = string[:half]
    second_str = string[half+1:]
 
# symmetric
if first_str == second_str:
    print(string, 'string is symmertical')
else:
    print(string, 'string is not symmertical')
 
# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')


##############################################################################
#    We are given a string and we need to reverse words of a given string?

# Function to reverse words of string 
  
def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print (rev_sentence(input))
    
    


###############################################################################
# Python3 program to reverse a string
 
# Function to reverse each word in the string
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1
 
 
s = "i like this program very much"
 
# Convert string to list to use it as a char array
s = list(s)
start = 0
while True:
     
    # We use a try catch block because for
    # the last word the list.index() function
    # returns a ValueError as it cannot find
    # a space in the list
    try:
        # Find the next space
        end = s.index(' ', start)
 
        # Call reverse_word function
        # to reverse each word
        reverse_word(s, start, end - 1)
 
        #Update start variable
        start = end + 1
 
    except ValueError:
 
        # Reverse the last word
        reverse_word(s, start, len(s) - 1)
        break
 
# Reverse the entire list
s.reverse()
 
# Convert the list back to
# string using string.join() function
s = "".join(s)
 
print(s)
############### 
# Solution contributed by ali  
s = "i like this program very much"
b=s.split(' ')
print(b)
l=b[::-1]

v=' '.join(l)
print(v)

'''
Ways to remove i’th character from string in Python

In Python it is all known that string is immutable and hence sometimes poses visible
 restrictions while coding the constructs that are required in day-day programming. This
 article presents one such problem of removing i’th character from string and talks about
 possible solutions that can be employed in achieving them.
'''
s = "i like this program very much"
print(s[8])

for i in s:
    if i!=9:
        b=
        











