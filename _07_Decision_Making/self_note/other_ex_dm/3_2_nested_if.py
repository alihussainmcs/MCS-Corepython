"""
1.Find grade of a student based on below requirement.
marks >= 80  => A+  , 60-79 => A,  50-60=> B, 35-50 => C,  Below 35 FAIL
if  elif elif elif   else
"""

print(".................Student Grade .....................................")

marks = 75  # int(input("Enter your marks : "))

if 0 <= marks <= 100:
    if marks >= 80:
        print("A+ Grade")
    elif 60 <= marks < 80:
        print("A Grade ")
    elif 50 <= marks < 60:
        print("B Grade ")
    elif 35 <= marks < 50:
        print("C Grade ")
    else:
        print("Fail")
else:
    print("Enter a number between 0 and 100")


i = 20
if i < 15:
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")

print()


i = 10
if i == 10:

    #  First if statement
    if i < 15:
        print("i is smaller than 15")

    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
