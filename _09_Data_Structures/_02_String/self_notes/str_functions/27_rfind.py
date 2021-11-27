"""
rfind(str, beg=0,end=len(string))
Same as find(), but search backwards in string.

"""

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)
print("............................................")
txt = "Hello, welcome to my world."

print(txt.rfind("q"))
