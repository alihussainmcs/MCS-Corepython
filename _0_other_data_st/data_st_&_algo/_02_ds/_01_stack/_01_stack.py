"""
Stack Data Structure
In this tutorial, you will learn about the stack data structure and its implementation in Python.

A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element
inserted inside the stack is removed first.

You can think of the stack data structure as the pile of plates on top of another.

elements on stack are added on top and removed from top just like a pile of plate
Here, you can:

Put a new plate on top
Remove the top plate
And, if you want the plate at the bottom, you must first remove all the plates on top. This is exactly how the stack
data structure works.

LIFO Principle of Stack
In programming terms, putting an item on top of the stack is called push and removing an item is called pop.


We can implement a stack in any programming language like Python, C, Java.

Basic Operations of Stack

There are some basic operations that allow us to perform different actions on a stack.

Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
Working of Stack Data Structure
The operations work as follows:

A pointer called TOP is used to keep track of the top element in the stack.
When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
On popping an element, we return the element pointed to by TOP and reduce its value.
Before pushing, we check if the stack is already full
Before popping, we check if the stack is already empty
Adding elements to the top of stack and removing elements from the top of stack

Stack Implementations in Python
The most common stack implementation is using arrays, but it can also be implemented using lists.

Python

# Stack implementation in python
"""


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if check_empty(stack):
        return "stack is empty"

    return stack.pop()


stack1 = create_stack()
push(stack1, str(1))
push(stack1, str(2))
push(stack1, str(3))
push(stack1, str(4))
print("popped item: " + pop(stack1))
print("stack after popping an element: " + str(stack1))

"""
Stack Time Complexity
For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).

Applications of Stack Data Structure
Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:

To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get 
the letters in reverse order.
In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the 
expression to prefix or postfix form.
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you 
visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the 
stack, and the previous URL is accessed.
"""
