"""
Sorting, although a basic operation, is one of the most important operations a computer should perform. It is a
building block in many other algorithms and procedures, such as searching and merging. Knowing different sorting
algorithms could help you better understand the ideas behind the different algorithms, as well as help you come up
with better algorithms.

The Selection Sort algorithm sorts an array by finding the minimum value of the unsorted part and then swapping it
with the first unsorted element. It is an in-place algorithm, meaning you won't need to allocate additional lists.
While slow, it is still used as the main sorting algorithm in systems where memory is limited.

Selection Sort

So how does the selection sort work? Selection sort breaks the input list in two parts, the sorted part which
initially is empty, and the unsorted part, which initially contains the list of all elements. The algorithm then
selects the minimum value of all the unsorted file and swaps it with the first unsorted value, and then increases the
sorted part by one.

A high level implementation of this sort would look something like this:


def selection_sort(L):
    for i in range(len(L) - 1):
        min_index = argmin(L[i:])
        L[i], L[min_index] = L[min_index], L[i]

In the above pseudocode, argmin() is a function that returns the index of the minimum value. The algorithm uses a
    variable i to keep track of where the sorted list ends and where the unsorted one begins. Since we start with no
    sorted items and take the minimum value, it will always be the case that every member of the unsorted part is
    greater than any member of the sorted part.

The first line increments the value of i, the second line finds the minimum value's index, and the third line swaps
    those values. Swapping works because Python calculated the right-hand side before assigning anything to the
    left-hand side, so we don't need any temporary variables.

Let's see how it works in action with a list that contains the following elements: [3, 5, 1, 2, 4].

We begin with the unsorted list:

3 5 1 2 4
The unsorted section has all the elements. We look through each item and determine that 1 is the smallest element. So,
    we swap 1 with 3:

1 5 3 2 4
Of the remaining unsorted elements, [5, 3, 2, 4], 2 is the lowest number. We now swap 2 with 5:

1 2 3 5 4
This process continues until the list is sorted:


1 2 3 5 4
1 2 3 4 5
1 2 3 4 5

Let's see how we can implement this in Python!

Implementation
The trick to implementing this algorithm is keeping track of the minimum value and swapping two elements of the list.
    Open a file named sort.py in your favorite editor and enter the following code in it:

"""


def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(L) - 1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]


# Now let's add some code to the file to test the algorithm:
L1 = [3, 1, 41, 59, 26, 53, 59]
print(L1)
selection_sort(L1)

# Let's see the list after we run the Selection Sort
print(L1)


"""
You can then open a terminal and run to see the results:


[3, 1, 41, 59, 26, 53, 59]
[1, 3, 26, 41, 53, 59, 59]


Selection Sort Complexity
Time Complexity	 
Best	O(n2)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	No
Cycle	Number of Comparison
1st	(n-1)
2nd	(n-2)
3rd	(n-3)
...	...
last	1
Number of comparisons: (n - 1) + (n - 2) + (n - 3) + ..... + 1 = n(n - 1) / 2 nearly equals to n2.

Complexity = O(n2)

Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity 
    is n*n = n2.

Time Complexities:

Worst Case Complexity: O(n2)
If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
Best Case Complexity: O(n2)
It occurs when the array is already sorted
Average Case Complexity: O(n2)
It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

The time complexity of the selection sort is the same in all cases. At every step, you have to find the minimum element 
    and put it in the right place. The minimum element is not known until the end of the array is not reached.

Space Complexity:

Space complexity is O(1) because an extra variable temp is used.

Selection Sort Applications
The selection sort is used when

a small list is to be sorted
cost of swapping does not matter
checking of all the elements is compulsory
cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of 
    bubble sort)

"""