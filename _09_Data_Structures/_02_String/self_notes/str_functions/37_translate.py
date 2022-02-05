"""
translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string.

"""

# Replace any "S" characters with a "P" character:

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
my_table = {83:  80}
txt = "Hello Sam!"
print(txt.translate(my_table))

print()

# Use a mapping table to replace "S" with "P":

txt = "Hello Sam!"
my_table = txt.maketrans("S", "P")
print(txt.translate(my_table))

print()


# Use a mapping table to replace many characters:

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
my_table = txt.maketrans(x, y)
print(txt.translate(my_table))

print()

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

print()

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))
