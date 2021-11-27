"""
rindex( str, beg=0, end=len(string))
Same as index(), but search backwards in string.

"""

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

# Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."

x = txt.rindex("e")

print(x)
