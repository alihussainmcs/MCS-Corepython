from pip._vendor.distlib.compat import raw_input


class WithDrawException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    amount = int(raw_input("Enter your Amount to withdraw : "))
    print("Your entered amount is ", amount)
    if amount == 100 or amount == 200 or amount == 500 or amount == 2000 or amount % 500 == 0:
        print("You can withdraw Amount ", amount)
    else:
        raise WithDrawException(amount)
except WithDrawException as custExec:
    print("Please enter amount multiples of 500 and not :", custExec)
finally:
    print("Your current transaction process completed")

print("-------------------------------------------------------------------------")


number1 = 100
number2 = 100

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
