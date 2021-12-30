maxPassengers = 0
vistedDestination = False
directionsArrayToStation = [[0, 1], [1, 0]]
directionsArrayToOrigin = [[0, -1], [-1, 0]]


def GetPassengers(matrix):
    if matrix is None or len(matrix) == 0:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    max = DFS(0, 0, rows, columns, matrix)
    return max


def DFS(row, col, rows, columns, matrix):
    if row == rows - 1 and col == columns - 1:
        vistedDestination = True
    if not vistedDestination:

        for i in range(0, 2):

            r = row + directionsArrayToStation[i, 0]

            c = col + directionsArrayToStation[i, 1]
            if r < 0 or c < 0 or r > rows - 1 or c > columns - 1 or matrix[r][c] == -1:
                continue
            if r == 0 and c == 0:
                break
            flag = 1 if matrix[r][c] == 1 else 0
            matrix[r][c] = 2
            maxPassengers = flag + DFS(r, c, rows, columns, matrix)


    elif vistedDestination:

        for i in range(0, 2):
            r = row + directionsArrayToOrigin[i, 0]

            c = col + directionsArrayToOrigin[i, 1]
            if r < 0 or c < 0 or r > rows - 1 or c > columns - 1 or matrix[r][c] == -1:
                continue
            if r == 0 and c == 0:
                break

            flag = 1 if matrix[r][c] == 1 else 0
            if matrix[r][c] == 1:
                matrix[r][c] = 2
            maxPassengers = flag + DFS(r, c, rows, columns, matrix)

    return maxPassengers

    # var res = GetPassengers(new int[][] {new int[] {0,1,-1},
    # new int[] { 1,0,-1 }, new int[] {1,1,1 } });
    # var res = GetPassengers(new int[][] {new int[] {0,0,0,1},
    # new int[] { 1,0,0,0 }, new int[] {0,0,0,0 }, new int[] {0,0,0,0 } });


res = GetPassengers([[0, 1], [-1, 0]])
