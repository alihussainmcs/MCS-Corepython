"""
String Functions:
-----------------
"""

# 1. capitalize() :: Returns a string where the first character is upper case.

print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")
print(".....Case 1.....")
msg = "sequence of characters"
print("Normal string  :", msg)

print("String after capitalize:",  msg.capitalize())


'''returns a string with the first letter capitalized and all other characters lowercase'''

print(".....Case 2.....")

msg1 = "sequence of Characters"
print("Normal string  :", msg1)
print("String after capitalize:",  msg1.capitalize())

'''In this case non alphabets is going to be the first character in the string'''

print(".....Case 3.....")

msg3 = "+ operator is used in the arithmetic operation"

print("Normal string:   ", msg3)  # both the outputs are same here because the sentence starts with an operator
print("String after capitalize:   ", msg3.capitalize())
