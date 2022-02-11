"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods
__iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers from which you can get an
iterator from.

All these objects have a iter() method which is used to get an iterator:

Example
Return an iterator from a tuple, and print each value:

"""
my_tuple = ("apple", "banana", "cherry")
my = iter(my_tuple)

print(next(my))
print(next(my))
print(next(my))

print("----------------------------------------------------------------")
"""
Even strings are iterable objects, and can return an iterator:

Example
Strings are also iterable objects, containing a sequence of characters:
"""
my_str = "banana"
my_it = iter(my_str)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

"""
Looping Through an Iterator
We can also use a for loop to iterate through an iterable object:

Example
Iterate the values of a tuple:
"""
print("------------------------------------------------")
#  The for loop actually creates an iterator object and executes the next() method for each loop.
my_tuple = ("apple", "banana", "cherry")

for x in my_tuple:
    print(x)

"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), 
which allows you to do some initializing when the object is being created. 

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator 
object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

Example
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one 
(returning 1,2,3,4,5 etc.):
"""
print("------------------------------------------------------------------------------------")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        y = self.a
        self.a += 1
        return y


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

"""
StopIteration
The example_1 above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified 
number of times:

Example
Stop after 20 iterations:
"""
print("------------------------------------------------------------------------------")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            z = self.a
            self.a += 1
            return z
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)
