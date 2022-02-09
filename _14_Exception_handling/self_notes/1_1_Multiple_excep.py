"""
Traceback (most recent call last):
File "C:/Users/0_sir_notes/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_1_Exception_handling.py",
  line 6, in <module>
    print("Division :", x / y)
ZeroDivisionError: division by zero

"""

'''
HANDLING MULTIPLE EXCEPTIONS
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value:"))  # ValueError
    li = [1, 2, 3, 4]
    print("List data :", li[3])  # IndexError
    print("Division :", x / y)  # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except ValueError as ve:
    print("** Value Error : **", ve)
except IndexError as ie:
    print("** Index Error : **", ie)
except ZeroDivisionError as zde:
    print("** Zero Division Error : **", zde)

print("End of program")
print("---Remaining code---")  # remaining piece of code

'''
Program Execution Flow:
-----------------------
Exception didn't happen :  1. Statements before try block
                           2. Statements in try block(ALL)
                           3. Statements after except block

Exception occurred       :  1. Statements before try block
                           2. Statements in try block,till the line of exception occurrence
                           3. Statements in except block
                           4. Statements after except block     

 - Python at a time,handles only one exception
 - If there is chance of multiple exceptions,handle using multiple except blocks
 -                 
'''

print("===================================================================")

try:
    # this will throw an exception if the file doesn't exist.
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close()

print("===================================================================")
try:
    a = 10 / 0
except(ArithmeticError, IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

print("===================================================================")


def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

