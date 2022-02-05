"""
1. index() : method returns the index of a substring inside the string (if found).
If the substring is not found, it raises an exception.
"""

print("------------- 5. index() -----------------")
print("index() : returns the index of a substring inside the string")

print("*************")

str1 = "My name is ali"
print("Normal String is:", str1)

print("The index of name is:", str1.index("name"))

'''The only difference between find() and index() in find() if the string is not found it returns -1
but in index() it raises exception'''

'''print(str1.index("an")) # It raises exception because an is not present in the string'''

# string.count(value, start, end)
'''
value:	A String. The string to value to search for
start:	An Integer. The position to start the search. Default is 0
end:	An Integer. The position to end the search. Default is the end of the string
'''

str1 = "My name is ali"

print("The index of i is", str1.index('i', 4, 11))  # i position between 4 to 11 is 8 here.

'''print(str1.index('I'))-----> it will produce exception because it is case sensitive'''
