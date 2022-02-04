# Clear()------ method removes the first matching element (which is passed as an argument) from the list.

print("*****Clear*****")
print("clear()--->Removes the item with the specified value")


numbers = [2, 3, 5, 7, 9, 11]

numbers.remove(9)    # Removing 9 from the list

print("Updated List:", numbers)


num = [2, 3, 5, 7]

# num.remove(10) ValueError: list.remove(x): x not in list
num.remove(7)

print('List after remove 7 :', num)

fruits = ['Mango', 'Banana', 'Grapes', 'Kiwi', 'Pineapple', 'apple']

print('List :', fruits)

fruits.remove('Mango')

print('List after remove Mango :', fruits)

fruits.remove('Banana')

print('List after remove Banana :', fruits)

# fruits.remove('') ValueError: list.remove(x): x not in list

fruits.remove('Kiwi')

print('List after remove Kiwi :', fruits)

fruits.remove('apple')

print('List after remove apple :', fruits)

fruits.remove('Grapes')

print('List after remove Grapes :', fruits)

fruits.remove('Pineapple')

print('List after remove Pineapple :', fruits)
