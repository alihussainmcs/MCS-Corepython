"""
Multithreading in Python 3
A thread is the smallest unit of a program or process executed independently or scheduled by the Operating System.
  In the computer system, an Operating System achieves multitasking by dividing the process into threads. A thread is
  a lightweight process that ensures the execution of the process separately on the system. In Python 3, when multiple
  processors are running on a program, each processor runs simultaneously to execute its tasks separately.

Python Multithreading
Multithreading is a threading technique in Python programming to run multiple threads concurrently by rapidly switching
   between threads with a CPU help (called context switching). Besides, it allows sharing of its data space with the
   main threads inside a process that share information and communication with other threads easier than individual
   processes. Multithreading aims to perform multiple tasks simultaneously, which increases performance, speed and
   improves the rendering of the application.

Note: The Python Global Interpreter Lock (GIL) allows running a single thread at a time, even the machine has multiple
   processors.
Benefits of Multithreading in Python
Following are the benefits to create a multithreading application in Python, as follows:

It ensures effective utilization of computer system resources.
Multithreading applications are more responsive.
It shares resources and its state with sub-threads (child) which makes it more economical.
It makes the multiprocessor architecture more effective due to similarity.
It saves time by executing multiple threads at the same time.
The system does not require too much memory to store multiple threads.

When to use Multithreading in Python?
It is a very useful technique for time-saving and improving the performance of an application. Multithreading allows
   the programmer to divide application tasks into sub-tasks and simultaneously run them in a program. It allows
   threads to communicate and share resources such as files, data, and memory to the same processor. Furthermore,
   it increases the user's responsiveness to continue running a program even if a part of the application is the
   length or blocked.


How to achieve multithreading in Python?
There are two main modules of multithreading used to handle threads in Python
.

The thread module
The threading module
Thread modules
It is started with Python 3, designated as obsolete, and can only be accessed with _thread that supports backward
   compatibility.

Syntax:

thread.start_new_thread ( function_name, args[, kwargs] )
To implement the thread module in Python, we need to import a thread module and then define a function that performs
   some action by setting the target with a variable.

"""

import time  # import time module


def cal_sqre(num):  # define the cal_sqre function
    print(" Calculate the square root of the given number")
    for n in num:
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(' Square is : ', n * n)


def cal_cube(num):  # define the cal_cube() function
    print(" Calculate the cube of  the given number")
    for n in num:
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(" Cube is : ", n * n * n)


arr = [4, 5, 6, 7, 2]  # given array

t1 = time.time()  # get total time to execute the functions
cal_sqre(arr)  # call cal_sqre() function
cal_cube(arr)  # call cal_cube() function

print(" Total time taken by threads is :", time.time() - t1)  # print the total time

print("--------------------------------------------------------------------------------")

"""
Threading Modules
The threading module is a high-level implementation of multithreading used to deploy an application in Python
. To use multithreading, we need to import the threading module in Python Program
.

Thread Class Methods


Methods	  Description
start()	  A start() method is used to initiate the activity of a thread. And it calls only once for each thread so that 
              the execution of the thread can begin.
run()	  A run() method is used to define a thread's activity and can be overridden by a class that extends the threads 
             class.
join()	  A join() method is used to block the execution of another code until the thread terminates.

Follow the given below steps to implement the threading module in Python Multithreading:

1. Import the threading module

Create a new thread by importing the threading module, as shown.

Syntax:

import threading  
A threading module is made up of a Thread class, which is instantiated to create a Python thread.


2. Declaration of the thread parameters: It contains the target function, argument, and kwargs as the parameter in the 
    Thread() class.

Target: It defines the function name that is executed by the thread.
Args: It defines the arguments that are passed to the target function name.
For example_1:

"""

import threading


def print_hello(n):
    print("Hello, how old are you ", n)


t1 = threading.Thread(target=print_hello, args=(18,))

'''
In the above code, we invoked the print_hello() function as the target parameter. The print_hello() contains one 
   parameter n, which passed to the args parameter.


3. Start a new thread: To start a thread in Python multithreading, call the thread class's object. The start() method 
      can be called once for each thread object; otherwise, it throws an exception error.

Syntax:
'''
t1.start()

'''
4. Join method: It is a join() method used in the thread class to halt the main thread's execution and waits till the 
    complete execution of the thread object. When the thread object is completed, it starts the execution of the main 
     thread in Python.

'''
print("---------------------------------------------------------------------")
import threading


def print_hello(n):
    print("Hello, how old are you? ", n)


T1 = threading.Thread(target=print_hello, args=(20,))
T1.start()
T1.join()
print("Thank you")

'''
When the above program is executed, the join() method halts the execution of the main thread and waits until the thread 
    t1 is completely executed. Once the t1 is successfully executed, the main thread starts its execution.

Note: If we do not use the join() method, the interpreter can execute any print statement inside the Python program. 
    Generally, it executes the first print statement because the interpreter executes the lines of codes from the 
    program's start.
    
5. Synchronizing Threads in Python

It is a thread synchronization mechanism that ensures no two threads can simultaneously execute a particular segment 
   inside the program to access the shared resources. The situation may be termed as critical sections. We use a race 
    condition to avoid the critical section condition, in which two threads do not access resources at the same time.

Let's write a program to use the threading module in Python Multithreading.

'''
print("------------------------------------------------------------------------------------")

import time  # import time module
import threading


def cal_sqre(num):  # define a square calculating function
    print(" Calculate the square root of the given number")
    for n in num:  # Use for loop
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(' Square is : ', n * n)


def cal_cube(num):  # define a cube calculating function
    print(" Calculate the cube of  the given number")
    for n in num:  # for loop
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(" Cube is : ", n * n * n)


ar = [4, 5, 6, 7, 2]  # given array

t = time.time()  # get total time to execute the functions
# cal_cube(ar)
# cal_sqre(ar)
th1 = threading.Thread(target=cal_sqre, args=(ar,))
th2 = threading.Thread(target=cal_cube, args=(ar,))
th1.start()
th2.start()
th1.join()
th2.join()
print(" Total time taking by threads is :", time.time() - t)  # print the total time
print(" Again executing the main thread")
print(" Thread 1 and Thread 2 have finished their execution.")
