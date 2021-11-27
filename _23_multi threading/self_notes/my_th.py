"""
Running several threads is similar to running several different programs concurrently, but with the following benefits −

Multiple threads within a process share the same data space with the main thread and can therefore share information
or communicate with each other more easily than if they were separate processes.

Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than
processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of
where within its context it is currently running.

It can be pre-empted (interrupted)

It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.

Starting a New Thread
To spawn another thread, you need to call following method available in thread module −

thread.start_new_thread ( function, args[, kwargs] )
This method call enables a fast and efficient way to create new threads in both Linux and Windows.

The method call returns immediately and the child thread starts and calls function with the passed list of args. When
function returns, the thread terminates.

Here, args is a tuple of arguments; use an empty tuple to call function without passing any arguments. kwargs is an
optional dictionary of keyword arguments.

Example

"""

import threading

print("current thread:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not main thread")

name = threading.current_thread().getName()
print(name)


# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

def print_cube(num):
	"""
	function to print cube of given num
	"""
	print("Cube: {}".format(num * num * num))

def print_square(num):
	"""
	function to print square of given num
	"""
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")
