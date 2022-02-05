"""
strip([chars])
Performs both lstrip() and rstrip() on string.
"""
# string.strip(characters)
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

print()

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

print()

txt = '   yaman   '
x = txt.strip()

print(x)

print()

txt = "reerrererer,,,,,,.....banana...hhhhggggg"

x = txt.strip(",.ghre")

print(x)
