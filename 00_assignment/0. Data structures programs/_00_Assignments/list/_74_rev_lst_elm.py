"""
Reverse list of elements and print in upper case
"""

lst = ['python', 'world', 'green']
print('Original List :', lst)
upr = []

for i in lst[::-1]:
    upr.append(i.upper())

print('Reverse list of elements and print in upper case :', upr)
