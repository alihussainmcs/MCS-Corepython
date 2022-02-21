"""
https://medium.com/swift-india/concurrency-parallelism-threads-processes-async-and-sync-related-39fd951bc61d
Concurrency and Parallelism ->Way tasks are executed.
Synchronous and Asynchronous ->Programming model.
Single Threaded and Multi-Threaded ->The environment of task execution.
concurrency --> normal execution
parallelism --> same execution
"""
# 1 process 10 start
# 4 process 40 s
# 1s 2s 3s  4s 10 s 10s 11s  12s 13s

"""
def some_fun(a,b):
    sum = a+ b
    return sum
    
def some_fun2(sum,c):
    print('harsha)
    mul = sum * c
    return mul
    
first = some_fun(1,2)
second = some_fun2(8,3)

async def some_fun3(a,b):
    sum = a + b
    return sum

async def some_fun4(sum,c):
    print('harsha')
    mul = sum * c
    return mul
    
first = await some_fun(1,2)
second = await some_fun2(first,3)

    


"""
import threading

print("current thread:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not main thread")

name = threading.current_thread().getName()
print(name)

# 2. creating a thread and ue it to run

from threading import *


def movie():
    print("Movie running successfully in Theatres")


for i in range(5):
    m = Thread(target=movie())
    m.start()

# creating thread without using a class


import datetime
import time

start_time = datetime.datetime.now()


def some_fun2():
    print('above sleep')
    time.sleep(2)
    print('below sleep')


some_fun2()
some_fun2()
final_time = datetime.datetime.now() - start_time
print(f'time taken to execute', final_time)

thread_start_time = datetime.datetime.now()

t1 = Thread(target=some_fun2)
t2 = Thread(target=some_fun2)

t1.start()
t2.start()
t1.join()
t2.join()

thread_final_time = datetime.datetime.now() - thread_start_time
print('thread response time', thread_final_time)

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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder and wait for 5 minutes", self.name)
        sleep(2)
        print("done")

    def task2(self):
        print("Add sugar and wait for 3 minutes", self.name)
        sleep(2)
        print("done")

    def task3(self):
        print("filter it serve it === end", self.name)
        print("done")


obj = Mythread('harsha', 1)
class_start_time = datetime.datetime.now()
obj2 = Mythread('ranjith', 2)
t1 = Thread(target=obj.prepareTea())
t2 = Thread(target=obj2.prepareTea())

t1.start()
t2.start()
class_finish_time = datetime.datetime.now() - class_start_time

print('total time', class_finish_time)
