"""

List comprehensions are a tool for transforming one list (any iterable actually) into another list.
 During this transformation, elements can be conditionally included in the new list and each element
  can be transformed as needed.
"""

# Nested List Comprehensions
# Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite
#                       similar to nested for loops. Below is the program which implements nested loop:


matrix = []

for i in range(3):

    # Append an empty sublist inside the list
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(matrix)

print("---------------------------------------------------------------------------------------------------")
# Now by using nested list comprehensions same output can be generated in fewer lines of code.


# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)

print("-------------------------------------------------------------------------------------------")

# Display even elements from a list of random numbers.

# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

print(trans)

print("---------------------------------------------------------------------")


# Display the sum of digits of all the odd elements in a list.

# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)
