print(101)

# OR

x = 101
print(x)
print(x+20)


print(101+201)
# OR
x = 101 + 201
print(x)

print("--------Return types------------")

'''
Here sum function is taking 2 responsibilities
1. Implementing the business logic
2. Handling the end result/output
'''
# Without return types

print("Without return types")


def sum_1(n1, n2):
    result = n1 + n2
    print("Addition : ", result)


sum_1(100, 200)       # returns None
print("Sum is  :", sum_1(100, 200))  # returns None

# with return type
print("With return type ")


def sum_1(n1, n2):
    result = n1 + n2
    return result  # int float bool string list tuple dict set


sum_1(11, 22)  # int float bool string list tuple dict set
print("Summation is :", sum_1(11, 22))
print("Summation is :", sum_1(11.5, 22.9))
print("Summation is :", sum_1(True, 22.9))
print("Summation is :", sum_1(True, False))
print("Summation is :", sum_1(True, True))
print("Summation is :", sum_1(True, 10+11j))
print("Summation is :", sum_1(True, 10+11j))
print("Summation is :", sum_1("Ali ", 'Hussain'))
print("Summation is :", sum_1([1, 2], [3, 4]))
print("Summation is :", sum_1((1, 2, 3, 7, 8, 9), (11, 22, 33, 77, 88, 99)))
# print("Summation is :", sum_1({1, 2}, {3, 4})) TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print("Summation is :", sum_1({1: 101, 2: 102}, {3: 103, 4: 104}))
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# 1000
# x = 10000

output = sum_1(25, 10)              # x = 10 print(x)
print("Addition 42: ", output)

print("Addition 44: ", sum_1(25, 10))  # print(10)

print("----Return type examples----")

list1 = [1, 2, 3, 4, 5]
print("Before append : ", list1)
list1.append(50)  # It will append 50 to list1 and returns None
print("Append 51 :", list1.append(51))  # print(10)

app = list1.append(200)   # x = 10 print(x)
print("Append 200 :", app)

print("After append  : ", list1)

print("-----Pop operations-------")
list1 = [1, 2, 43, 65, 23, 46, 78, 29, 83, 23, 3, 4]
print(list1.pop())  # It will remove last element and returns the element to us
print("Removed values is :", list1.pop())
print("LIST : ", list1)

val = list1.pop(5)
print("Values is :", val)
print(val)
print()
print("Removed value is : ", val)

print(list1.remove(65))

print("Index is : ", list1.index(29))
