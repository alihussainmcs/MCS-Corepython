class A:
    def m1(self):
        print("In A : m1() ")


class B(A):
    def m2(self):
        print("In B :m2()")


a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()


# b1.m3()


class A:
    def m1(self):
        print("In A : m1() ")


class B(A):

    def m2(self):
        print("In B :m2()")  # 2

    # method overriding
    def m1(self):
        print("In B :m1()")  # 1.2


a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()
# b1.m3()

print("................................................................")


class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())


print("...................................................................")


class Animal:
    # properties
    multicellular = True
    # Eukaryotic means Cells with Nucleus
    eukaryotic = True

    # function breathe
    def breathe(self):
        print("I breathe oxygen.")

    # function feed
    def feed(self):
        print("I eat food.")


# Let's create a child class Herbivorous which will extend the class Animal:


class Herbivorous(Animal):

    # function feed
    def feed(self):
        print("I eat only plants. I am vegetarian.")


herbi = Herbivorous()
herbi.feed()
# calling some other function
herbi.breathe()
