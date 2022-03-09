"""
PROBLEM: Write a function "canConstruct(target, wordBank)" that accepts a target
string and an array of strings.

Function should returned a boolean indicating whether or not the 'target' can be constructed by
concatenating elements of the 'wordBank' array.

You may reuse elements of 'wordBank' as many times as needed.

"""


def canConstruct(target, wordBank):

    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target.replace(word, '', 1)

            if canConstruct(suffix, wordBank):
                return True

    return False


print(canConstruct("banana", ["ba", "pa", "ca", "na"]))                 # // True
print(canConstruct("", ["ba", "pa", "ca", "na"]))                       # // True
print(canConstruct("abcdef", ["ab", "abcdefgh", "c", "def"]))           # // True
print(canConstruct("potato", ["pot", "ta", "to"]))                      # // False
print(canConstruct("skateboard", ["skat", "te", "bor", "ard"]))         # // False
print(canConstruct("skateboard", ["skat", "te", 'e', "bo", "ard"]))     # // True

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
print('..................Memoization .........................................')


def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target.replace(word, '', 1)

            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(canConstruct("banana", ["ba", "pa", "ca", "na"]))                 # // True
print(canConstruct("", ["ba", "pa", "ca", "na"]))                       # // True
print(canConstruct("abcdef", ["ab", "abcdefgh", "c", "def"]))           # // True
print(canConstruct("potato", ["pot", "ta", "to"]))                      # // False
print(canConstruct("skateboard", ["skat", "te", "bor", "ard"]))         # // False
print(canConstruct("skateboard", ["skat", "te", 'e', "bo", "ard"]))     # // True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee',
                                                         'eeeeeeee']))    # // false
