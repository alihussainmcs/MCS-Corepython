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

my_table = txt.maketrans(x, y, z)

print(txt.translate(my_table))


# example dictionary
dict1 = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict1))

# example dictionary
dict2 = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict2))
