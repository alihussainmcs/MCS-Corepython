"""
splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

"""
# string.splitlines(keeplinebreaks)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)
