# Function categories
"""
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type

T T
T F
F T
F F
"""

# Sum functionality

print("------------CAT 1 -------------------")
# 1st -> T T :: Function with parameters, with return type
print(" Function with parameters, with return type")
num1 = 10
num2 = 20


def sum1(a, b):
    result = a + b
    return result


output = sum1(num1, num2)
print("Addition of Cat 1 is : ", output)

print("------------CAT 2 -------------------")

# 2nd -> T F :: Function with parameters, without return type
print("Function with parameters, without return type")


def sum2(a, b):
    res = a + b
    print("Addition of Cat 2 is :", res)


sum2(101, 201)

print("------------CAT 3 -------------------")
# 3rd --> F T :: Function without parameters, with return type
print("Function without parameters, with return type")


def sum3():
    a = 101
    b = 1001
    res = a + b
    return res


print("Sum of Cat 3 is ", sum3())


print("------------CAT 4 -------------------")

# 4th  --> F F  :: Function without parameters, without return type
print("Function without parameters, without return type")


def sum4():
    n1 = 10
    n2 = 20
    res = n1 + n2
    print("Addition of Cat 4 is : ", res)


sum4()

print("Cat 4 : ", sum4())
