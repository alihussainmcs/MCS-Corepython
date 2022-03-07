"""

Dynamic Programming

Part - 1. Memoization
Part - 2. Tabulation


Problem :

Write a function that takes a number as argument and return n-th number of Fibonacci sequence.

-->

The 1st and 2nd number of the sequence will be 1.
To generate next number of sequence, we sum two previous numbers

n       : 1, 2, 3, 4, 5, 6, 7 , 8 , 9  ,...
fib(n)  : 1, 1, 2, 3, 5, 8, 13, 21, 34 ,...

"""
print('...................    fibonacci series ....................')
print()


def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(6))
print(fib(7))
print(fib(8))
# print(fib(37))
print()

# Memoization on fib.
print('.............................Memoization on fibonacci series ....................')
print()
f = {}


def fib1(n):
    if n in f:
        return f[n]

    if n <= 2:
        return 1

    f[n] = fib1(n - 1) + fib1(n - 2)
    return f[n]


print(fib1(6))
print(fib1(7))
print(fib1(8))
print(fib1(50))
print(fib1(500))
print(fib1(1000))


# Write a function `fib(n)` that takes in a number as an argument.
# The function should return the n-th number in the Fibonacci sequence
# Ex: Fibonacci: 1,1,2,3,5,8,13,21, etc
#             n: 1,2,3,4,5,6,7 ,8
def fib_without_memoization(n):
    """
    Doesn't make use of memoization to return the nth number of
    Fibonacci
    This function has a time complexity of O(2^n)
    and a space complexity of O(n)
    """
    if n <= 2:
        return 1

    return fib_without_memoization(n - 1) + fib_without_memoization(n - 2)


def fib(n, memo={}):
    """
    Makes use of memoization to store previously calculated values
    and return those instead of spawning of more recursive calls
    onto the stack.
    We'll be using a dictionary to store previously computed results.
    This functions time complexity is O(n)
    and it's space complexity is O(n) as well
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


if __name__ == "__main__":
    # if we were to change testData to something like 50
    # the execution time would increase quite a lot.
    testData = 6
    expected = 8

    # Testing the logic without memoization
    got = fib_without_memoization(testData)
    print(got)

    assert got == expected, "Values did not match"

    # Testing the logic with memoization
    t = 50
    e = 12586269025

    # We now see that the value computes practically instantly
    got = fib(t)

    print(got)

    assert got == e, "Values did not match"
