# Generators with Iterators
def generator_thr_iter():
    yield 'xyz'
    yield 246
    yield 40.50


for i in generator_thr_iter():
    print(i)

print("-------------------------------------------------------------------------------------------------")


# Generator using next
def generator_thr_iter():
    yield 'xyz'
    yield 246
    yield 40.50


g = generator_thr_iter()
print(g.__next__())

print(g.__next__())

print(g.__next__())

# print(g.__next__())  StopIteration


"""
Program to print square of numbers from 1 to n
Consider we want to calculate the square of number from 1 to n, where n is really big number, such that creating a list 
of numbers up to ‘n’ would occupy the entire system memory space.

With generator, our approach will be something like -

"""
print("---------------------------------------------------------------------------------------------------")


def num_generator(n):
    num = 1
    while True:
        yield num
        if num == n:
            return
        else:
            num += 1


for i in num_generator(100):
    print(i*i)

print("------------------------------------------------------------------------------------------------------")


def my_generator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30


gen = my_generator()
print(next(gen))

print(next(gen))

print(next(gen))


print("---------------------------------------------------------------------------------------------")


def rev_str(my_str):
    length = len(my_str)
    for la in range(length - 1, -1, -1):
        yield my_str[la]


# For loop to reverse the string
for char in rev_str("MCS-Python"):
    print(char)
