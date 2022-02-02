"""
21. what is decorator?

A decorator in Python is a function that takes another function as its argument, and returns
yet another function . Decorators can be extremely useful as they allow the extension of an
existing function, without any modification to the original function source code.

These are used to modify the behavior of the function. Decorators provide the flexibility to wrap
another function to expand the working of wrapped function, without permanently modifying it.

It is also called meta programming where a part of the program attempts to change another part
of program at compile time.

#Syntax for Decorator: 

@gfg_decorator
def hello_decorator():
    print("Gfg")

#Above code is equivalent to -

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)


#example:
# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called

	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")

	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

"""