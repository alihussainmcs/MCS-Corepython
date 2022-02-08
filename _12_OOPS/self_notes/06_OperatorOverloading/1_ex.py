"""

https://www.geeksforgeeks.org/operator-overloading-in-python/

"""
# Everything is an object in Python

# Operator overloading
# 10+20  10+20+30

x = 10
y = 20
print("Addition : ", x + y)  # x.__add__(y)

list1 = list()
x = 10.5
y = 20.2
print("Addition : ", x + y)  # x.__add__(y)

str1 = 'Hello'
str2 = 'World'
print("Addition  :", str1 + str2)  # str1.__add__(str2)

print("...................................................")


class Bubble:
    def __init__(self, volume):
        self.volume = volume

    def __str__(self):
        return "volume is " + str(self.volume)

    def __add__(self, other):
        volume = self.volume + other.volume
        return Bubble(volume)


b1 = Bubble(20)
b2 = Bubble(30)
b3 = b1 + b2
print(b3)

print(".......................................................")


class Complex:
    # defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # overloading the add operator using special function
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return r, i

    # string function to print object of Complex class
    def __str__(self):
        return str(self.real) + ' + ' + str(self.img) + 'i'


c1 = Complex(5, 3)
c2 = Complex(2, 9)
print("sum = ", c1 + c2)
