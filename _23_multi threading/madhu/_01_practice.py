import threading

print("current thread:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not main thread")

name = threading.current_thread().getName()
print(name)

print("--------------------------------------------------------------------------")
# 2. creating a thread and ue it to run

from threading import *


def movie():
    print("Movie running successfully in Theatres")


for i in range(5):
    m = Thread(target=movie())
    m.start()

# creating thread without using a class
from threading import *


def display(str):
    print(str)


for i in range(5):
    t = Thread(target=display('hello'), args='hello')
    t.start()

# Class Mythread(thread):
# t1 = mythread
# t1.join

# python program to create a thread by making our class as sub class to thread class

from threading import Thread


class Mythread(Thread):
    def run(self):
        for i in range(1, 6):
            print(i)


t1 = Mythread()
t1.start()
t1.join()

# program to create thread tha access the instance variables

'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print("get details:", self.name, self.age)

s = Student('raja', 26)
s2 = Student("super", 26)
s2.get_details()
s.get_details()
'''
from threading import *
from time import *


class Mythread:

    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder and wait for 5 minutes")
        sleep(5)
        print("done")

    def task2(self):
        print("Add sugar and wait for 3 minutes")
        sleep(3)
        print("done")

    def task3(self):
        print("filter it serve it === end")
        print("done")


obj = Mythread()
t = Thread(target=obj.prepareTea())

t.start()
