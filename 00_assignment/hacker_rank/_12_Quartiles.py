"""
Objective
In this challenge, we practice calculating quartiles.

Task
Given an array, arr, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third
quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

Example

arr = [9, 5, 7, 1, 3]
The sorted array is [1, 3, 5, 7, 9] which has an odd number of elements. The lower half consists of [1, 3], and its
median is 1+3/2 = 2. The middle element is 5 and represents the second quartile. The upper half is [5, 7] and its median
 is 5+7/2 = 6. Return [2, 5, 8].

arr = [1, 3, 5, 7]
The array is already sorted. The lower half is [1, 3] with a median = 1+3/2 = 2. The median of the entire array is
3+5/2 = 4, and of the upper half is 5+7/2 = 6. Return [2, 4, 6].



Function Description

Complete the quartiles function in the editor below.

quartiles has the following parameters:

int arr[n]: the values to segregate
Returns

int[3]: the medians of the left half of arr, arr in total, and the right half of arr.
Input Format
The first line contains an integer, n, the number of elements in arr.
The second line contains n space-separated integers, each an arr[i].

Constraints
5 <= n <= 50
0 < arr[i] <= 100, where arr[i] is the ith element of the array.
Sample Input

STDIN                   Function
-----                   --------
9                       arr[] size n = 9
3 7 8 5 12 14 21 13 18  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
Sample Output

6
12
16
Explanation
arrsorted = [3, 5, 7, 8, 12, 13, 14, 18, 21]. There is an odd number of elements, and the middle element, the median,
is 12.

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in
either half:

Lower half (L): 3, 5, 7, 8

Upper half (U): 13, 14, 18, 21

Now find the quartiles:

Q1 is the median(L). So, . Q1 = (5+7)/2 = 6
Q2 is the median(X). So, . Q2 = 12
Q3 is the median(U). So, . Q3 = (14+18)/2 = 16
"""

n = int(input())
numbers = sorted(list(map(int, input().split())))


def median(x):
    # Return the median of list x
    if len(x) % 2 != 0:
        return x[len(x) // 2]
    else:
        return 0.5 * (x[len(x) // 2 - 1] + x[len(x) // 2])


m = median(numbers)
q1 = median(list(filter(lambda x: x < m, numbers)))
q2 = m
q3 = median(list(filter(lambda x: x > m, numbers)))

print(int(q1))
print(int(q2))
print(int(q3))
