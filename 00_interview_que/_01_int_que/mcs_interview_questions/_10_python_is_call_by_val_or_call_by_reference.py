"""
10. python is call by value or call by reference:

Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.
In the event that you pass arguments like whole numbers, strings or tuples to a function, the
passing is like call-by-value because you can not change the value of the immutable objects being
passed to the function.

Whereas passing mutable objects can be considered as call by reference because when their values are
changed inside the function, then it will also be reflected outside the function.


The two most widely known and easy to understand approaches to parameter passing amongst programming
languages are pass-by-reference and pass-by-value. Unfortunately, Python is “pass-by-object-reference”,
of which it is often said: “Object references are passed by value.”


Pass by reference – It is used in some programming languages, where values to the argument of the
function are passed by reference which means that the address of the variable is passed and then the
operation is done on the value stored at these addresses.

Pass by value – It means that the value is directly passed as the value to the argument of the function.
Here, the operation is done on the value and then the value is stored at the address. Pass by value is
used for a copy of the variable.

#example:


# Python code to demonstrate
# call by value


string = "Geeks"


def test(string):

	string = "GeeksforGeeks"
	print("Inside Function:", string)

# Driver's code
test(string)
print("Outside Function:", string)

#output:

Inside Function: GeeksforGeeks
Outside Function: Geeks


#example:


# Python code to demonstrate
# call by reference


def add_more(list):
	list.append(50)
	print("Inside Function", list)

# Driver's code
mylist = [10,20,30,40]

add_more(mylist)
print("Outside Function:", mylist)

#output:

Inside Function [10, 20, 30, 40, 50]
Outside Function: [10, 20, 30, 40, 50]


#difference between call by value call by reference:

Call by reference	                                                Call by value


1.While calling a function, in a programming language
instead of copying the values of variables, the
address of the variables is used, it is known
as “Call By Reference.”	                                        While calling a function, when we pass
                                                                values by copying variables, it is
                                                                known as “Call By Values.”


2.In this method, a variable itself is passed.	                A copy of the variable is passed in a call
                                                                by value.

3.Change in the variable also affects the value of
the variable outside the function.	                            Changes made in a copy of a variable never
                                                                modify the value of the variable outside
                                                                the function.

4.Allows you to make changes in the values of
variables by using function calls.	                            Does not allow you to make any changes in
                                                                the actual variables.

5.The original value is modified.                                	Original value not modified.
"""