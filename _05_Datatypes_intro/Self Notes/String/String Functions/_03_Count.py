# 3. The count() method returns the number of occurrences of a substring in the given string.


print("------------- 3. count() -----------------")

print("count() : Returns the number of times a specified value occurs in a string")

print("************************")

txt = "Python is an awesome language"
print("Normal String is:", txt)
txt1 = txt.count("Python")
print("The Count of Python in the sentence is:", txt1)
print("The count of e in the sentence is:", txt.count("e"))
print("The count of y in the sentence is:", txt.count("y"))
print("The count of p in the sentence is:", txt.count("p"))
print("The count of w in the sentence is:", txt.count("w"))
print("The count of n in the sentence is:", txt.count("n"))


# string.count(value, start, end)
'''
value:	A String. The string to value to search for
start:	An Integer. The position to start the search. Default is 0
end:	An Integer. The position to end the search. Default is the end of the string
'''

txt = "Python is an awesome language"
txt2 = txt.count("a", 5, 24) # it shows the count of alphabet a from position 5 to 24.
print("The Count of a in the sentence from position 5 to 24 is:", txt2)