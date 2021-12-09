x = 10
print("x details : ", x, id(x))


# Function memory allocation

def get_data():   # Function invocation
    print("Welcome to my method")
    return "Hello World"


res = get_data()   # Function calling
print("Result is : ", res)

print("Function details ", get_data)  # Get function body address

# Pass by value ,Pass by reference
"""
Pass by reference vs value in Python
Developers jumping into Python programming from other languages like C++ and Java are often confused by the process 
of passing arguments in Python. The object-centric data model and its treatment of assignment is the cause behind 
the confusion at the fundamental level. In the article below we will be discussing the concept of passing arguments 
in Python and try to understand it with the help of examples.

Is Python Argument Passing model a “Pass by Value” or “Pass by Reference”?
You might want to punch something after reading ahead, so brace yourself. Python’s argument passing model is 
neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.

 Attention geek! Strengthen your foundations with the Python Programming Foundation Course and learn the basics.  

To begin with, your interview preparations Enhance your Data Structures concepts with the Python DS Course. 
And to begin with your Machine Learning Journey, join the Machine Learning - Basic Level Course

The paradigms of “Pass by value”, “Pass by Reference” and “Pass by object Reference” can be understood by 
exploring the below example_1 functions.
Look into the two functions defined below:
"""


def set_list(_):
    lst = ["A", "B", "C"]
    return lst


def add(lst):
    lst.append("D")
    return lst


my_list = ["E"]

print(set_list(my_list))

print(add(my_list))
"""
Output:

['A', 'B', 'C']
['E', 'D']
Now, let’s explore the above code,

The variable is not the object passed:
What if I tell you The Ramayana was not written by Tulsi Das but The Ramayana was written by a man named Tulsi Das.
 Does that distinction make any sense? No right?!. But according to Python it does and it makes a crucial distinction.
  So, in Python and its PKD’s, there is a big difference between the thing and the label we use to refer to that thing.
   “A man named Tulsi Das ” is just a man and “Tulsi Das” is a name used to refer to that man.
So, consider a list

 a = ["X", "Y"]
Here “a” is a variable that points to a list containing the element “X” and “Y”. But “a” itself is not the list. 
Consider “a” to be a bucket that contains the object “X” and “Y”.

Pass by Reference:

In pass by reference the variable( the bucket) is passed into the function directly. The variable acts a Package 
that comes with it’s contents(the objects).

In the above code image both “list” and “my_list” are the same container variable and therefore refer to the exact 
same object in the memory. Any operation performed by the function on the variable or the object will be directly 
reflected to the function caller. For instance, the function could completely change the variable’s content, 
and point it at a completely different object:

Also, the function can reassign the contents of the variable with the same effect as below:

To summarize, in pass by reference the function and the caller use the same variable and object.

Pass by Value:

In pass by value the function is provided with a copy of the argument object passed to it by the caller. That means the
original object stays intact and all changes made are to a copy of the same and stored at different memory locations.

The same is true for any operation performed by the function on the variable or the object

To summarize the copies of the variables and the objects in the context of the caller of the function are completely 
isolated.

Pass Object by Reference:

As python is different in this context, the functions in python receive the reference of the same object in the
 memory as referred by the caller. However, the function does not receive the variable(the bucket) that the caller 
 is storing the same object in; like in pass-by-value, the function provides its own bucket and creates an entirely 
 new variable for itself.

The same object in the memory is referred by both the caller and the function, so when the append function adds an 
extra element to the list, the caller object gets updated too. They have different names but are the same thing. 
Both the variables contain the same object. This is the meaning behind pass by object reference. The function and
 caller use the same object in memory, but get them through different variables. Any changes made to the function
  variable(bucket) won’t change the nature of the caller variable (bucket), only the content gets updated.
"""

# Mutable,Immutable


