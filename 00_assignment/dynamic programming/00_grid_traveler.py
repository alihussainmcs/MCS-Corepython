def grid_traveler1(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


"""
print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(5, 5))
print(grid_traveler(15, 15))
print(grid_traveler(20, 20))
print(grid_traveler(29, 30))
"""


def grid_traveler(p, q):
    dp = [1 for _ in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]


print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(5, 5))
print(grid_traveler(15, 15))
print(grid_traveler(20, 20))
print(grid_traveler(29, 30))
