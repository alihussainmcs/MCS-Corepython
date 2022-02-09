"""
Traceback (most recent call last):
  File "C:/Users/0_sir_notes/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling
                            /_1_1_Exception_handling.py", line 6, in <module>
    print("Division :", x / y)
ZeroDivisionError: division by zero
"""
print("Start of program")
"""
try:
    print("----While Exception handling----")
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value:"))
    print("Division :", x / y)  # ZeroDivisionError("division by zero")
    list1 = [1, 2, 3, 4]
    print("List value : ", list1[10])  # IndexError("....")
    print("Hello world")
    print("---------------------------------")
except ValueError as ve:
    print("** ERROR : Please enter numbers for num/den values **", ve)
    # print(ve)
except ZeroDivisionError as zde:
    print("** ERROR : Please enter den. value other than 0 **", zde)
except IndexError as ie:
    print("** ERROR : Given index value doesnt exists **",ie)

print("----Remaining code----")  # remaining piece of code

"""

number1 = 100
number2 = 10

# Division by zero is being done
# encapsulating the doubtful code in try clause
try:
    quotient = number1 / number2
    print("Quotient is {}".format(quotient))

    data = "Sellouts"
    # data.get('name')

    # defining an array
    myList = [1, 2, 3, 4, 5, 6]
    print(myList[20])

except ZeroDivisionError:
    print("Division by zero is being performed")
except AttributeError:
    print("Attribute Error Occurred")
except IndexError:
    print("Index out of range error")

print("-------------------------------------------------------------")


number1 = 100
number2 = 0

# Division by zero is being done
# encapsulating the doubtful code in try clause
try:
    quotient = number1 / number2
    print("Quotient is {}".format(quotient))

    data = "Sellouts"
    # data.get('name')

    # defining an array
    myList = [1, 2, 3, 4, 5, 6]
    print(myList[20])

except ZeroDivisionError:
    print("Division by zero is being performed")
except AttributeError:
    print("Attribute Error Occurred")
except IndexError:
    print("Index out of range error")
