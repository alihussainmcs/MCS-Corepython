# Boolean   True 1   False 0

x = True
print("Value of x: ", x)
x = False
print("Value of x: ", x)

# Logical gate ===> and or not

# OR operator:
# Guest   Coffee or Tea
print("OR 1 :", True or False)
print("OR 2 :", False or True)
print("OR 3 :", True or True)
print("OR 4 :", False or False)
print("-----------------------")
# Guest Water and Coffee
print("AND 1 :", True and False)  # False
print("AND 2 :", False and True)  # False
print("AND 3 :", True and True)   # True
print("AND 4 :", False and False)  # False


# not
not True  # False
not False  # True

'''
condition1   AND/OR    condition2   AND/OR  condition3

condition
not condition

'''
print("Cond 1:", 10 > 20 and 5 < 2)  # False and False ==> False
print("Cond 2:", 10 < 20 and 5 > 2)  # True and True  ==> True
print("Cond 3:", not 5>2)
