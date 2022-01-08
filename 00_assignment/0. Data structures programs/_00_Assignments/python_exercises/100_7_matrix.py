# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Input  : 3,5
# Output : [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

X, Y = 3, 5  # map(int, input().split(','))
matrix = [i * j for i in range(X) for j in range(Y)]
print([matrix[:5], matrix[5:10], matrix[10:16]])
