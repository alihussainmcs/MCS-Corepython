class M:
    def f1(self):
        print("1st method of M class")

    def f2(self):
        print("2nd method of M class")


class N(M):
    def fn1(self):
        print("1st method of class N")


n3 = N()

n3.f1()

n3.f2()

n3.fn1()
