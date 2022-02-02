"""
6. what is the difference between list and set?

A set is a collection which is unordered and un-indexed, and doesnt allow duplicates.
In Python, sets are written with curly brackets. A list is a collection which is ordered
and changeable. In Python lists are written with square brackets.


List: Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and
ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in
Python.
The main characteristics of lists are –

1.The list is a datatype available in Python which can be written as a list of comma-separated
values (items) between square brackets.

2.List are mutable .i.e it can be converted into another data type and can store any data element in it.
3.List can store any type of element.


Set: In Python, Set is an unordered collection of data type that is iterable, mutable, and has
no duplicate elements. The major advantage of using a set, as opposed to a list, is that it has
a highly optimized method for checking whether a specific element is contained in the set.

The main characteristics of set are –

1.Sets are an unordered collection of elements or unintended collection of items In python.
2.Here the order in which the elements are added into the set is not fixed, it can change frequently.
3.It is defined under curly braces{}
4.Sets are mutable, however, only immutable objects can be stored in it.




List	                                                            Set

Lists is Mutable	                                            Set is Mutable

It is Ordered collection of items	                            It is Unordered collection of items

Items in list can be replaced or changed	                    Items in set cannot be changed or replaced

#example:
                                                                #example:
L1 = ["John", 102, "USA"]
L2 = [1, 2, 3, 4, 5, 6]
print(type(L1))
print(type(L2))                                                 Days = {"Monday", "Tuesday", "Wednesday", "Thursday",
                                                                "Friday", "Saturday", "Sunday"}
                                                                print(Days)
                                                                print(type(Days))
                                                                print("looping through the set elements ... ")
                                                                for i in Days:
                                                                print(i)

"""
