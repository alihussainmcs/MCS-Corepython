
import threading

print("current thread:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not main thread")

name = threading.current_thread().getName()
print(name)
