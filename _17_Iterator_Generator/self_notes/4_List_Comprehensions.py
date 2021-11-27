"""
Generator Function -> yield
Generator expression -> comprehension
                        List/Set/Dict comprehension
"""

#  https://www.programiz.com/python-programming/list-comprehension
'''
List Comprehension :
-------------------
 => List comprehension provide a concise way to create lists

'''
# Example: Create List of Even Numbers without List Comprehension
even_nums = []
for x in range(21):
    if x % 2 == 0:
        even_nums.append(x)
print(even_nums)

print("-----------------------------------------------------------------------------------------------")

# Example: Create List of Even Numbers with List Comprehension
even_nums = [x for x in range(21) if x % 2 == 0]
print(even_nums)

print("-----------------------------------------------------------------------------------------------")

# Example: List Comprehension with String List
names = ['Steve', 'Bill', 'Ram', 'Moan', 'Abdul']
names2 = [s for s in names if 'a' in s]
print(names2)

print("-----------------------------------------------------------------------------------------------")

# The following example uses a list comprehension to build a list of squares of the numbers between 1 and 10.

# Example: List Comprehension
squares = [x * x for x in range(11)]
print(squares)

print("-----------------------------------------------------------------------------------------------")
# It is possible to use nested loops in a list comprehension expression. In the following example, all combinations of
#              items from two lists in the form of a tuple are added in a third list object.

# Example: List Comprehension
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums = [(x, y) for x in nums1 for y in nums2]
print(nums)

print("-------------------------------------------------------------------------------------------------")

# The following example demonstrates the if..else loop with a list comprehension.

# Example: List Comprehension

odd_even_list = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
print(odd_even_list)

odd_even_list = [str(i) + '=Even' if i % 2 == 0 else str(i) + "=Odd" for i in range(5)]
print(odd_even_list)

print("-------------------------------------------------------------------------------------------------")
# One of the applications of list comprehension is to flatten a list comprising of multiple lists into a single list.

# Example: List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatList = [num for row in matrix for num in row]
print(flatList)

print("-------------------------------------------------------------------------------------------------")

# We can use nested if conditions with a list comprehension.

# Example: List Comprehension Copy
nums = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
print(nums)
