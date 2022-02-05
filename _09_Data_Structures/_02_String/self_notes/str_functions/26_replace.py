"""
replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max occurrences if max given.

"""
print("String replace() function practice ")
msg = 'pip install'
stg = """console"""

print('Given string :', '\n', msg, '\n', stg)
print("The replace of the msg to stg string is :", msg.replace(msg, stg))

print("The replace of the stg to msg string is :", stg.replace(stg, msg))
