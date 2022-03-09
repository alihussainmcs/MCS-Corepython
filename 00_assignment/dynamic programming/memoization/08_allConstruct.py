"""
Problem:
Write a function all_construct(target, word_bank) that accepts a target string and a list of strings.

The function should return a 2D list containing all the ways that the target can be constructed
by concatenating elements of the word_bank list. Each element of the 2D list should represent
one combination that constructs the target.

You may reuse elements of the word_bank as many times as needed.


Python implementation --->

The catch here is in implementing target_ways. We need to copy all sub-lists in a list.
However, using list.copy() on nested lists will only copy the outer list while all sub-lists will keep pointing to the
sub-lists in the original list. There are several ways to implement copy for nested lists in Python, I choose to use
list comprehension with full slicing new_list = [sublist[:] for sublist in nested_list]

"""

# O(n**m)


def all_construct(target, word_bank):
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            result.extend(target_ways)
    return result


print(all_construct('hello', ['cat', 'dog', 'mouse']))  # []
print(all_construct('', ['cat', 'dog', 'mouse']))  # [[]]
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # [['le', 'purp'], ['le', 'p', 'ur', 'p']]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
# [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]

print('..................Memoization .....................................')


def all_construct(target, word_bank, memo):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            # ret_target = [el[:] for el in target_ways]
            result.extend(target_ways)
    memo[target] = result
    return result


print(all_construct('hello', ['cat', 'dog', 'mouse'], memo={}))  # []
print(all_construct('', ['cat', 'dog', 'mouse'], memo={}))  # [[]]
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}))  # [['le', 'purp'], ['le', 'p', 'ur', 'p']]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], memo={}))
# [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]
print(all_construct("eeeeeeeeeeeeeeef", [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
    'eeeeeee',
    'eeeeeeee'
], memo={}))