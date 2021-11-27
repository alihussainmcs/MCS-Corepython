# Iterator

list_1 = [1, 2, 3]
data = iter(list_1)

print(next(data))

print(next(data))

print(next(data))

print("--------------------------------------------------------------------------------------")
# Generator


def iter_func():
    yield 'Python'


for i in iter_func():
    print(i)
