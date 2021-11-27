# define an iterable such as a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# get an iterator using iter()
iter1 = iter(list1)
# infinite loop
while True:
    try:
        # get the next item
        print(next(iter1))
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

print("--------------------------------------------------------------------------------------------------")


# Here is our own custom Iterator that returns an even number or 1 every time we iterate upon it:

class Evenit:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            if self.n % 2 == 0:
                result = self.n
                self.n += 1
                return result
            else:
                self.n += 1
                return 1
        else:
            raise StopIteration


# create an object
numbers = Evenit(10)

for i in numbers:
    print(i)

"""As we can see, this iterator returns even numbers up to 10 (because we have given the argument to the event as 
10), and whenever it encounters an odd number, it just returns 1. In a similar manner, you can create your own 
iterator. 
"""
print("------")
# Use iterables in for-loops for multiple times
number_iterable = [1, 2, 3]
for i in number_iterable:
    print(i)
print('-----')
for i in number_iterable:
    print(i)
print('-----')
# Use iterators in for-loops for multiple times
number_iterator = iter([1, 2, 3])
for i in number_iterator:
    print(i)
print('-----')
for i in number_iterator:
    print(i)
# nothing is printed

print("-------------------------------------------------------------------------------------")


# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)
