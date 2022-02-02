"""
7. what is the difference between append and extend in list?

append adds its argument as a single element to the end of a list. The length
of the list itself will increase by one. extend iterates over its argument adding
each element to the list, extending the list.

append() method will increase the length of the list by exactly one.
This means that if the input to append is a list of elements, then the list itself
will be appended and not the individual elements:

my_lst = [1, 2, 3]
my_lst.append([4, 5])
print(my_lst)

extend() method accepts an iterable whose elements will be appended to the list.
For example, if the input to extend() is a list, it will concatenate the first list
with the other list by iterating over the elements of the input list. This means
that the resulting list’s length will be increased with the size of the iterable
passed to extend() .

my_lst = [1, 2, 3]
my_lst.extend([4, 5, 6])
print(my_lst)

#example:

x = [1, 2, 3]
x.append([4, 5])
print (x)#gives you: [1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5])
print (x)#gives you: [1, 2, 3, 4, 5]

#append() vs extend():

    1.Both extend() and append() are built-in list extension methods.
    2.Append accepts all data types and adds only one element to the list.
    3.Extend accepts only iterable types and appends all elements to the list.
    4. The time complexity is the easiest way to assess each method.
    ex:
    +-----------+-----------------+
    | Method    | Time Complexity |
    +-----------+-----------------+
    | append()  |  O(1)           |
    | extend()  |  O(k)           |
    +-----------+-----------------+
     “k” is the number of elements in the iterable parameter of Extend method.

    5.append() takes single element as an argument whereas extend() doesn't take single element as an
    argument.

    6.append() adds all argument as a single element to the end of a list whereas extend()  iterates over the
    argument and add each element of argument at the end of the list.

    7.append() increases the size of list by 1 whereas extend() increases the size of the list by the number
    of elements in the iterable argument.


"""
