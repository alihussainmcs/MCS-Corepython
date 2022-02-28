# Dynamic Programming  (DP)

# Find Fibonacci series

# 1 Naive recursive algorithm


def fib2(n):
    if n <= 2:
        f = 1
    else:
        f = fib2(n - 1) + fib2(n - 2)

    return f


"""
print(fib2(6))
print(fib2(7))
print(fib2(8))
print(fib2(50))
print(fib2(100))

"""

"""
def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(6))
print(fib2(7))
print(fib2(8))
print(fib2(50))
print(fib2(100))
"""


# 2 Memorized DP algorithm

memo = {}


def fib(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)

    memo[n] = f
    return f


print(fib(1))
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(500))
print(fib(1000))
