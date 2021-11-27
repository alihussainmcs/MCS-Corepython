"""
maketrans()
Returns a translation table to be used in translate function.

"""

txt = "Hello Sam!"
my_table = txt.maketrans("S", "P")
print(txt.translate(my_table))

print("..........................")
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
my_table = txt.maketrans(x, y)
print(txt.translate(my_table))

print("..........................")
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
