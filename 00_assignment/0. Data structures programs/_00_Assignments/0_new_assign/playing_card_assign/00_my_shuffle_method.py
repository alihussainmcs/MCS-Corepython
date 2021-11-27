import copy
import random


def shuffle_1(container):
    new_container = copy.copy(container)
    shuffle_in_place(new_container)
    return new_container


def shuffle_in_place(container):
    for index in range(len(container) - 1, 0, -1):
        other = random.randint(0, index)
        if other == index:
            continue
        container[index], container[other] = container[other], container[index]


mylist = ["apple", "banana", "cherry"]

print(shuffle_1(mylist))
