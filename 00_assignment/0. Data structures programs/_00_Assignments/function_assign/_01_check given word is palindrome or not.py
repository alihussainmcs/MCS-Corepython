# P01. check given word is palindrome or not
"""
          A string is said to be palindrome if the reverse of the string is the same as string. For example,
                “radar” is a palindrome, but “radix” is not a palindrome.
"""

"""
1. CRUD       -->  Create
2. STATE      -->  string
3. BEHAVIOR   -->  str  |   for  |  +=
"""

# 0. Mathematics
"""
str_1 = 'radar' 
we want to know the reverse of string str_1 is same or not
Expected output : 'radar' is same as reverse of the str_1
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
str_1 = 'radar'
print("Given string : ", str_1)
print('Reverse of the string :', str_1[::-1])
print("given string is palindrome string ")
print()
str_2 = 'radix'
print("Given string : ", str_2)
print('Reverse of the string :', str_2[::-1])
print("given string is not palindrome string ")

# 2. Algorithm
print("--------2 Algorithm              ----------")
print("Given string : ", str_1)
str_rev = ''
for i in str_1[::-1]:
    str_rev += i

print('Reverse of the string :', str_rev)
print("given string is palindrome string ")

# 3 Using Functions
print("--------3 Using Functions        ----------")


def str_rev(str_3):
    print("Given string : ", str_3)
    print('Reverse of the string :', str_3[::-1])
    if str_3 == str_3[::-1]:
        print("given string is palindrome string ")
    else:
        print("given string is not palindrome string ")


str_rev(str_1)
print()
str_rev(str_2)

# 4 OOPS
print("--------4 Object Oriented        ----------")


class StringReverse:
    def __init__(self, str_4):
        self.str_4 = str_4

    def string_rev(self):
        print("Given string :", self.str_4)
        print('Reverse of the string :', self.str_4[::-1])

        if self.str_4 == self.str_4[::-1]:
            print("given string is palindrome string ")
        else:
            print("given string is not palindrome string ")


str_rev_1 = StringReverse(str_1)
str_rev_1.string_rev()

# 5 Exception handling
print("--------5 Exception handling     ----------")

try:
    print("Given string :", str_1)
    print('Reverse of the string :', str_1[::-1])
    if str_1 == str_1[::-1]:
        print("given string is palindrome string ")
    else:
        print("given string is not palindrome string ")

except Exception as ex:
    print("Exception part ! ", ex)

print()
try:
    str_1 = 1010
    print("Given string :", str_1)
    print('Reverse of the string :', str_1[::-1])
    if str_1 == str_1[::-1]:
        print("given string is palindrome string ")
    else:
        print("given string is not palindrome string ")
except TypeError as te:
    print("Exception part ! ", te)
finally:
    pass

# 6 File Handling
print("--------6 File Handling          ----------")
data_1 = open('sample.txt')
lines = data_1.readlines()


def str_pal(str_a):
    print("Given String :", str_a)
    print('Reverse of the string :', str_a[::-1])
    if str_a == str_a[::-1]:
        print("given string is palindrome string ")
    else:
        print("given string is not palindrome string ")


str_pal(lines[0].strip())
print()
str_pal(lines[1].strip())

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
