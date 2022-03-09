"""
PROBLEM:
Write a function "howSum(targetSum, numbers)" that takes in a targetSum
and an array of numbers as arguments.

The function should return an array containing any combination of elements that
add up to exactly the targetSum. If there is no combination that add up to targetSum, than
result null.

If there are multiple combinations possible, you may return any single one.


"""


def howSum(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = howSum(remainder, arr)
        if result is not None:
            result.append(num)
            return result
    return None


"""
    m = target sum
    n = length of array

    Brute Force 
    time: O(n^m * m)
    space: O(m)
"""

testCases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (8, [2, 3, 5])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={howSum(targetSum, numbers)}')

print('       .. ...........     Memoization   ........................')


def howSum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = howSum(remainder, arr, memo)
        if result is not None:
            result.append(num)
            memo[target] = result
            return memo[target]
    memo[target] = None
    return None


"""
    m = target sum
    n = length of array

    Brute Force 
    time: O(n^m * m)
    space: O(m)

    Memoize Version
    time: O(n*m*m) or O(n * m^2)
    space: O(m*m) or O(m^2)
"""

testCases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (7, [2, 4]), (300, [7, 14]), (500, [13, 13]), (5000, [10, 10])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={howSum(targetSum, numbers)}')
