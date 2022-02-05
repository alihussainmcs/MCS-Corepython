"""
isdecimal()
Returns true if a unicode string contains only decimal characters and false otherwise.

"""

txt = "\u0033"  # unicode for 3

x = txt.isdecimal()

print(x)

# Check if all the characters in the unicode are decimals:

a = "\u0030"  # unicode for 0
b = "\u0047"  # unicode for G

print(a.isdecimal())

print()

print(b.isdecimal())


s = "28212"
print(s.isdecimal())

print()

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

print()

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())
