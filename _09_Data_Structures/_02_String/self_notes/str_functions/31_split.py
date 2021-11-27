"""
split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and returns list of substrings; split
into at most num substrings if given.

"""
# Syntax : str.split(separator, maxsplit)
txt = "welcome to the jungle"

x = txt.split()

print(x)


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
