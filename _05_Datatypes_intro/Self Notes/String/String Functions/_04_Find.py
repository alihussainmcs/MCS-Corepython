# 4. find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

print("------------- 4. find() -----------------")

print("find() : method finds the first occurrence of the specified value")
print("************")

str1 = "python is a good language"

print("The normal String is:", str1)

print("The index of a in the given string is", str1.find('a'))    # output here is 10 because index of 'a' is 10

print("The index of a in the given string is", str1.find('z'))    # output here is -1 because 'z' is not present in str1

'''Finding a character within the string from desired positions'''

# string.find(value, start, end)

'''
value:	The value to search for
start:	Where to start the search. Default is 0
end:    Where to end the search. Default is to the end of the string
'''
print("The number of times alphabet o repeated is:", str1.find('o', 2, 16))

print("The number of times alphabet O repeated is:", str1.find('O', 2, 16))

# Here in the above example_1 the output is -1 because capital O is given it is case sensitive

str1 = "python is a good language"

print('The index value of good is:', str1.find('good'))

# Here in the above example_1 the output is 12 because g index is 12 so it will show the starting letter index in output

print("The python present in the string or not:", "python" in str1)

# Used to check whether the word is present in string or not.
