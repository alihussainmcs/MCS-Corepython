"""
lstrip()
Removes all leading whitespace in string.

"""

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

print()

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
