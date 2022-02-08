print("------------Using functions static data---------------------")


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


print("Factorial of 4 is :", factorial(4))
print("Factorial of 5 is :", factorial(5))

print("------------Using functions dynamic data---------------------")

a = 6  # int(input("Enter a number : ")


def factorial_1(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    print("Factorial is :", result)


factorial_1(a)

print("------------Using OOPs---------------------")


class Fact:
    def __init__(self):
        pass

    @ staticmethod
    def fact(n):
        if n == 0:
            result = 1
        else:
            result = n * factorial(n - 1)

        print("Factorial is :", result)

        
f = Fact()

f.fact(5)
