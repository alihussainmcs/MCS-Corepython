"""
translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string.

"""

# Replace any "S" characters with a "P" character:

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


# Use a mapping table to replace "S" with "P":

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# Use a mapping table to replace many characters:

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
