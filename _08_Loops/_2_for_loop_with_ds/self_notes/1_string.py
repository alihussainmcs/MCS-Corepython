"""
for <var> in <sequence>:
    # perform business logic
"""

print("..................For loop with String.......................")

msg = 'This is my message to you'

print("msg :", msg)
for i in msg:
    print('character in msg is ', i)

print("Printing character without space in string ")
for i in msg:
    if i == ' ':
        continue
    else:
        print('character in msg is ', i)
