print("------1.Normal Inheritance: - 1.1 - Reuse super class methods  AS IS-------")


class M:
    def f1(self):
        print("1st method of M class")

    def f2(self):
        print("2nd method of M class")


class N(M):
    def fn1(self):
        print("1st method of class N")


n1 = N()
n1.fn1()
n1.f2()
n1.f1()

print("------1.Normal Inheritance: - 1.2 Override super class methods--------")


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

print("------1.Normal Inheritance: - 1.3 Few Super classmeethods AS IS, few unique--------")


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


class MyTitle:
    def t1(self):
        print("My Title is Kujda ")


class MyName(MyTitle):
    def t1(self):
        print("My name Own title is Rain ")


n1 = MyName()
n1.t1()

'''
  1. 2L of Can <== 2L water - YES
  2. 5L of Can <== 5L water - YES
  3. 5L of Can <== 2L water - YES  (Memory Loss)  90%
  4. 2L of Can <== 5L water - NO  (Data Loss) 
x = 10
int x = 10
'''
'''
class Animal:
    def m1()

class Tiger(Animal):
    def m2()

Tiger tiger = new Tiger()    # 1    tiger.m1()
                                    tiger.m2()

Animal animal = new Animal() # 2    animal.m1()

Animal animal = new Tiger()  # 3**    animal.m1()
                                      animal.m2()  ==> Will give error


Tiger tiger = new Animal()   # 4    Error Downcasting



x = 10
print(x)  - 10
x = 10.5
print(x)  - 10.5

int x   = 10     # 1
float x = 10.5   # 2
float x = 10     # 3 Implicit casting   ==> float x = (float)10(internally converts)
int x = 10.5  XX # 4 Explict casting    ==> int x = (int)10.5 (externally you have to write)

'''
