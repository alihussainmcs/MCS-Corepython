# Write a program that accepts a sentence and calculate the number of letters and digits.
# Input  : hello world! 123
# Output : LETTERS 10, DIGITS 3

string = input()
count_alpha = count_digit = 0
for i in string:
    if i.isalpha():
        count_alpha += 1
    elif i.isnumeric():
        count_digit += 1
print('LETTERS ' + str(count_alpha) + ', ' + 'DIGITS ' + str(count_digit))
