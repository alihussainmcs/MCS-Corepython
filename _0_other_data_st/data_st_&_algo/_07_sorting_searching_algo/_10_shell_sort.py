"""
Shell Sort Algorithm

Shell sort is a generalized version of the insertion sort algorithm. It first sorts elements that are far apart from
    each other and successively reduces the interval between the elements to be sorted.

The interval between the elements is reduced based on the sequence used. Some of the optimal sequences that can be used
    in the shell sort algorithm are:

Shell's original sequence: N/2 , N/4 , …, 1
Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....

Note: The performance of the shell sort depends on the type of sequence used for a given input array.


Shell Sort Algorithm
shellSort(array, size)
  for interval i <- size/2n down to 1
    for each interval "i" in array
        sort all the elements at interval "i"
end shellSort

"""

# Shell sort in python


def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 1]

print('Given data : ', data)
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)


"""
Shell Sort Complexity
Time                Complexity	 
Best	            O(nlog n)
Worst	            O(n2)
Average	            O(nlog n)
Space Complexity	O(1)
Stability	No
Shell sort is an unstable sorting algorithm because this algorithm does not examine the elements lying in between the 
    intervals.

Time Complexity
Worst Case Complexity: less than or equal to O(n2)
Worst case complexity for shell sort is always less than or equal to O(n2).

According to Poonen Theorem, worst case complexity for shell sort is Θ(Nlog N)2/(log log N)2) or Θ(Nlog N)2/log log N) 
    or Θ(N(log N)2) or something in between.
Best Case Complexity: O(n*log n)
When the array is already sorted, the total number of comparisons for each interval (or increment) is equal to the size 
    of the array.
Average Case Complexity: O(n*log n)
It is around O(n1.25).
The complexity depends on the interval chosen. The above complexities differ for different increment sequences chosen. 
    Best increment sequence is unknown.

Space Complexity:

The space complexity for shell sort is O(1).

Shell Sort Applications
Shell sort is used when:

calling a stack is overhead. uClibc library uses this sort.
recursion exceeds a limit. bzip2 compressor uses it.
Insertion sort does not perform well when the close elements are far apart. Shell sort helps in reducing the distance 
    between the close elements. Thus, there will be less number of swapping to be performed.
"""