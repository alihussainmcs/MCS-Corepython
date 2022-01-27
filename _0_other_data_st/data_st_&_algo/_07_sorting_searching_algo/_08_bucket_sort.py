"""
Bucket Sort Algorithm

Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets. Each
bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm.

Finally, the sorted buckets are combined to form a final sorted array.

Scatter Gather Approach

The process of bucket sort can be understood as a scatter-gather approach. Here, elements are first scattered into
    buckets then the elements in each bucket are sorted. Finally, the elements are gathered in order.


Bucket Sort Algorithm
bucketSort()
  create N buckets each of which can hold a range of values
  for all the buckets
    initialize each bucket with 0 values
  for all the buckets
    put elements into buckets matching the range
  for all the buckets
    sort elements in each bucket
  gather elements from each bucket
end bucketSort

"""


# Bucket Sort in Python


def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array1 = [.42, .32, .33, .52, .37, .47, .51]

print('Given array : ', array1)
print("Sorted Array in descending order is")
print(bucketSort(array1))

"""
Bucket Sort Complexity
Time                Complexity	 
Best	            O(n+k)
Worst	            O(n2)
Average	            O(n)
Space Complexity	O(n+k)
Stability	Yes


Worst Case Complexity: O(n2)
When there are elements of close range in the array, they are likely to be placed in the same bucket. This may result 
    in some buckets having more number of elements than others.
It makes the complexity depend on the sorting algorithm used to sort the elements of the bucket.
The complexity becomes even worse when the elements are in reverse order. If insertion sort is used to sort elements 
    of the bucket, then the time complexity becomes O(n2).
    
    
Best Case Complexity: O(n+k)
It occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each 
    bucket.
The complexity becomes even better if the elements inside the buckets are already sorted.
If insertion sort is used to sort elements of a bucket then the overall complexity in the best case will be linear ie. 
    O(n+k). O(n) is the complexity for making the buckets and O(k) is the complexity for sorting the elements of the 
        bucket using algorithms having linear time complexity at the best case.
        
        
Average Case Complexity: O(n)
It occurs when the elements are distributed randomly in the array. Even if the elements are not distributed uniformly, 
    bucket sort runs in linear time. It holds true until the sum of the squares of the bucket sizes is linear in the 
    total number of elements.
    
Bucket Sort Applications

Bucket sort is used when:
input is uniformly distributed over a range.
there are floating point values

"""