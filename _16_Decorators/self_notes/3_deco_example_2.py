def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("+" * 30)
        func(*args, **kwargs)
        print("=" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

print("--------------------------------------------------------------------")


def printer(msg):
    print(msg)


printer = star(percent(printer))
printer('MCS')
print("--------------------------------------------------------------------")


@percent
@star
def printer(msg):
    print(msg)


printer('Python')

print('---------------------------------------------------------------------------')


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
    print(a/b)


divide(2, 5)
'''

o/p:

I am going to divide 2 and 5
0.4
'''

divide(2, 0)

'''
o/p:

I am going to divide 2 and 0
Whoops! cannot divide

'''
