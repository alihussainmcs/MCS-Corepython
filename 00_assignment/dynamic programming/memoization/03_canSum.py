"""
Write a function 'canSum(targetSum, numbers)' that takes in a targetSum and an
array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible
to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are no negative
7, [5,3,4,7]
"""


def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum in numbers or targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        reminder = targetSum - i
        if canSum(reminder, numbers):
            return True
    return False


print(canSum(7, [2, 3]))

print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(100, [20, 31]))
# print(canSum(300, [7, 14]))

# Memoization
print('             ..........        Memoization   .................')


def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum in numbers or targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(100, [20, 31]))
print(canSum(300, [7, 14]))
print(canSum(500, [13, 13]))
print(canSum(5000, [10, 10]))
