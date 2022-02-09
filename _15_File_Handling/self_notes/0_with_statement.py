"""
The with statement can be used while opening a file.

advantage: it will take care of closing file which is opened by it

Hence we need not to close the file explicitly.

In case of exception also, 'with statement' will close the file before the exception
handled.
"""
# with statement to open a file and write data
with open('sample.txt', 'w') as sm:
    sm.write('This is my sample file text data \n')
    sm.write('This is second line ')

# with statement to open a file and read data
with open('sample.txt', 'r') as data:
    for line in data:
        print(line)

# with statement to open a file and write data
with open('sample_1.txt', 'w') as sm:
    sm.writelines('The with statement can be used while opening a file.\nadvantage: \n it will take care of closing '
                  'file '
                  'which is opened by it \n Hence we need not to close the file explicitly. \n In case of exception '
                  'also, "with statement" will close the file before the exception handled.\n')
    sm.write(' This is last line ')

# with statement to open a file and read data
with open('sample_1.txt', 'r') as data:
    for line in data:
        print(line)
