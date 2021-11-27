# Insert()------ method inserts an element to the list at the specified index.

print("*****Insert*****")
print("insert()--->Adds the element at the specified position")

numbers = [2, 3, 5, 7, 9, 11]

# 4 represents index
# 67 is the number to be added in the list
numbers.insert(4, 67)

print(numbers)


'''
insert() takes two parameters
1--> index
2--> element
'''

# Inserting a Tuple (as an Element) to the List

numbers = [2, 3, 5, 7, 9, 11]
num1 = (2, 3) # tuple

# here inserting or adding tuple to the existing list
numbers.insert(6, num1)
print(numbers)