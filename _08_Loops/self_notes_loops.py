"""
Python Loops – Learn one of the most powerful concepts in programming
Loops are one of the most powerful and basic concepts in programming. A loop can contain a set of statements that
keeps on executing until a specific condition is reached.

Today, we are going to learn about the loops that are available in Python. In Python loops, we will study For loop,
 while loop, nested loops and loop control statements.

Python Loops
Let’s suppose you have a task to do which is to be executed a thousand times.

Here, programming languages provide us with the concept of loops which helps us execute some task n number of
times where n can be any whole number. They are pretty useful and can be applied to various use cases.

1. Python For in loop
For loop in Python is used to iterate over a sequence of items like list, tuple, set, dictionary, string or any
other iterable objects.

Syntax:


for item in sequence:
    body of for loop
The Python for loop doesn’t need indexing unlike other programming languages (C/C++ or Java). It works like an iterator
 and the item variable will contain an item from the sequence at each iteration.

The for loop continues until we reach the end of the sequence.

Flowchart of for loop in PythonFlowchart of for loop in Python

Code:

for item in [1,2,3,4]:
    print( item)
Output:

1
2
3
4
a. The range() function
When using for loops in Python, the range() function is pretty useful to specify the number of times the loop is
executed. It yields a sequence of numbers within a specified range.

Syntax:

range(start, stop, step)
The first argument is the starting value. It is zero by default.
The second argument is the ending value of the range.
The third argument is the number of steps to take after each yield.

#converting range to list

Code:

list(range(10))
list(range(4,10))
list(range(2,10,2))
Output:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9],
[2, 4, 6, 8]
b. Iterating over range object
You can use the for loop to iterate over the range of objects.

Code:

for i in range(2,20,2):
  print(i)
Output:

2
4
6
8
10
12
14
16
18
Similarly, we can iterate the same way in tuples, lists, sets, and strings.

Code:

for char in “Hello”:
  print(char)
Output:


H
e
l
l
o
—
c. Using else in for loop
In Python programming, the loops can also have an else part which will be executed once when the loop terminates.

Code:

for i in [1, 2, 3, 4]:
  print(i)
else:
  print(“The loop ended”)
Output:

1
2
3
4
The loop ended
2. Python While loop
The while loop in Python executes a block of code until the specified condition becomes False.

Flowchart of while loop in PythonFlowchart of while loop in Python

Syntax:


while( condition):
  Body of while
  Inside while block
Code:

count = 0
while( count< 10):
  print(count)
  count = count + 2
Output:

0
2
4
6
8
In the example_1, the while statement checks if count is less than 10.

Initially, count is zero so the statement is true and it executes the body of while. Then the count gets incremented
by 2. Again we check the condition and this goes on till the condition becomes false.

Here, when our code checks 10<10, the statement returns False and so the code in while block is not executed.

a. Infinite loop
A loop is called an infinite loop when the loop will never reach its end.

Usually, when a condition is always True in a while loop, the loop will become an infinite loop. So we should be
careful when writing conditions and while updating variables used in the loop.

In Python shell, we can the program on an infinite loop by using CTRL + C. Sometimes, we need to implement an
infinite terminate loop for example_1, when reading frames from a webcam.

Code:

while (True):
    print(“Infinite Loop”)
This code will keep on printing the “Infinite Loop” statement. We terminate the loop by pressing CTRL + C.


b. Using else in while loop
The while loop may also have an else part after the loop. It is executed only when the condition of while loop
becomes false. But if we break out of the loop before the condition has not reached false, then the else block
does not get executed.

Code:

num = 0
while( num<10 ):
    print(num)
    num += 1
    if( num==5):
        break
else:
    print('Loop ended')
Output:

0
1
2
3
4
Here the else statement didn’t get executed because the break statement ends the loop execution and the while condition
 therefore never becomes false.

3. Python Nested Loops
We can nest a loop inside another loop which simply means that a loop within a loop. Let’s see this with an example_1.

Code:

for num1 in range(3):
    for num2 in range(5, 8):
        print(num1, ",", num2)
Output:

0 , 5
0 , 6
0 , 7
1 , 5
1 , 6
1 , 7
2 , 5
2 , 6
2 , 7
From this example_1, you can observe that the first iteration of the outer loop will run the whole inner loop and then
in the next iteration of the outer loop, the inner loop gets executed again. This process is repeated until we
reach the end of the outer loop.


4. Loop Control Statements in Pythonpython loop control statements


Python allows us to control the flow of the execution of the program in a certain manner. For this we use the
continue, break and pass keywords.

a. break
The break statement inside a loop is used to exit out of the loop. Sometimes in a program, we need to exit the
loop when a certain condition is fulfilled.

Code:


num = 0
while( num <10 ):
    num +=1
    if(num==5): break
    print( num )
print("Loop ended")
Output:

1
2
3
4
Loop ended
In this loop, we are incrementing the value of num variable and then printing it. When the num value becomes 5
the break statement is executed which terminates the loop and therefore loop is not executed further.

b. continue
The continue statement is used to skip the next statements in the loop.

When the program reaches the continue statement, the program skips the statements after continue and the flow
 reaches the next iteration of the loop.

Let’s take the same example_1 –

Code:

num = 0
while( num <10 ):
    num +=1
    if(num==5): continue
    print( num )
print("Loop ended")
Output:

1
2
3
4
6
7
8
9
10
Loop ended
Here, we see that when the num variable is equal to 5, the continue statement is executed. It then doesn’t
execute the lines after the continue statement and the control is sent to the next iteration.


c. pass
The pass is a null statement and the Python interpreter returns a no-operation (NOP) after reading the pass
 statement. Nothing happens when the pass statement is executed. It is used as a placeholder when implementing
 new methods or we can use them in exception handling.

Code:

nums = [1,2,3,4]
for num in nums:
  pass
print(nums)
Summary
To sum up, we learned how the concepts of loops are useful for us programmers to do repetitive tasks
effectively with the help of loops. We saw examples and syntax of different types of Python loops, which
are for loop and while loop. We also saw that we can use else statements with a for or while loop.

Moreover, we saw nested loop and loop control statements which helps to change the normal flow of the loop.



"""

print('these are loops ..........')
