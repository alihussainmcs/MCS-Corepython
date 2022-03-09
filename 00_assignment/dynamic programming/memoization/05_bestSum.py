"""
Write a function 'bestSum(targetSum, numbers') that takes in a targetSum
and an array of numbers as arguments.

The function should return an array containing the shortest combinations
of numbers that add up to exactly the targetSum.

If there is tie in the shortest combination, you may return any one of
the shortest.

"""


def bestSum(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    shortedCombination = None
    for num in arr:
        remainder = target - num
        result = bestSum(remainder, arr)
        if result is not None:
            result.append(num)
            if shortedCombination is None or len(result) < len(shortedCombination):
                shortedCombination = result
    return shortedCombination


testCases = [(7, [5, 3, 4, 7]), (8, [2, 3, 5])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={bestSum(targetSum, numbers)}')


"""
m = target sum
n = numbers

Brute force
time : O(m^n*m)
space : O(m^2)

memoization 
time : 0(n*m^2)
space : O(m^2)

"""

print('................................Memoization..........................................')


def bestSum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortedCombination = None
    for num in arr:
        remainder = target - num
        result = bestSum(remainder, arr, memo)
        if result is not None:
            # result.append(num)
            combination = result[:] + [num]
            if shortedCombination is None or len(combination) < len(shortedCombination):
                shortedCombination = combination
    memo[target] = shortedCombination
    return shortedCombination


testCases = [(7, [5, 3, 4, 7]), (8, [2, 3, 5]), (100, [1, 2, 5, 25]), (300, [7, 14]), (5000, [400, 100])]

for test in testCases:
    targetSum, numbers = test
    print(f'canSum({targetSum}, {numbers})={bestSum(targetSum, numbers)}')
