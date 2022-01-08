# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number.
# Input  : 34,67,55,33,12,98
# Output :
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

numbers = 34, 67, 55, 33, 12, 98
numbers_tuple = tuple(numbers)
print(numbers, '\n', numbers_tuple)
