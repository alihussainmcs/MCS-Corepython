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

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
