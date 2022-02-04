# Reverse()------ Reverses the order of the list.

print("*****Reserve*****")
print("reverse()--->Reverses the order of the list")

numbers = [2, 3, 5, 7, 9, 11]

print("Original List:", numbers)

numbers.reverse()

print("Reversed List:", numbers)


a = ["notebook", "board", "chalk", "bench"]

print("Original List:", a)

a.reverse()

print("Reversed List:", a)

# Reverse a List Using Slicing Operator

li1 = a[::-1]

print("Reversed using slicing operator:", li1)

fruits = ['Mango', 'Banana', 'Grapes', 'Kiwi', 'Pineapple', 'apple']

print('Original List :', fruits)

fruits.reverse()

print('Reversed list :', fruits)

print(id(fruits))  # 2120649072832

print(id(fruits.reverse()))  # 140704320695512

lst = [1, True, '1', 1.0]

print('Original List :', lst)

lst.reverse()

print('Reversed list :', lst)


my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

print('Original list :', my_list)

my_list.reverse()

print('Reversed list :', my_list)