"""
Understanding Mutable and Immutable in Python
Mutable and Immutable in Python
Mutable Definition
Immutable Definition
List of Mutable and Immutable objects
Objects in Python
Mutable Objects in Python
Immutable Objects in Python
Immutability of Tuple
Exceptions in immutability
FAQs
What is the difference between mutable vs immutable in Python?
What are the mutable and immutable data types in Python?
Are lists mutable in Python?
Why are tuples called immutable types?
Are sets mutable in Python?
Are strings mutable in Python?

Mutable and Immutable in Python
Mutable is a fancy way of saying that the internal state of the object is changed/mutated. So, the simplest 
definition is: An object whose internal state can be changed is mutable. On the other hand, immutable doesn’t allow 
any change in the object once it has been created.

Mutable Definition
Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of 
objects to change their values. These are often the objects that store a collection of data.

Immutable Definition
Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed 
over time, then it is known as immutable. Once created, the value of these objects is permanent.

List of Mutable and Immutable objects
Objects of built-in type that are mutable are:

Lists
Sets
Dictionaries
User-Defined Classes (It purely depends upon the user to define the characteristics) 
Objects of built-in type that are immutable are:

Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
Strings
Tuples
Frozen Sets
User-Defined Classes (It purely depends upon the user to define the characteristics)
Object mutability is one of the characteristics that makes Python a dynamically typed language. Though Mutable and 
Immutable in Python is a very basic concept, it can at times be a little confusing due to the intransitive nature of
 immutability.

Objects in Python
In Python, everything is treated as an object. Every object has these three attributes:

Identity – This refers to the address that the object refers to in the computer’s memory.
Type – This refers to the kind of object that is created. For example_1- integer, list, string etc. 
Value – This refers to the value stored by the object. For example_1 – List=[1,2,3] would hold the numbers 1,2 and 3
While ID and Type cannot be changed once it’s created, values can be changed for Mutable objects.

Mutable Objects in Python
I believe, rather than diving deep into the theory aspects of mutable and immutable in Python, a simple code would
 be the best way to depict what it means in Python. Hence, let us discuss the below code step-by-step:
"""
# Creating a list which contains name of Indian cities

cities = ['Delhi', 'Mumbai', 'Kolkata']
# Printing the elements from the list cities, separated by a comma & space
print("list cities :", cities)
for city in cities:
    print(city, end=',')

