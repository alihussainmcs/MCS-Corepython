"""
Handling EOFError Exception in Python
EOFError is raised when one of the built-in functions input() or raw_input() hits an end-of-file condition (EOF)
without reading any data. This error is sometimes experienced while using online IDEs. This occurs when we have asked
the user for input but have not provided any input in the input box. We can overcome this issue by using try and except
keywords in Python. This is called as Exception Handling.

"""


"""
n = int(input())

print(n * 10)

"""


try:
    n = int(input())
    print(n * 10)

except EOFError as e:
    print(e)
   

