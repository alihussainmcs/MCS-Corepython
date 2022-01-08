# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Input  : 100,150,180
# Output : 18,22,24

from math import sqrt

C, H = 50, 30
result = []
D_numbers = 100, 150, 180

for D in D_numbers:
    result.append(str(int(sqrt((2 * C * int(D) / H)))))
print(",".join(result))
