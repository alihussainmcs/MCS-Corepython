# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Input  : 8
# Output : 40320

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n_1 = 8
print(factorial(n_1))
