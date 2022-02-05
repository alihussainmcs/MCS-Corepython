"""
startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given)
starts with substring str; returns true if so and false otherwise.

"""
# string.startswith(value, start, end)

txt = "Hello, welcome to my world."

print('String :', txt)

x = txt.startswith("Hello")
print(x)

print()

txt = "Hello, welcome to my world."

print('String :', txt)

x = txt.startswith("wel", 7, 20)
print(x)

print()

x = txt.startswith("wor", 7, 20)
print(x)
