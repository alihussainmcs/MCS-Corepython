"""
endswith(suffix, beg=0, end=len(string))

Determines if string or a substring of string (if starting index beg and ending index end are given)

ends with suffix; returns true if so and false otherwise.

"""
# string.endswith(value, start, end)
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

print()

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

print()

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)
