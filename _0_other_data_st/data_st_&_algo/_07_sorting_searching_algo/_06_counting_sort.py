"""
Counting Sort Algorithm

Counting sort is a sorting algorithm used to sort elements of an array in linear time. We usually use Counting Sort to
    sort integer arrays.

Counting Sort a stable, non-comparative algorithm.

Non-comparative sorting algorithms perform sorting without any comparison between elements to be sorted.

Stable sorting algorithms preserve the relative order of elements with the same value in the sorted array. That means
    that the relative order of two same-value elements in the original array will be the same as their relative order
    in the sorted array.

Stable sorting
Counting sort is not an in-place algorithm, it uses an auxiliary array to sort elements of an input array.

Let's first take an intuitive look at how the algorithm works.

Assume that we have the array I = [2, 2, 0, 6, 1, 9, 9, 7] and we want to sort it. We'll call the array I the
    input array.

Counting Sort works by counting the number of elements, that fit a distinct key value, and then calculates the
    positions of each key.

First of all, we need to find the element with the highest value, we'll call it the maximum element - maxElement = 9.

Then, we'll create an auxiliary array with maxElement+1 elements, called the count array (C). We'll use it to store the
    number of occurrences of each individual element in the input array I. Therefore, all counts should be initialized
    to 0:

	   C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Count array
 # indices: 0  1  2  3  4  5  6  7  8  9
Now, we need to go through the following steps:

1. Go over each element of the input array and increase its corresponding count by 1

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
2. For each element in the count array, sum up its value with the value of all its previous elements, and store that
    value as the value of the current element:

     C = [1, 2, 4, 4, 4, 4, 5, 6, 6, 8]
#indices: 0  1  2  3  4  5  6  7  8  9
# Element  0 = 1
# Element  1 = 1 + 1
# Element  2 = 1 + 1 + 2
# Element  3 = 1 + 1 + 2 + 0
#...
This way, we are storing the cumulative sum of the elements of the count array, on each step.

3. Calculate element position based on the count array values:

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


Counting Sort Algorithm
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1

"""


# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

"""
Complexity
Time                Complexity	 
Best	            O(n+k)
Worst	            O(n+k)
Average	            O(n+k)
Space Complexity	O(max)
Stability	Yes
Time Complexities

There are mainly four main loops. (Finding the greatest value can be done outside the function.)

for-loop	time of counting
1st	        O(max)
2nd	        O(size)
3rd	        O(max)
4th	        O(size)
Overall complexity = O(max)+O(size)+O(max)+O(size) = O(max+size)

Worst Case Complexity:      O(n+k)
Best Case Complexity:       O(n+k)
Average Case Complexity:    O(n+k)
In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the 
    algorithm goes through n+k times.


There is no comparison between any elements, so it is better than comparison based sorting techniques. But, it is bad 
    if the integers are very large because the array of that size should be made.

Space Complexity

The space complexity of Counting Sort is O(max). Larger the range of elements, larger is the space complexity.

Counting Sort Applications
Counting sort is used when:

there are smaller integers with multiple counts.
linear complexity is the need.
"""
