def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(4, 2)
print()
divide(5, 0)

print('---------------------------------------------------------')


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_hello():
    print("Hello There")


say_hello()

print('----------------------------------------------------------------------------------')


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))


cities("Bangalore", "Hyderabad")
