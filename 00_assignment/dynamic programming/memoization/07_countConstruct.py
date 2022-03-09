"""
PROBLEM: Write a function "countConstruct(target, wordBank)" that accepts a target
string and an array of strings.

Function should return the number of ways that the 'target' can be constructed by
concatenating elements of the 'wordBank' array.

You may reuse elements of 'wordBank' as many times as needed.

"""


def countConstruct(target, wordBank):
    if target == '':
        return 1
    totalCount = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target.replace(word, '', 1)
            numWaysForRest = countConstruct(suffix, wordBank)
            totalCount += numWaysForRest

    return totalCount


print(countConstruct("banana", ["ba", "pa", "ca", "na"]))  # // 1
print(countConstruct("", ["ba", "pa", "ca", "na"]))  # // 1
print(countConstruct("abcdef", ["ab", "abcdefgh", "c", "def"]))  # // 1
print(countConstruct("potato", ["pot", "ta", "to"]))  # // 0
print(countConstruct("skateboard", ["skat", "te", "bor", "ard"]))  # // 0
print(countConstruct("skateboard", ["skat", "te", 'e', "bo", "ard", 'ska']))  # // 2

print('.......................Memoization........................................ ')


def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == '':
        return 1
    totalCount = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target.replace(word, '', 1)
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numWaysForRest

    memo[target] = totalCount
    return totalCount


print(countConstruct("purple", ["purp", "p", "ur", "le", 'purpl']))  # // 2
print(countConstruct("abcdef", ["ab", "abcdefgh", "c", "def"]))  # // 1
print(countConstruct("skateboard", ["skat", "te", "bor", "ard"]))  # // 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", 'ot', 'o', 't']))  # // 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee',
                                                           'eeeeeeee']))  # // 0
print(countConstruct("banana", ["ba", "pa", "ca", "na"]))  # // 1
print(countConstruct("", ["ba", "pa", "ca", "na"]))  # // 1
print(countConstruct("potato", ["pot", "ta", "to"]))  # // 0
print(countConstruct("skateboard", ["skat", "te", 'e', "bo", "ard", 'ska']))  # // 2

"""
m = target sum
n = numbers

Brute force
time : O(n^m*m)
space : O(m^2)

memoization 
time : 0(n*m^2)
space : O(m^2)

"""
