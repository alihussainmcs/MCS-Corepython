# Grid Traveler Memoization
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


def gridTraveler_without_memoization(m, n):
    """
    See above for what this is solving.
    The run time of this function is O(2^m+n)
    The space complexity is O(m+n)
    """
    # Base cases
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    # down - reduce rows, right - reduce columns
    return gridTraveler_without_memoization(m - 1, n) + gridTraveler_without_memoization(m, n - 1)


print(gridTraveler_without_memoization(0, 1))  # 0
print(gridTraveler_without_memoization(1, 0))  # 0
print(gridTraveler_without_memoization(1, 1))  # 1
print(gridTraveler_without_memoization(1, 2))  # 1
print(gridTraveler_without_memoization(2, 1))  # 1
print(gridTraveler_without_memoization(2, 2))  # 2
print(gridTraveler_without_memoization(2, 3))  # 3
print(gridTraveler_without_memoization(3, 2))  # 3
print(gridTraveler_without_memoization(3, 3))  # 6
# print(gridTraveler_without_memoization(13, 13))  # 2704156

memo = {}


def gridTraveler(m, n):
    """
    See above for what this is solving.
    This version makes sense of memoization
    The run time of this function is O(m*n)
    The space complexity is O(m+n)
    """
    # Are the arguments in the memo
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]

    # Base cases
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    # down - reduce rows, right - reduce columns
    memo[key] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return memo[key]


print()
print(gridTraveler(10, 10))
print(gridTraveler(13, 13))
print(gridTraveler(20, 20))
# print(gridTraveler(30, 30))
# print(gridTraveler(100, 100))
# print(gridTraveler(500, 500))
print(memo)