"""
Output [1]: Delhi, Mumbai, Kolkata
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))

Output [2]: 0x1691d7de8c8
#Adding a new city to the list cities

cities.append(‘Chennai’)
#Printing the elements from the list cities, separated by a comma & space 

for city in cities:
	print(city, end=’, ’)

Output [3]: Delhi, Mumbai, Kolkata, Chennai
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))

Output [4]: 0x1691d7de8c8
The above example_1 shows us that we were able to change the internal state of the object ‘cities’ by adding one 
more city ‘Chennai’ to it, yet, the memory address of the object did not change. This confirms that we did not 
create a new object, rather, the same object was changed or mutated. Hence, we can say that the object which is a
 type of list with reference variable name ‘cities’ is a MUTABLE OBJECT.

Let us now discuss the term IMMUTABLE. Considering that we understood what mutable stands for, it is obvious that 
the definition of immutable will have ‘NOT’ included in it. Here is the simplest definition of immutable– An object
 whose internal state can NOT be changed is IMMUTABLE.


Again, if you try and concentrate on different error messages, you have encountered, thrown by the respective IDE; 
you use you would be able to identify the immutable objects in Python. For instance, consider the below code & 
associated error message with it, while trying to change the value of a Tuple at index 0. 

#Creating a Tuple with variable name ‘foo’

foo = (1, 2)
#Changing the index[0] value from 1 to 3

foo[0] = 3

TypeError: 'tuple' object does not support item assignment 
Immutable Objects in Python
Once again, a simple code would be the best way to depict what immutable stands for. Hence, let us discuss the below
 code step-by-step:

#Creating a Tuple which contains English name of weekdays

weekdays = ‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’
# Printing the elements of tuple weekdays

print(weekdays)

Output [1]:  (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’)
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(weekdays)))

Output [2]: 0x1691cc35090
#tuples are immutable, so you cannot add new elements, hence, using merge of tuples with the # + operator to add a new
 imaginary day in the tuple ‘weekdays’

weekdays  +=  ‘Pythonday’,
#Printing the elements of tuple weekdays

print(weekdays)

Output [3]: (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’, ‘Pythonday’)
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(weekdays)))

Output [4]: 0x1691cc8ad68

This above example_1 shows that we were able to use the same variable name that is referencing an object which is a 
type of tuple with seven elements in it. However, the ID or the memory location of the old & new tuple is not the 
same. We were not able to change the internal state of the object ‘weekdays’. The Python program manager created a 
new object in the memory address and the variable name ‘weekdays’ started referencing the new object with eight
 elements in it.  Hence, we can say that the object which is a type of tuple with reference variable name ‘weekdays’
  is an IMMUTABLE OBJECT.

Also Read: Understanding the Exploratory Data Analysis (EDA) in Python

Where can you use mutable and immutable objects:

Mutable objects can be used where you want to allow for any updates. For example_1, you have a list of employee names
 in your organizations, and that needs to be updated every time a new member is hired. You can create a mutable list,
  and it can be updated easily.

Immutability offers a lot of useful applications to different sensitive tasks we do in a network centred environment 
where we allow for parallel processing. By creating immutable objects, you seal the values and ensure that no threads
 can invoke overwrite/update to your data. This is also useful in situations where you would like to write a piece of
  code that cannot be modified. For example_1, a debug code that attempts to find the value of an immutable object.

Watch outs:  Non transitive nature of Immutability:

OK! Now we do understand what mutable & immutable objects in Python are. Let’s go ahead and discuss the combination
 of these two and explore the possibilities. Let’s discuss, as to how will it behave if you have an immutable object 
 which contains the mutable object(s)? Or vice versa? Let us again use a code to understand this behaviour–

#creating a tuple (immutable object) which contains 2 lists(mutable) as it’s elements

#The elements (lists) contains the name, age & gender 

person = (['Ayaan', 5, 'Male'], ['Aaradhya', 8, 'Female'])
#printing the tuple

print(person)

Output [1]: (['Ayaan', 5, 'Male'], ['Aaradhya', 8, 'Female'])

#printing the location of the object created in the memory address in hexadecimal format

print(hex(id(person)))

Output [2]: 0x1691ef47f88
#Changing the age for the 1st element. Selecting 1st element of tuple by using indexing [0] then 2nd element of 
the list by using indexing [1] and assigning a new value for age as 4

person[0][1] = 4
#printing the updated tuple

print(person)

Output [3]: (['Ayaan', 4, 'Male'], ['Aaradhya', 8, 'Female'])
#printing the location of the object created in the memory address in hexadecimal format

print(hex(id(person)))

Output [4]: 0x1691ef47f88
In the above code, you can see that the object ‘person’ is immutable since it is a type of tuple. However, it has two
lists as it’s elements, and we can change the state of lists (lists being mutable). So, here we did not change the 
object reference inside the Tuple, but the referenced object was mutated.

Also Read: Real-Time Object Detection Using TensorFlow

Same way, let’s explore how it will behave if you have a mutable object which contains an immutable object? Let us 
again use a code to understand the behaviour–

#creating a list (mutable object) which contains tuples(immutable) as it’s elements

list1 = [(1, 2, 3), (4, 5, 6)]
#printing the list

print(list1)

Output [1]: [(1, 2, 3), (4, 5, 6)]

#printing the location of the object created in the memory address in hexadecimal format

print(hex(id(list1)))

Output [2]: 0x1691d5b13c8	
#changing object reference at index 0

list1[0] = (7, 8, 9)
#printing the list

Output [3]: [(7, 8, 9), (4, 5, 6)]
#printing the location of the object created in the memory address in hexadecimal format

print(hex(id(list1)))

Output [4]: 0x1691d5b13c8
As an individual, it completely depends upon you and your requirements as to what kind of data structure you would 
like to create with a combination of mutable & immutable objects. I hope that this information will help you while 
deciding the type of object you would like to select going forward.

Before I end our discussion on IMMUTABILITY, allow me to use the word ‘CAVITE’ when we discuss the String and 
Integers. There is an exception, and you may see some surprising results while checking the truthiness for 
immutability. For instance:
#creating an object of integer type with value 10 and reference variable name ‘x’ 

x = 10

#printing the value of ‘x’

print(x)

Output [1]: 10
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(x)))

Output [2]: 0x538fb560

#creating an object of integer type with value 10 and reference variable name ‘y’

y = 10
#printing the value of ‘y’

print(y)

Output [3]: 10
#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(y)))

Output [4]: 0x538fb560
As per our discussion and understanding, so far, the memory address for x & y should have been different, since, 
10 is an instance of Integer class which is immutable. However, as shown in the above code, it has the same memory
 address. This is not something that we expected. It seems that what we have understood and discussed, has an 
 exception as well.

Immutability of Tuple
Tuples are immutable and hence cannot have any changes in them once they are created in Python. This is because 
they support the same sequence operations as strings. We all know that strings are immutable. The index operator will 
select an element from a tuple just like in a string. Hence, they are immutable.

Exceptions in immutability
Like all, there are exceptions in the immutability in python too. Not all immutable objects are really mutable. 
This will lead to a lot of doubts in your mind. Let us just take an example_1 to understand this.

Consider a tuple ‘tup’.

Now, if we consider tuple tup = (‘GreatLearning’,[4,3,1,2]) ;

We see that the tuple has elements of different data types. The first element here is a string which as we all know 
is immutable in nature. The second element is a list which we all know is mutable. Now, we all know that the tuple 
itself is an immutable data type. It cannot change its contents. But, the list inside it can change its contents.
 So, the value of the Immutable objects cannot be changed but its constituent objects can. change its value.

FAQs
1. Difference between mutable vs immutable in Python?
Mutable Object	Immutable Object
State of the object can be modified after it is created.	State of the object can’t be modified once it is created.
They are not thread safe.	They are thread safe
Mutable classes are not final.	It is important to make the class final before creating an immutable object.
2. What are the mutable and immutable data types in Python?
Some mutable data types in Python are:
list, dictionary, set, user-defined classes.

Some immutable data types are: 
int, float, decimal, bool, string, tuple, range.

3. Are lists mutable in Python?
Lists in Python are mutable data types as the elements of the list can be modified, individual elements can be
 replaced, and the order of elements can be changed even after the list has been created.
(Examples related to lists have been discussed earlier in this blog.)

4. Why are tuples called immutable types?
Tuple and list data structures are very similar, but one big difference between the data types is that lists are
 mutable, whereas tuples are immutable. The reason for the tuple’s immutability is that once the elements are added 
 to the tuple and the tuple has been created; it remains unchanged.

A programmer would always prefer building a code that can be reused instead of making the whole data object again.
 Still, even though tuples are immutable, like lists, they can contain any Python object, including mutable objects.

5. Are sets mutable in Python?
A set is an iterable unordered collection of data type which can be used to perform mathematical operations 
(like union, intersection, difference etc.). Every element in a set is unique and immutable, i.e. no duplicate 
values should be there, and the values can’t be changed. However, we can add or remove items from the set as 
the set itself is mutable.

6. Are strings mutable in Python?
Strings are not mutable in Python. Strings are a immutable data types which means that its value cannot be updated.

Join Great Learning Academy’s free online courses and upgrade your skills today.
"""

