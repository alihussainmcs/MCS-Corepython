# Clear()------ method removes the first matching element (which is passed as an argument) from the list.

print("*****Clear*****")
print("clear()--->Removes the item with the specified value")


numbers = [2, 3, 5, 7, 9, 11]

numbers.remove(9)    # Removing 9 from the list

print("Updated List:", numbers)


num = [2, 3, 5, 7]

num.remove(10)

print(num)  # Deleting the element does not exist it will throw the error


