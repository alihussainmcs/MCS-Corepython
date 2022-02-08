class M:
    def f1(self):
        print("1st method of M class")

    def f2(self):
        print("2nd method of M class")


class N(M):
    def fn1(self):
        print("1st method of class N")  # Own method --> Method Over riding


n1 = N()
n1.fn1()
n1.f2()
n1.f1()

print("..........................................................")


class M:
    def f1(self):
        print("1st method of M class")

    def f2(self):
        print("2nd method of M class")


class N(M):
    def f1(self):                       # Own implementation
        print("1st method of class N")

    def f2(self):                       # Own implementation
        print("2nd method of class N")


n2 = N()
n2.f1()
n2.f2()
