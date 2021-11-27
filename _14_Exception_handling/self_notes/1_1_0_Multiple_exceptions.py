"""
# Without EH
print("Start of program")
x = int(input("Enter numerator value :"))   # ValueError
y = int(input("Enter denominator value:"))  # ValueError
li = [1,2,3,4]
print(li[3])   # IndexError
print("Division :", x / y)  # ZeroDivisionError
print("Hello world")
print("---------------------------------")
"""

# Handling multiple exceptions
'''
HANDLING MULTIPLE EXCEPTIONS

To handle multiple exceptions,write multiple except blocks
Below code is not proper 
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError
    y = int(input("Enter denominator value:"))
    li = [1, 2, 3, 4]
    print("List val:", li[2])  # IndexError
    print("Division :", x / y)  # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except Exception as e:
    print("** Error occurred :  **", e)
'''
except:
    print("** Error occurred :  **")

    5L Water <-- 1L 2L 2.5L 3L 3.5L 4L 5L

    Animal  a = Tiger()   5L CAN <---- 2L Water
    Animal  a = Lion()
    Animal  a = Cat()
    Animal  a = Dog()
'''

print("------------------------------------------------------------------------")

try:
    f = open("myfile.txt")
    try:
        f.write("Locum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

print("-------------------------------------------------")
'''
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")  # raise Exception("Sorry, no numbers below zero")
'''

print("---------------------------------------------------------")

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print("a/b = %d" % c)
    # Using exception object with the except statement
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")
