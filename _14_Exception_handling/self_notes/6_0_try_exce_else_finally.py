"""
'''
@author: 0_sir_notes
'''
try:
    print("In try block")
    a=10/0
    print("Hello world",a)
except Exception as e:  # Exception e = ZeroDivisionError("Division by zero")  # 3 Upcasting
    print("I am in  Exception")
else:
    print("ELSE Block :Successfully Done")
finally:
    print("Finally")

print("------------------------")
try:
    num1 =int(input("Enter num1"))
    num2 =int(input("Enter num2"))
    print("----Before---")
    a = num1/num2
    print("----After---")
    print("The value of a =",a)
except:
    print("Please enter value other than 0 for num2")
else:
    print("Successfully Done")
finally:
    print("-----Closing operations here----")

print("-------------------------------")

ae = ZeroDivisionError("division by zero")

'''
result = 10/0
print("Hello World")
'''
try:
    print("----in try block------")
    result = 10/0
    print("Division result ",result)
except ZeroDivisionError as zero_div_error:
    print("You are trying to divide by Zero.Pleaes enter value other than 0 : ",zero_div_error)
else:
    print("Welcome.Your Program execution is success")
finally:
    print("Finally block")

print("------------------------------------")

'''

try:
    print("Before in TRY")
    result = 10/0
    print("In TRY :: Division result ",result)
    print("In EXCEPT :: You are trying to divide by Zero.Please enter value other than 0 : ")
else:
    print("In ELSE :: Welcome.Your Program execution is success")
finally:
    print("In FINALLY :: Finally will be executed irrespective of Exception")


# Once exception happens,further statements will not be executed in try block
# Exception  ---- try except finally
# No Exception -- try else   finally
'''
"""

try:
    print(python)
except NameError:
    print("python is not defined")
try:
    list = [1, 2, 3]
    print(list[5])
except IndexError as e:
    print(e)
print("index error")
try:
    from cv import numpy
except Exception:
    print("improper module")
try:
    print(hello)
except:
    print("hello is not defined")
finally:
    print(" The finally is executed")
try:
    print(chair)
except NameError:
    print("NameError:'cot' is not defined")
else:
    print("word found no error")
