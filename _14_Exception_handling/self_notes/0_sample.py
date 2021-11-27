
"""
Exceptions

Exception
├── ArithmeticError
│   ├── FloatingPointError
│   ├── OverflowError
│   └── ZeroDivisionError
├── AssertionError
├── AttributeError
├── BufferError
├── EOFError
├── ImportError
│   └── ModuleNotFoundError
├── LookupError
│   ├── IndexError
│   └── KeyError
├── MemoryError
├── NameError
│   └── UnboundLocalError
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
├── ReferenceError
├── RuntimeError
│   ├── NotImplementedError
│   └── RecursionError
├── StopAsyncIteration
├── StopIteration
├── SyntaxError
│   └── IndentationError
│       └── TabError
├── SystemError
├── TypeError
├── ValueError
│   └── UnicodeError
│       ├── UnicodeDecodeError
│       ├── UnicodeEncodeError
│       └── UnicodeTranslateError
└── Warning
    ├── BytesWarning
    ├── DeprecationWarning
    ├── FutureWarning
    ├── ImportWarning
    ├── PendingDeprecationWarning
    ├── ResourceWarning
    ├── RuntimeWarning
    ├── SyntaxWarning
    ├── UnicodeWarning
    └── UserWarning
"""

# Exception handling
"""
Traceback (most recent call last):
  File "C:/Users/0_sir_notes/git_projects/Batch_16/B16_PythonTraining/_14_Exception_handling/mypractice/test1.py", line 11, in <module>
    print("Result is ", in_val + 10)
TypeError: must be str, not int
"""
list1 = [1, 2, 3, 4]
# print(list1[12])  # IndexError: list index out of range
print("-- list1----", list1)

try:
    list1[12]
except IndexError:
    print('list index out of range')

# in_val = input("Enter value : ")  # '5'
# print("Result is ", in_val + 5)  # TypeError: must be str, not int

print("----------------------------------------------------------------------")
# print(x)  # NameError: name 'x' is not defined

try:
    print(x)
except NameError:
    print("Variable x is not defined")

print("----------------------------------------------------------------------")

try:
    print(a)
except NameError:
    print("a value not defined ")

