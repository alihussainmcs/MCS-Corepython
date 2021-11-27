"""
istitle()
Returns true if string is properly "titlecased" and false otherwise.

"""

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)
print(".........................................")
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
e = "2 Abc 6536625 jksvkhjef"
f = "2 Abc 6536625 Jksvkhjef"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
print(e.istitle())
print(f.istitle())
