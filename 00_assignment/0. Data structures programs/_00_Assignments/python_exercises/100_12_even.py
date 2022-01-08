# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = []
for i in range(1000, 3001):
    count = 0
    for k in str(i):
        if int(k) % 2 == 0:
            count += 1
    if count is 4:
        numbers.append(str(i))
print(','.join(numbers))
