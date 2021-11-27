# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

'''
RegEx Functions

The re module offers a set of functions that allows us to search a string for a match:

1. findall :	Returns a list containing all matches
2. search  :	Returns a Match first occurrence object if there is a match anywhere in the string
3. split   :	Returns a list where the string has been split at each match
4. sub     :	Replaces one or many matches with a string
'''
# Returns every occurrence in the txt

print("____findall function___")
import re

txt = "The rain in Spain"
x = re.findall("i", txt)
print(x)
# Returns every occurrence in the txt
# if no matches found returns empty list


print("_____ search() Function______")

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

import re

txt = "The rain in Spain"
x = re.search("a", txt)

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned

print("____split() Function____")

# The split() function returns a list where the string has been split at each match

import re

txt = "The rain in Spain"
x = re.split("\s", txt)  # \s 	Returns a match where the string contains a white space character
print(x)

# You can control the number of occurrences by specifying the max split parameter
# Split the string only at the first occurrence:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)

print("____sub() Function___")

# The sub() function replaces the matches with the text of your choice

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#  You can control the number of replacements by specifying the count parameter
# Replace the first 2 occurrences:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 1)
print(x)

# Match Object
'''
A Match Object is an object containing information about the search and the result.If there is no match,
the value None will be returned, instead of the Match Object.


The Match object has properties and methods used to retrieve information about the search, and the result:

1.span():  returns a tuple containing the start-, and end positions of the match.
2.string:  returns the string passed into the function
3.group(): returns the part of the string where there was a match
'''

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

print("____using span_________")

txt = "The rain in Spain"
x = re.search(r"\br\w+", txt)
# \b 	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# \w 	Returns a match where the string contains any word characters (characters from
# a to Z, digits from 0-9, and the underscore _ character)
print(x.span())

print("____using string_________")

# Print the string passed into the function:

txt = "The rain in Spain"
x = re.search(r"\br\w+", txt)
print(x.string)

# The string property returns the search string


print("____using group_________")
# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Search for an upper case "S" character in the beginning of a word, and print the word


'''

Metacharacters

Metacharacters are characters with a special meaning:

[] 	A set of characters 	          "[a-m]" 	
\ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
. 	Any character (except newline character) 	"he..o" 	
^ 	Starts with 	"^hello" 	
$ 	Ends with 	"planet$" 	
* 	Zero or more occurrences 	      "he.*o" 	
+ 	One or more occurrences 	      "he.+o" 	
? 	Zero or one occurrences 	"he.?o" 	
{} 	Exactly the specified number of occurrences 	"he{2}o" 	
| 	Either or 	"falls|stays" 	
() 	Capture and group


Special Sequences

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\A 	    Returns a match if the specified characters are at the beginning of the string 	"\AThe" 	
\b  	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\bain"
r"ain\b" 	

\B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\Bain"
r"ain\B" 	

\d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d" 	
\D 	Returns a match where the string DOES NOT contain digits 	"\D" 	
\s 	Returns a match where the string contains a white space character 	"\s" 	
\S 	Returns a match where the string DOES NOT contain a white space character 	"\S" 	
\w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the 
            underscore _ character) 	"\w" 	
\W 	Returns a match where the string DOES NOT contain any word characters 	"\W" 	
\Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z" 	

'''
