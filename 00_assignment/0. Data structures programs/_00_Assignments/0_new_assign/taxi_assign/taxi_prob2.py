matrix = [[0, 1],
          [1, 1],
          [1, 1]]

rows = len(matrix)
col = len(matrix[0])

passengers = 0

rpos = 0
cpos = 0

for i in range(len(str(matrix))):
    if cpos < col - 1:
        if matrix[rpos][cpos + 1] == 1:
            cpos += 1
            passengers += 1
        elif matrix[rpos][cpos + 1] == 0:
            cpos += 1
    if rpos < rows - 1:
        if matrix[rpos + 1][cpos] == 1:
            rpos += 1
            passengers += 1
        elif matrix[rpos + 1][cpos] == 0:
            rpos += 1

if rpos != rows - 1 or cpos != col - 1:
    passengers = 0
print(passengers)
