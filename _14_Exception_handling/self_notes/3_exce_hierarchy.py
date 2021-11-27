try:
    n = 0
    m = 3
    c = m / n
except ZeroDivisionError as e:
    print("The zero can't be divided")
try:
    n = 2
    m = 'HEllo'
    p = m + n
except TypeError:
    print('The number is in the string format')
try:
    from cv import pandas
except Exception:
    print("improper module")

print("-------------------------------------------------------")

try:
    print(x)
except TypeError:
    print("x is not defined")
except:
    print("Error")
try:
    print(a + b)
except:
    print("exception occured")
try:
    print(hello)
except SyntaxError as e:
    print("Invalid syntax")
except:
    print("Invalid syntax")

print("-------------------------------------------")


class CashNotInRangeError(Exception):
    def __init__(self, cash, message="Cash is not in (2000, 1000) range"):
        self.cash = cash
        self.message = message
        super().__init__(self.message)


cash = int(input("Enter cash: "))
if not 2000 < cash < 1000:
    raise CashNotInRangeError(cash)

print("-------------------------------------------------------------------")

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
