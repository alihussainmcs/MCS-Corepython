"""
ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a total of width columns.

"""

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

print()

txt = "banana"

x = txt.ljust(20, "O")

print(x)
