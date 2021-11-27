'''
Accessing List Items:
---------------------
List items are indexed you can access them by referring to the index number.'''

a = ["apple", "banana", "cherry"]

print(a[1]) # banana

print(a[-1]) # Cherry

'''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.'''

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("******Slicing*******")

print("Normal List is:", b)

print("Slicing between the desired position:", b[2:5])

print("Slicing from the start:", b[:3])

print("Slicing from the end:", b[3:])

print("Slicing operation: ", b[::1])

print("Slicing operation: ", b[::2])

print("Slicing operation:", b[::])

print("Slicing operation:", b[1:-3])

print("Slicing operation:", b[-3:-1])


print("*****Adding Two List*****")

sum1 = [1, 2, 3]
sum2 = [4, 5, 6]

print("Adding two lists", sum1 + sum2)

print("*****Max*****")

print("Maximum number in the list is:", max(b))


print("*****Min*****")

print("Minimum number in the list is:", min(b))

print("*****Length*****")

print("Length of the list is:", len(b))


