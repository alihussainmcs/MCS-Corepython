"""
Binary Search in Python

A binary search is an algorithm to find a particular element in the list. Suppose we have a list of thousand elements,
    and we need to get an index position of a particular element. We can find the element's index position very fast
    using the binary search algorithm.

There are many searching algorithms but the binary search is most popular among them.

The elements in the list must be sorted to apply the binary search algorithm. If elements are not sorted then sort
    them first.

Concept of Binary Search
In the binary search algorithm, we can find the element position using the following methods.

Recursive Method
Iterative Method


Recursive Method
The divide and conquer approach technique is followed by the recursive method. In this method, a function is called
    itself again and again until it found an element in the list.


Iterative Method
A set of statements is repeated multiple times to find an element's index position in the iterative method. The while
    loop is used for accomplish this task.

Binary search is more effective than the linear search because we don't need to search each list index. The list must
    be sorted to achieve the binary search algorithm.

Let's have a step by step implementation of binary search.

We have a sorted list of elements, and we are looking for the index position of 45.

[12, 24, 32, 39, 45, 50, 54]


So, we are setting two pointers in our list. One pointer is used to denote the smaller value called low and the second
    pointer is used to denote the highest value called high.

Next, we calculate the value of the middle element in the array.

mid = (low+high)/2
Here, the low is 0 and the high is 7.
mid = (0+7)/2
mid = 3 (Integer)
Now, we will compare the searched element to the mid index value. In this case, 32 is not equal to 45. So we need to
    do further comparison to find the element.

If the number we are searching equal to the mid. Then return mid otherwise move to the further comparison.

The number to be search is greater than the middle number, we compare the n with the middle element of the elements on
    the right side of mid and set low to low = mid + 1.

Otherwise, compare the n with the middle element of the elements on the left side of mid and set high to high = mid - 1.


"""


# Iterative Binary Search Function method Python Implementation
# It returns index of n in given list1 if present,
# else returns -1
def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    # mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list1
list2 = [12, 24, 32, 39, 45, 50, 54]
print('Given list :', list2)
n1 = 45
print('Element to search :', n1)
# Function call
result = binary_search(list2, n1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")

"""
Explanation:

In the above program -

We have created a function called binary_search() function which takes two arguments - a list to sorted and a number to 
    be searched.
We have declared two variables to store the lowest and highest values in the list. The low is assigned initial value to 
    0, high to len(list1) - 1 and mid as 0.
Next, we have declared the while loop with the condition that the lowest is equal and smaller than the highest The 
    while loop will iterate if the number has not been found yet.
In the while loop, we find the mid value and compare the index value to the number we are searching for.
If the value of the mid-index is smaller than n, we increase the mid value by 1 and assign it to The search moves to 
    the left side.
Otherwise, decrease the mid value and assign it to the high. The search moves to the right side.
If the n is equal to the mid value then return mid.
This will happen until the low is equal and smaller than the high.
If we reach at the end of the function, then the element is not present in the list. We return -1 to the calling 
    function.
Let's understand the recursive method of binary search.

Recursive Binary Search
The recursion method can be used in the binary search. In this, we will define a recursive function that keeps calling 
    itself until it meets the condition.

Let's understand the above program using the recursive function.
"""


# Python program for recursive binary search.
# Returns index position of n in list1 if present, otherwise -1
def binary_search(list1, low, high, n):
    # Check base case for the recursive function
    if low <= high:

        mid = (low + high) // 2

        # If element is available at the middle itself then return the its index
        if list1[mid] == n:
            return mid

            # If the element is smaller than mid value, then search moves
        # left sublist1
        elif list1[mid] > n:
            return binary_search(list1, low, mid - 1, n)

            # Else the search moves to the right sublist1
        else:
            return binary_search(list1, mid + 1, high, n)

    else:
        # Element is not available in the list1
        return -1

    # Test list1ay


list2 = [12, 24, 32, 39, 45, 50, 54]
n1 = 32
print()
print('Element to search :', n1)
# Function call
res = binary_search(list2, 0, len(list2) - 1, n1)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in list1")

"""
Explanation


The above program is similar to the previous program. We declared a recursive function and its base condition. The 
    condition is the lowest value is smaller or equal to the highest value.

We calculate the middle number as in the last program.
We have used the if statement to proceed with the binary search.
If the middle value equal to the number that we are looking for, the middle value is returned.
If the middle value is less than the value, we are looking then our recursive function binary_search() again and 
    increase the mid value by one and assign to low.
If the middle value is greater than the value we are looking then our recursive function binary_search() again and 
    decrease the mid value by one and assign it to low.
In the last part, we have written our main program. It is the same as the previous program, but the only difference is 
    that we have passed two parameters in the binary_search() function.

This is because we can't assign the initial values to the low, high and mid in the recursive function. Every time the
    recursive is called the value will be reset for those variables. That will give the wrong result.

Complexity

The complexity of the binary search algorithm is O(1) for the best case. This happen if the element that element we 
are looking find in the first comparison. The O(logn) is the worst and the average case complexity of the binary 
search. This depends upon the number of searches are conducted to find the element that we are looking for. """