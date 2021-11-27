"""
1.Find grade of a student based on below requirement.
marks >= 80  => A+  , 60-79 => A,  50-60=> B, 35-50 => C,  Below 35 FAIL
if  elif elif elif   else
"""

print(".................Student Grade .....................................")

marks = int(input("Enter your marks : "))

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
