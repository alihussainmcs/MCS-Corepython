"""
Say that you are a traveler on a 2D grid. You begin in the top-left
corner and your goal is to travel to the bottom-right corner. You may
only move down or right.

In how may ways can you travel to the goal on a grid with dimensions
m * n?

Write a function `gridTraveler(m, n)` that calculates this.
ex:
gridTraveler(0,1) -> 0  -- No way      -- 1 no box  ie, 0x1
gridTraveler(1,0) -> 0  -- No way      -- 1 no box  ie, 0x1
gridTraveler(8,0) -> 0  -- No way      -- 1 no box  ie, 8x1
gridTraveler(0,0) -> 0  -- No way      -- 1 no box  ie, 0x0

gridTraveler(1,1) -> 1  -- Do Nothing  -- 1 square box ie, 1x1


gridTraveler(2,3) -> 3

Because:
1. right, right, down
2. right, down, right
3. down, right, right
gridTraveler(1,1) -> 1
(the start is the end)
gridTraveler(0,1) -> 0
gridTraveler(1,0) -> 0
(there is there no grids)
The recursive nature can be defined as such,
when traveling down, the function calls would reduce the amount of rows
when traveling right, the function calls would reduce the amount of columns

"""


# O(m*n)
def gridTraveler(m, n):
    table = []
    for i in range(m+1):
        table.append([0 for _ in range(n+1)])
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current

    return table[m][n]


print(gridTraveler(10, 10))
print(gridTraveler(13, 13))
print(gridTraveler(20, 20))
print(gridTraveler(30, 30))
print(gridTraveler(100, 100))
print(gridTraveler(500, 500))
