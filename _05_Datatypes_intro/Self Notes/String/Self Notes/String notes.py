"""
STRINGS:
-------
String is a collection of alphabets, words or other characters.
It is one of the primitive data structures and are the building blocks for data manipulation.
Python has a built-in string class named str .
Python strings are "immutable" which means they cannot be changed after they are created.
"""
'''
Assign String to a Variable:
---------------------------
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Example:
--------
'''

a = "Hello"
print(a)

'''
Positive String Indexing:
---------------
Strings are ordered sequences of character data.
Indexing allows you to access individual characters in a string directly by using a numeric value. 
String indexing is zero-based: the first character in the string has index 0, the next is 1, and so on.
Index Value normally starts from 0 and spaces between the words are also considered in the index.

Example:'''

str0 = "Welcome to python programming"

print(".......Positive Indexing.......")

print("The First Character is:  " + str0[0])  # prints the first character.
print("The Last Character is:  " + str0[28])  # prints the last character.

'''
Negative String Indexing:
-----------------
Negative indexes to start the slice from the end of the string
'''

str1 = "Hello everybody"

print(".......Negative Indexing.......")

print("The second character from the Last is:  " + str1[-2])
print("The sixth character from the Last is:  " + str1[-6])

'''
String Slicing:
--------------
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''

str2 = "python is very easy to learn"

print("Get the characters from position 2 to position 5:  " + str2[2:9])
print("Get the characters from the start to position 4:  " + str2[:4])
print("Get the characters from position 2 to the end:  " + str2[2:])

msg = "Python Developer "

print('Length of msg :', len(msg))
