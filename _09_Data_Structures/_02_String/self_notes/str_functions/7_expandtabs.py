"""
expandtabs(tabsize=8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

"""
txt = "H\te\tl\tl\to"

x = txt.expandtabs(12)

print(x)

print()

txt = "H\te\tl\tl\to"

print(txt)

print()

print(txt.expandtabs())

print()

print(txt.expandtabs(2))

print()

print(txt.expandtabs(4))

print()

print(txt.expandtabs(10))
