"""
9. difference between iterator and generator:

9.1:Iterator

    1.Class is used to implement an iterator

    2.Local Variables are not used here.

    3.Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.

    4.Iterator uses iter() and next() functions

    5.Every iterator is not a generator

    6. example:

    iter_list = iter(['Geeks', 'For', 'Geeks'])
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))



9.2:Generator

    1.Function is used to implement a generator.

    2.All the local variables before the yield function are stored.

    3.Generators are mostly used in loops to generate an iterator by returning all the values in the
    loop without affecting the iteration of the loop.

    4.Generator uses yield keyword

    5.Every generator is an iterator

    6. example:

    def sq_numbers(n):
        for i in range(1, n+1):
            yield i*i

    a = sq_numbers(3)

    print("The square of numbers 1,2,3 are : ")
    print(next(a))
    print(next(a))
    print(next(a))

9.21.Advantages of Python Generators:

1. Easy to Implement Anywhere

The python generators are easy to implement in the dynamic as well as user-defined codes.
They generally fetch values from libraries, which make them accessible on every python version.

2. Highly Memory Efficient

A normal function to return a sequence will create the entire sequence in memory before returning
the result within the runtime itself.

3. Represent Infinite Stream

Generators can represent the length of a series of infinite numbers taken at a time. And this is
supported by the library function.

4. Pipelining Generators in Python

Multiple generators can be used to pipeline a series of operations within the runtime itself.


S.no 	Parameters              	Generator	                            Iterator


1	   Implementation      	Implemented using a function defined
                                in the runtime.	                        Implemented using a class in
                                                                        the code.

2	Yield usage for coder	Generator uses the ‘yield’ keyword	        Iterator does not use any keyword

3	Class variable	        Generator does not need a class in python.	Iterator implements its own class

4	Globals and locals  	Generator saves the states of the local
                            variables	                                Iterator also does not uses local
                                                                        variable

5	Yield usage for user	Uses the yield keyword for the output.	    Does not use the yield keyword
                                                                        anywhere in the code.

6	Efficiency          	Generators  write fast and compact
                            code	                                    Iterator writes custom and long codes

7	Functions	            Generator use python functions	            Iterator,use the iter() and next()
                                                                        functions

8	Storage capacity	    Generator is not memory efficient	        Iterator is memory-efficient

9	Relative working	    Usage results in a concise code
                            in any  relative function.	                Usage results in a relatively
                                                                        less concise code as compared
                                                                        in the whole python code.

"""