
mg = 'hi hello hi hello hi hi '

# index(str, beg=0, end=len(string))

print(' index(str, beg=0, end=len(string)) ')

print()

print(" Same as find(), but raises an exception if str not found ")

print()

print(" Using index function ", mg.index('hi', 0, len(mg)))

print()

print(" Using index function ", mg.index('hello', 0, len(mg)))

# print(" Using find function ", mg.index('py', 0, len(mg))) ValueError: substring not found
