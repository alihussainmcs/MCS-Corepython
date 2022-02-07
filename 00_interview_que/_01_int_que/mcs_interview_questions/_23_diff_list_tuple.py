"""
23. write a difference between list and tuple?

The key difference between the tuples and lists is that while the tuples are immutable objects
the lists are mutable. This means that tuples cannot be changed while the lists can be modified.
Tuples are more memory efficient than the lists.



List:

List is a container to contain different types of objects and is used to iterate objects.

#Example

list = ['a', 'b', 'c', 'd', 'e']


list1 = ['JavaTpoint', 1, 2, 54.30, {'Name: ''Peter'}]
print(type(list))
tuple1 = ('JavaTpoint',5,8,31.9,[1,2,3])
print(type(tuple1))

Tuples:

Tuple is also similar to list but contains immutable objects. Tuple processing is faster than List.

#Example

tuples = ('a', 'b', 'c', 'd', 'e')


a = (10,20,"JavaTpoint",30,40)
print(a)

Sr. No.	            Key                     	List	                                    Tuple

1	                Type	                List is mutable.	                Tuple is immutable.

2	                Iteration	            List iteration is slower and
                                            is time consuming.	                Tuple iteration is faster.

3	                Appropriate             for	List is useful for insertion
                                            and deletion operations.	        Tuple is useful for readonly
                                                                                operations like accessing
                                                                                elements.

4	            Memory Consumption	        List consumes more memory.	        Tuples consumes less memory.

5	                Methods	            List provides many in-built methods.	Tuples have less in-built methods.

6	            Error prone	             List operations are more error prone.	Tuples operations are safe.



"""