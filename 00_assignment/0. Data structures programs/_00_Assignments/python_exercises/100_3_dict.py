# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Input  : 8
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = 8
dict_square = {i: i * i for i in range(1, n + 1)}
print(dict_square)