# Copy : Shallow copy,Deep copy


"""
Python Shallow Copy and Deep Copy
In this article, you’ll learn about shallow copy and deep copy in Python with the help of examples.

Copy an Object in Python
In Python, we use = operator to create a copy of an object. You may think that this creates a new object; 
it doesn't. It only creates a new variable that shares the reference of the original object.

Let's take an example_1 where we create a list named old_list and pass an object reference to new_list using = operator.

Example 1: Copy using = operator
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
When we run above program, the output will be:

Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Old List: 140673303268168

New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of New List: 140673303268168
As you can see from the output both variables old_list and new_list shares the same id i.e 140673303268168.

So, if you want to modify any values in new_list or old_list, the change is visible in both.

Essentially, sometimes you may want to have the original values unchanged and only modify the new values or 
vice versa. In Python, there are two ways to create copies:

Shallow Copy
Deep Copy
To make these copy work, we use the copy module.

Copy Module
We use the copy module of Python for shallow and deep copy operations. Suppose, you need to copy the compound 
list say x. For example_1:

import copy
copy.copy(x)
copy.deepcopy(x)
Here, the copy() return a shallow copy of x. Similarly, deepcopy() return a deep copy of x.

Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects.
 This means, a copy process does not recurse or create copies of nested objects itself.

Example 2: Create a copy using shallow copy
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
When we run the program , the output will be:

Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
In above program, we created a nested list and then shallow copy it using copy() method.

This means it will create new and independent object with same content. To verify this, we print the both old_list 
and new_list.


To confirm that new_list is different from old_list, we try to add new nested object to original and check it.

Example 3: Adding [4, 4, 4] to old_list, using shallow copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
When we run the program, it will output:

Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
In the above program, we created a shallow copy of old_list. The new_list contains references to original nested 
objects stored in old_list. Then we add the new list i.e [4, 4, 4] into old_list. This new sublist was not copied
 in new_list.

However, when you change any nested objects in old_list, the changes appear in new_list.

Example 4: Adding new nested object using Shallow copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
When we run the program, it will output:

Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
In the above program, we made changes to old_list i.e old_list[1][1] = 'AA'. Both sublists of old_list and new_list 
at index [1][1] were modified. This is because, both lists share the reference of same nested objects.

Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

Let’s continue with example_1 2. However, we are going to create deep copy using deepcopy() function present in copy 
module. The deep copy creates independent copy of original object and all its nested objects.

Example 5: Copying a list using deepcopy()
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
When we run the program, it will output:

Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
In the above program, we use deepcopy() function to create copy which looks similar.

However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the 
copy new_list.

Example 6: Adding a new nested object in the list using Deep copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
When we run the program, it will output:

Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
In the above program, when we assign a new value to old_list, we can see only the old_list is modified. 
This means, both the old_list and the new_list are independent. This is because the old_list was recursively 
copied, which is true for all its nested objects.
"""
