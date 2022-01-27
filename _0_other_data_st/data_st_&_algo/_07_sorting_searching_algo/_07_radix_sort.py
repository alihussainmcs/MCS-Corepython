"""


Introduction to Radix Sort
The radix (or base) is the number of digits used to represent numbers in a positional numeral system. For the binary
    system, the radix is 2 (it uses only two digits - 0 and 1). For the decimal system, the radix is 10 (it uses ten
    digits to represent all numbers - from 0 to 9).

A positional numeral system is, in simple terms, a number writing system, where the weight (or the value) of a digit is
    determined by its position. For example, in the number 123, 1 has more value than 3 because it's in position that
    denotes hundreds, and the 2 is in the tens.

Radix Sort can be used to lexicographically sort many types of data - integers, words, emails, but is mainly used to
    sort collections of integers and strings (that are mapped to appropriate integer keys).

It's a non-comparative sorting algorithm, meaning that it doesn't sort a collection by comparing its individual elements
    , but rather uses the inherent nature of the data its sorting to sort faster - it sorts data based on their radix.

Comparative sorting algorithms have the best case time complexity of O(nlogn), which is comparatively worse to linear
    execution time (O(n+k)) of non-comparative algorithms.

For example, let n be the number of elements to be sorted, and k is the range of allowed element values.

Counting Sort (a popular non-comparative algorithm) has the complexity of O(n+k) when the k is in the range from 1..n.
    But, if elements range from 1..n², then the complexity rises to O(n²), which is worse than any comparative
    sorting algorithm.

Counting Sort has the potential to be significantly faster than other popular comparative algorithms, though, only if a
    certain condition was fulfilled.


The idea of the Radix Sort is to upgrade Counting Sort so that it maintains the linear time complexity even if the
    range of elements' values drastically exceeds the number of elements.

In fact, Radix Sort inherently uses Counting Sort as the main subroutine, with a few tweaks to overcome the issues that
    arise with an increased range of elements' values.

Counting Sort Algorithm
In order to get a grasp of Radix Sort, we'll have to delve into Counting Sort first, implement it and observe the
    downfall with an increased number of element values.

Why Use Counting Sort in the Radix Sort?
Counting sort is a stable, non-comparative sorting algorithm, and it is mainly used to sort integer arrays. All of
    these characteristics are important for its use in Radix Sort. You can use other algorithms as the subroutine, as
    long as they have these characteristics, though, Counting Sort is the most natural match up.

Radix Sort needs to maintain a relative order of elements with the same key values in the input array while sorting the
    same place value digits, therefore, our main subroutine by definition needs to be some sort of stable
    sorting algorithm:

stable sorting illustration
Non-comparative sorting algorithms generally have linear complexity, so they will have less impact on the complexity of
    the Radix Sort.

How Does the Counting Sort Work?
Let's take a look at an unsorted integer array, which we'll sort using Counting Sort:

I = [2, 2, 0, 6, 1, 9, 9, 7]
Counting Sort works by counting the number of elements, that fit a distinct key value, and then calculates the positions
    of each key.

First of all, we'll find the maximum element in the input array - max = 9.

Then, we'll create an auxiliary array with max+1 elements. This is the count array (C), which will be used to store the
    number of occurrences of each element in the input array.

Initially, all counts are initialized to 0:


     C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Count array
#indices: 0  1  2  3  4  5  6  7  8  9
Now, we need to go through the following steps:

1. Traverse the input array and increase the corresponding count for every element by 1

For example, if we come across an element with the value of 2 in the input array (I), we add 1 to the element with the
    index 2 in the count array:

    I = [2, 2, 0, 6, 1, 9, 9, 7] # The first element is 2
         ^

    C = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # We increase count of 2nd element by 1
#indices: 0  1  2  3  4  5  6  7  8  9
After this step, the count array will store the number of occurrences of each element in the input array:

     C = [1, 1, 2, 0, 0, 0, 1, 1, 0, 2]
#indices: 0  1  2  3  4  5  6  7  8  9

# Element 0 has 1 occurrence
# Element 1 has 1 occurrence
# Element 2 has 2 occurrences
# Element 3 has no occurrences...
2. For each element in the count array, sum up its value with the value of all its previous elements, and then store
    that value as the value of the current element:

     C = [1, 2, 4, 4, 4, 4, 5, 6, 6, 8]
#indices: 0  1  2  3  4  5  6  7  8  9
# Element  0 = 1
# Element  1 = 1 + 1
# Element  2 = 1 + 1 + 2
# Element  3 = 1 + 1 + 2 + 0
#...
This way, we are storing the cumulative sum of the elements of the count array, on each step.

3. Calculate element position based on the count array values

To store this sorted sequence, we'll need to create a new array. Let's call it the output array (O), and initialize it
    with k zeros, where k is the number of elements in the input array:

  O = [0, 0, 0, 0, 0, 0, 0, 0] // Initialized output array
#indices: 0  1  2  3  4  5  6  7
For each element I[i] (starting from the end) in the input array:

Find the index in the count array that is equal to the value of the current element I[i]
That's the element C[j] where j=I[i]
Subtract 1 from the value of the C[i]
Now we have newValue = C[i]-1
Store the I[i] to the O[newValue]
Update the C[i] with the newValue

In the end, the output array contains the sorted elements of the input array!

Radix Sort Algorithm
radixSort(array)
  d <- maximum number of digits in the largest element
  create d buckets of size 0-9
  for i <- 0 to d
    sort the elements according to ith place digits using countingSort

countingSort(array, d)
  max <- find largest element among dth place elements
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique digit in dth place of elements and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
"""


def countingSort(inputArray):
    # Find the maximum element in the inputArray
    maxEl = max(inputArray)

    countArrayLength = maxEl + 1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase
    # the corresponding count for every element by 1
    for el in inputArray:
        countArray[el] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i - 1]

        # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


inputArray1 = [2, 2, 0, 6, 1, 9, 9, 7]
print("Input array = ", inputArray1)

sortedArray = countingSort(inputArray1)
print("Counting sort result = ", sortedArray)

"""
Radix Sort Complexity
Time Complexity	 
Best	O(n+k)
Worst	O(n+k)
Average	O(n+k)
Space Complexity	O(max)
Stability	Yes
Since radix sort is a non-comparative algorithm, it has advantages over comparative sorting algorithms.

For the radix sort that uses counting sort as an intermediate stable sort, the time complexity is O(d(n+k)).


Here, d is the number cycle and O(n+k) is the time complexity of counting sort.

Thus, radix sort has linear time complexity which is better than O(nlog n) of comparative sorting algorithms.

If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in
    linear time however the intermediate sort takes large space.

This makes radix sort space inefficient. This is the reason why this sort is not used in software libraries.

Radix Sort Applications
Radix sort is implemented in

DC3 algorithm (Kärkkäinen-Sanders-Burkhardt) while making a suffix array.
places where there are numbers in large ranges.
"""