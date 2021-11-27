"""
├── OSError
│   ├── BlockingIOError
│   ├── ChildProcessError
│   ├── ConnectionError
│   │   ├── BrokenPipeError
│   │   ├── ConnectionAbortedError
│   │   ├── ConnectionRefusedError
│   │   └── ConnectionResetError
│   ├── FileExistsError
│   ├── FileNotFoundError
│   ├── InterruptedError
│   ├── IsADirectoryError
│   ├── NotADirectoryError
│   ├── PermissionError
│   ├── ProcessLookupError
│   └── TimeoutError

"""

"""
Handling OSError exception in Python
Last Updated : 19 Aug, 2020
Let us see how to handle OSError Exceptions in Python. OSError is a built-in exception in Python and serves as the 
error class for the os module, which is raised when an os specific system function returns a system-related error, 
including I/O failures such as “file not found” or “disk full”.
"""

# Importing os module
import os

# os.ttyname() # AttributeError: module 'os' has no attribute 'ttyname'
# method in Python is used to get the terminal
# device associated with the specified file descriptor.
# and raises an exception if the specified file descriptor
# is not associated with any terminal device.
print(os.ttyname(1))





















