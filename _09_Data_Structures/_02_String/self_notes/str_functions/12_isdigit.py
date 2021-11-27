"""
isdigit()
Returns true if string contains only digits and false otherwise.

"""

txt = "50800"

x = txt.isdigit()

print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = 'amara'
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())
