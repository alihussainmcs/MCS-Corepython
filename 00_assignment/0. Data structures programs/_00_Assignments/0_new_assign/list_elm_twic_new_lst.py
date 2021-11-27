Input = [1, 2, 3, 4]

# Using list comprehension
Output = [elem for x in Input for elem in (x,) * (x % 4 + 1)]

# printing
print("Initial list is:'", Input)
print("New list is:", Output)


Input = [1, 2, 3, 4]

# Using list comprehension
Output = [elem for x in Input for elem in (x,) * (x % 5)]

# printing
print("Initial list is:'", Input)
print("New list is:", Output)


Input = [1, 2, 3, 4]

# Using list comprehension
Output = [elem for x in Input for elem in (x,) * (x % 2 + 2)]

# printing
print("Initial list is:'", Input)
print("New list is:", Output)


Input = [1, 2, 3, 4]

# Using list comprehension
Output = [elem for x in Input for elem in (x,) * (x % 1 + 3)]

# printing
print("Initial list is:'", Input)
print("New list is:", Output)
