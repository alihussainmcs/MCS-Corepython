# Passing Arguments

"""
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
"""

# 1. Positional arguments (Required arguments)
print("--------1. Positional arguments--------------")


def sum(n1, n2, n3):  # sum(int n1, int n2, int n3) sum(int n1, String n2, List n3)
    print("In sum method with values :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)


sum(10, 20, 30)


# sum(10, 20)          # TypeError: sum() missing 1 required positional argument: 'n3'3#
# sum(10, 20, 30, 40)    # TypeError: sum() takes 3 positional arguments but 4 were given


def sub(a, b, c):
    print('Given values :', a, b, c)
    print('Subtraction is :', a - b - c)


# sub(11,10)  TypeError: sub() missing 1 required positional argument: 'c'

sub(11, 1, 2)

# sub(11, 2, 4, 5) TypeError: sub() takes 3 positional arguments but 4 were given


# 2. Default arguments
print("--------2. Default arguments-------------")


def sum(n1, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ", res)


sum(10, 20)
sum(10, 20, 30)  # n3 = 1000, n3 = 30


# sum(10)  #TypeError: sum() missing 1 required positional argument: 'n2'
# sum(10, 20, 30, 40) # TypeError: sum() takes from 2 to 3 positional arguments but 4 were given


def sub(a, b, c=1):
    print('Given values :', a, b, c)
    print('Subtraction is :', a - b - c)


sub(11, 9)

sub(11, 1, 2)


# sub(11, 2, 4, 5) TypeError: sub() takes 3 positional arguments but 4 were given


def sum(n1, n2=500, n3=1000):
    res = n1 + n2 + n3
    return res


print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))


# print("Zero argument    :",sum())
# print("Extra arguments  :",sum(10,20,30,40))


def sub(a, b=1, c=4):
    return a - b - c


print("One argument     :", sub(10))
print("Two argument     :", sub(10, 20))
print("Three argument   :", sub(10, 20, 30))
# print("Zero argument    :",sub())            TypeError: sub() missing 1 required positional argument: 'a'
# print("Extra arguments  :",sub(10,20,30,40)) TypeError: sub() takes from 1 to 3 positional arguments but 4 were given

'''
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
'''

# 3. Keyword argument (Named argument)
print("--------3. Keyword argument-------------")


def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum is : ", res)


sum(10, 20, 30)  # 1.Positional/Required
sum(n2=10, n3=20, n1=30)


def sum(n1, n2, n3=45):
    res = n1 + n2 + n3
    print("Sum is : ", res)


sum(10, 20, 30)  # Positional
sum(n2=10, n3=20, n1=30)  # Keyword
sum(n2=10, n1=30)  # Default + Keyword
sum(n1=30, n2=10)  # Default + Keyword


def sub(a, b, c=1):
    print('Subtraction is :', a - b - c)


sub(1, 2, 3)  # Positional
sub(a=3, b=2, c=1)  # Keyword
sub(b=4, a=2)  # Default + Keyword
