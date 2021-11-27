# P01. REQ : to set the indentation of the first line

"""
1. CRUD       - Retrieve
2. STATE      - String
3. BEHAVIOR   - str
"""

"""
Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement. 
The statements with the same indentation belong to the same group called a suite.
"""
# 0. Mathematics
"""
1. Initialize a string 
2. retrieve the string with new line
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")


msg = 'Good mood bad mood'
print("String : ", msg)
print('String length :', len(msg))
print('String before indentation of first line:', msg.center(18, '\n'))

print('String after indentation of first line :', msg.center(19, '\n'))

# 2. Algorithm

print("--------2 Algorithm              ----------")
import textwrap
sample_text = '''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 = textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()
# 3 Using Functions
print("--------3 Using Functions        ----------")

# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
