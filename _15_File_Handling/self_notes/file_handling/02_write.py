# CRUD  ----- Create   Update

data = open('my_text_1.txt', 'w')
data.write('hi, my text file is ready \n')
data.writelines('hello, this is python txt file'
                'you can write in this file ')
data.close()

data_1 = open('my_text_1.txt')
# print(data_1.read())

for li in data_1:
    print(li.split('  '))


print('-------------------------------  2nd ex.  ----------------------------------------')

data = open('my_text_1.txt', 'w')
data.write('hi, my text file is ready \n')
data.writelines('hello, this is python txt file'
                'you can write in this file '""" This is by far the best answer here and deserves to be on top. One 
                could even write '.'*n to make it more clear. No joining, no zipping, no loops, no list comprehension; 
                just find the next two characters next to each other, which is exactly how a human brain thinks about 
                it. If Monty Python were still alive, he'd love this method! – 
SO_fix_the_vote_sorting_bug
 Dec 12 '18 at 1:27
1
This is the fastest method for reasonably long strings too: gitlab.com/snippets/1908857 – 
Ralph Bolton
 Oct 30 '19 at 16:03
6
This won't work if the string contains newlines. This needs flags=re.S. – 
Arian-Fey
 Nov 14 '19 at 17:17""")
data.close()

data_1 = open('my_text_1.txt')
print(data_1.read())

for li in data_1:
    print(li.split(' '))

print("---------------------------------------------------------------------------------------------------------")

# data_2 = open('new_file.txt', 'x') FileExistsError: [Errno 17] File exists: 'new_file.txt'
data_2 = open('new_file.txt', 'w')
data_2.write(""" Niklaus Wirth, a Swiss computer scientist, wrote a book in 1976 titled Algorithms + Data Structures = 
Programs.

40+ years later, that equation still holds true. That’s why software engineering candidates have to demonstrate their 
understanding of data structures along with their applications.

Almost all problems require the candidate to demonstrate a deep understanding of data structures. It doesn’t matter 
whether you have just graduated (from a university or coding bootcamp), or you have decades of experience.

Sometimes interview questions explicitly mention a data structure, for example_1, “given a binary tree.” Other times 
it’s implicit, like “we want to track the number of books associated with each author.”

Learning data structures is essential even if you’re just trying to get better at your current job. Let’s start with 
understanding the basics.

What is a Data Structure?
Simply put, a data structure is a container that stores data in a specific layout. This “layout” allows a data 
structure to be efficient in some operations and inefficient in others. Your goal is to understand data structures 
so that you can pick the data structure that’s most optimal for the problem at hand.

Why do we need Data Structures?
As data structures are used to store data in an organized form, and since data is the most crucial entity in computer 
science, the true worth of data structures is clear.

No matter what problem are you solving, in one way or another you have to deal with data — whether it’s an employee’s 
salary, stock prices, a grocery list, or even a simple telephone directory.

Based on different scenarios, data needs to be stored in a specific format. We have a handful of data structures that 
cover our need to store data in different formats.

Commonly used Data Structures
Let’s first list the most commonly used data structures, and then we’ll cover them one by one:

Arrays
Stacks
Queues
Linked Lists
Trees
Graphs
Tries (they are effectively trees, but it’s still good to call them out separately).
Hash Tables
Arrays
An array is the simplest and most widely used data structure. Other data structures like stacks and queues are derived
from arrays.

Here’s an image of a simple array of size 4, containing elements (1, 2, 3 and 4).""")

data_2.close()

data_3 = open('my_text_1.txt')
print(data_3.read(100))

print("-----------------------------------------------------------")

print(data_3.readlines(100))

print("-----------------------------------------------------------")

print(data_3.readline(100))
