"""
Two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row
and j-th column of the array should be i*j
"""
row_num = 3  # int(input("Input number of rows: "))
col_num = 4  # int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row * col

print(multi_list)
