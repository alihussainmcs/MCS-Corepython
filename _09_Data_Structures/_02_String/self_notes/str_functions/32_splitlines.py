"""
splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

"""
# string.splitlines(keeplinebreaks)

txt = "Thank you for the music\nWelcome to the jungle"

print(txt)

print()

x = txt.splitlines()

print(x)

print()

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)
