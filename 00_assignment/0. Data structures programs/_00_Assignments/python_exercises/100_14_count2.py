# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Input  : Hello world!
# Output : UPPER CASE 1, LOWER CASE 9

string = input()
count_lower = count_upper = 0
for i in string:
    if i.islower():
        count_lower += 1
    elif i.isupper():
        count_upper += 1
print('UPPER CASE ' + str(count_upper) + ', ' + 'LOWER CASE ' + str(count_lower))
