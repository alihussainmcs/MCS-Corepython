"""
isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise.

"""

txt = "565543"

x = txt.isnumeric()

print(x)

a = "\u0030"  # unicode for 0

b = "\u00B2"  # unicode for &sup2

c = "10km2"

d = "-1"

e = "1.5"

print()

print(a.isnumeric())

print()

print(b.isnumeric())

print()

print(c.isnumeric())

print()

print(d.isnumeric())

print()

print(e.isnumeric())
