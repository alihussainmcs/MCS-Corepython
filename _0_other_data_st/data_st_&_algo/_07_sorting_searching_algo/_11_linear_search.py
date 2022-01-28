"""
What is a linear search algorithm?
In the linear search algorithm, we start from the index 0 of a list and check if the element is present at the index or
    not. If the element is present at the index, we return the index as output. Otherwise, we move to the next index
    until we find the element that is being searched or we reach the end of the list.

For example, Suppose that we are given a list myList= [1,23,45,23,34,56,12,45,67,24] .



Now, we want to search the index of the element 12. For this, we will start from index 0 and check  if 12 is present
    there or not. If yes, we will return 0 as result or we will move to index 1. We will keep moving in this way to
    index 6 where 12 is present. After checking that 12 is present at index 6, we will return 6 as an output.
    If any element is not present, we will return -1 which will specify that the element is not present in the list.

Having an overview of the linear search operation, let us define an algorithm for the linear search operation.

Algorithm for linear search
The algorithm for linear search can be specified as follows.

Input to algorithm: A list and an element to be searched.

Output: Index of the element if the element is present. Otherwise,-1.

1. Start from index 0 of the list.
2. Check if the element is present at the current position.
3. If yes, return the current index. Goto 8.
4. Check if the current element is the last element of the list.
5. If yes, return -1. Goto 8. Otherwise, goto 6.
6. Move to the next index of the list.
7. Goto 2.
8. Stop.


Linear Search Algorithm
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index


"""


def LinearSearch(input_list, element: int):
    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i
    return -1


myList = [1, 23, 45, 23, 34, 56, 12, 45, 67, 24]
print("Given list is:", myList)
position = LinearSearch(myList, 12)
print("Element 12 is at position:", position)

"""
Drawbacks of linear search algorithm
A linear search algorithm is very costly in terms of time complexity. It has O(n) complexity in the worst case where n 
    is the number of elements in the list.


Another drawback is that it does’t consider the arrangement of elements in the list. If the elements are arranged in 
    ascending order and we have to search for the largest element, it will always take a maximum number of steps to 
    produce a result.


Similarly, if an element is not present in the list, it will again take the maximum number of steps to produce the 
    result as it will traverse each element of the list. 
    
    
Linear Search Applications
For searching operations in smaller arrays (<100 items).

"""