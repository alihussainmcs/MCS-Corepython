"""
rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a total of width columns.

"""

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

print()

# Using the letter "O" as the padding character:

txt = "banana"

x = txt.rjust(20, "O")

print(x)
