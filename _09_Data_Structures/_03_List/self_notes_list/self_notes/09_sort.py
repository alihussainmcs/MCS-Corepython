"""
 9. sort
      list.sort(obj)   Sorts the elements
"""


list1 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]

print("Given list1 is : ", list1)

list1.sort()  # ascending order

print("List sort ascending : ", list1)

list1.sort(reverse=True)  # descending order
print("List sort descending: ", list1)

list2 = [11, 27, 39, 40, 25, 67, 10, 10.4]

print("Given list2 is : ", list2)

list2.sort()  # ascending order

print("List2 sort ascending : ", list2)

list1.sort(reverse=True)  # descending order
print("List2 sort descending: ", list2)

# list2 = [11, 27, 39, 40, 25, 67, 10, 10.4, True, 'Hello', [1, 2, 3], (10, 20, 30), {1: 1}, {200, 100, 300}]
# list2.sort()  # ascending order
# TypeError: '<' not supported between instances of 'str' and 'int'
