"""
Bubble Sort in Python

A Bubble sort is an easy algorithm among the various sorting algorithms. We learn it as a first sorting algorithm. It
is easy to learn and highly intuitive. It can be easy to implement into the code, which is much beneficial for
beginner software developers. But it is the worst algorithm for sorting the elements in every except because it
checks every time the array is sorted or not.

Let's understand the concepts of the bubble sort.

Concept of Bubble Sort

The bubble sort uses a straightforward logic that works by repeating swapping the adjacent elements if they are not
in the right order. It compares one pair at a time and swaps if the first element is greater than the second element;
otherwise, move further to the next pair of elements for comparison.

Let's understand it by an example -


Example -

We are creating a list of element, which stores the integer numbers

list1 = [5, 3, 8, 6, 7, 2]

Here the algorithm sort the elements -

First iteration

[5, 3, 8, 6, 7, 2]
It compares the first two elements and here 5>3 then swap with each other. Now we get new list is -

[3, 5, 8, 6, 7, 2]

In second comparison, 5 < 8 then swapping happen -


[3, 5, 8, 6, 7, 2]

In third comparison, 8>6 then swap -

[3, 5, 6, 8, 7, 2]

In fourth comparison, 8>7 then swap -

[3, 5, 6, 7, 8, 2]


In fifth comparison, 8>2 then swap-

[3, 5, 6, 7, 2, 8]

Here the first iteration is complete and we get the largest element at the end. Now we need to the len(list1) - 1


Second Iteration

[3, 5, 6, 7, 2, 8] - > [3, 5, 6, 7, 2, 8] here, 3<5 then no swap taken place

[3, 5, 6, 7, 2, 8] - > [3, 5, 6, 7, 2, 8] here, 5<6 then no swap taken place

[3, 5, 6, 7, 2, 8] - > [3, 5, 6, 7, 2, 8] here, 6<7 then no swap taken place

[3, 5, 6, 7, 2, 8] - > [3, 5, 6, 2, 7, 8] here 7>2 then swap their position. Now

[3, 5, 6, 2, 7, 8] - > [3, 5, 6, 2, 7, 8] here 7<8 then no swap taken place.

Third Iteration

[3, 5, 6, 2, 7, 8] - > [3, 5, 6, 7, 2, 8] here, 3<5 then no swap taken place

[3, 5, 6, 2, 7, 8] - > [3, 5, 6, 7, 2, 8] here, 5<6 then no swap taken place

[3, 5, 6, 2, 7, 8] - > [3, 5, 2, 6, 7, 8] here, 6<2 then swap their positions

[3, 5, 2, 6, 7, 8] - > [3, 5, 2, 6, 7, 8] here 6<7 then no swap taken place. Now

[3, 5, 2, 6, 7, 8] - > [3, 5, 2, 6, 7, 8] here 7<8 then swap their position.

It will iterate until the list is sorted.

Fourth Iteration -

[3, 5, 2, 6, 7, 8] - > [3, 5, 2, 6, 7, 8]

[3, 5, 2, 6, 7, 8] - > [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] - > [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] - > [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] - > [3, 2, 5, 6, 7, 8]

Fifth Iteration

[3, 2, 5, 6, 7, 8] - > [2, 3, 5, 6, 7, 8]
Check the each element and as we can see that our list is sorted using the bubble sort technique.

Implementation in Python Code
We have already described the technique of bubble sort. Now, we will implement the logic in the Python
code.
"""


# Creating a bubble sort function
def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list2 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list2)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list2))

"""
Output:


The unsorted list is:  [5, 3, 8, 6, 7, 2]
The sorted list is:  [2, 3, 5, 6, 7, 8]
Explanation:

In the above code, we have defined a bubble_sort() function which takes list1 as an argument.

Inside the function, we have defined two for loop - first for loop iterates the complete list and the second for loop 
    iterates the list and the compare the two elements in every outer loop iterations.
The for loop will be terminated when it reaches at the end.
We have defined the condition in the inner for loop; if a first index value is greater than the second index value, 
    swap their positions with each other.
We called the function and passed a list; it iterated and returned the sorted list.
Without using a temp variable
We can also swap the elements without using the temp variable. Python has a very unique syntax. We can use the 
    following lines of code.

Example -
"""


def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                # here we are not using temp variable
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


list2 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list2)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list2))

"""
Output:

The unsorted list is:  [5, 3, 8, 6, 7, 2]
The sorted list is:  [2, 3, 5, 6, 7, 8]
Optimization of Python Code Implementation
We can optimize the above code using the two techniques. The swaps are not done; it means list is sorted. In the 
    previous technique - The previous technique will evaluate the complete list though it doesn't seem necessary to do.

We can prevent the unnecessary evaluation using the Boolean flag and checks if any swaps were made in the 
    previous section.

Example -

"""


def bubble_sort(list1):
    # We can stop the iteration once the swap has done
    has_swapped = True

    while has_swapped:
        has_swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    return list1


list2 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list2)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list2))

"""
Output:

The unsorted list is:  [5, 3, 8, 6, 7, 2]
The sorted list is:  [2, 3, 5, 6, 7, 8]
In the second technique, we consider the fact that the iteration is ended when the largest element of the list end up 
    at the end of the list.

The first time, we pass the largest element at the end position using the n position. The second time, we pass through 
    the n-1 position, the second largest element.

In each consecutive iteration, we can compare at one less element than before. More accurately, in the k-th iteration, 
    only need to compare at the first n - k + 1 elements:

Example -
"""


def bubble_sort(list1):
    has_swapped = True

    total_iteration = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(list1) - total_iteration - 1):
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
        total_iteration += 1
    print("The number of iteration: ", total_iteration)
    return list1


list2 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list2)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list2))

"""
Output:

The unsorted list is:  [5, 3, 8, 6, 7, 2]
The number of iteration:  6
The sorted list is:  [2, 3, 5, 6, 7, 8]
Time Comparison
Let's see the time comparison between the above code snippets.

Unoptimized Bubble Sort Takes: 0.0106407  
Optimize Bubble Sort Takes: 0.0078251  
Bubble Sort with a Boolean flag and shortened list Takes: 0.0075207   
All techniques are useful for the fewer elements, but if the list consists of many elements, then the second optimize 
    technique make a huge difference.


Bubble Sort Complexity
Time               Complexity	 
Best	            O(n)
Worst	            O(n2)
Average	            O(n2)
Space Complexity	O(1)
Stability	Yes
Complexity in Detail
Bubble Sort compares the adjacent elements.

Cycle	Number of Comparisons
1st	    (n-1)
2nd	    (n-2)
3rd	    (n-3)
.......	......
last	1
Hence, the number of comparisons is

(n-1) + (n-2) + (n-3) +.....+ 1 = n(n-1)/2
nearly equals to n2

Hence, Complexity: O(n2)

Also, if we observe the code, bubble sort requires two loops. Hence, the complexity is n*n = n2

1. Time Complexities
Worst Case Complexity: O(n2)
If we want to sort in ascending order and the array is in descending order then the worst case occurs.
Best Case Complexity: O(n)
If the array is already sorted, then there is no need for sorting.
Average Case Complexity: O(n2)
It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
2. Space Complexity
Space complexity is O(1) because an extra variable is used for swapping.
In the optimized bubble sort algorithm, two extra variables are used. Hence, the space complexity will be O(2).
Bubble Sort Applications
Bubble sort is used if

complexity does not matter
short and simple code is preferred
"""