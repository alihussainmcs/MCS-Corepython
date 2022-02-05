"""
zfill (width)
Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any
sign given (less one zero).

"""

# Fill the string with zeros until it is 10 characters long:

txt = "50"

x = txt.zfill(10)

print(x)

print()

# Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))

print()

print(b.zfill(10))

print()

print(c.zfill(10))
