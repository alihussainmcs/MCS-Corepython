"""
Problem :

Write a function that takes a number as argument and return n-th number of Fibonacci sequence.

-->

The 1st and 2nd number of the sequence will be 1.
To generate next number of sequence, we sum two previous numbers

n       : 1, 2, 3, 4, 5, 6, 7 , 8 , 9  ,...
fib(n)  : 1, 1, 2, 3, 5, 8, 13, 21, 34 ,...

"""


# O(n)
def fib(n):
    table = []
    for i in range(n+1):
        table.append(0)
    table[1] = 1
    for count in range(n):
        table[count+1] += table[count]
        if count < len(table)-2:
            table[count+2] += table[count]
    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
print(fib(100))
print(fib(1000))
