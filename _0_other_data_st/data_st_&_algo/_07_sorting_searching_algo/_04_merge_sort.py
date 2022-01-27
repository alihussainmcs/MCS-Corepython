"""
Merge Sort in Python

Merge sort is similar to the quick sort algorithm as works on the concept of divide and conquer. It is one of the most
    popular and efficient sorting algorithm. It is the best example for divide and conquer category of algorithms.

It divides the given list in the two halves, calls itself for the two halves and then merges the two sorted halves. We
    define the merge() function used to merging two halves.

The sub lists are divided again and again into halves until we get the only one element each. Then we combine the pair
    of one element lists into two element lists, sorting them in the process. The sorted two element pairs is merged
    into the four element lists, and so on until we get the sorted list.

Merge Sort Concept
Let's see the following Merge sort diagram.

We have divided the given list in the two halves. The list couldn't be divided in equal parts it doesn't matter at all.

Merge sort can be implement using the two ways - top-down approach and bottom-up approach.

The bottom-up approach provides the more optimization which we will define later.

The main part of the algorithm is that how we combine the two sorted sublists. Let's merge the two sorted merge list.

A : [2, 4, 7, 8]
B : [1, 3, 11]
sorted : empty
First, we observe the first element of both lists. We find the B's first element is smaller, so we add this in our
    sorted list and move forward in the B list.

A : [2, 4, 7, 8]
B : [1, 3, 11]
Sorted : 1
Now we look at the next pair of elements 2 and 3. 2 is smaller so we add it into our sorted list and move forward to
    the list.

A : [2, 4, 7, 8]
B : [1, 3, 11]
Sorted : 1
Continue this process and we end up with the sorted list of {1, 2, 3, 4, 7, 8, 11}. There can be two special cases.

What if both sublists have same elements - In such case, we can move either one sublist and add the element to the
    sorted list. Technically, we can move forward in both sublist and add the elements to the sorted list.
We have no element left in one sublist. When we run out the in a sublist simply add the element of the second one after
    the other.
We should remember that we can sort the element in the any order. We sort the given list in ascending order but we can
    easily sort in descending order.


Implementation
The merge sort algorithm is implemented by suing the top-down approach. It can be look slightly difficult, so we will
    elaborate each step in details. Here, we will implement this algorithm on two types of collections - integer
    element's list (typically used to introduce sorting) and a custom objects (a more practical and realistic scenario).

Sorting Array
The main concept of algorithm is to divide (sub)list into halves and sort them recursively. We continue the process
    until we end up lists that have only one element. Let's understand the following function for division -

def merge_sort(array, left_index, right_index):
       if left_index >= right_index:
                 return middle = (left_index + right_index)//2
       merge_sort(array, left_index, middle)
       merge_sort(array, middle + 1, right_index)
       merge(array, left_index, right_index, middle)
Our primary focus to divide the list into subparts before the sorting happen. We need to get the integer value so we
    use the // operator for our indices.

Let's understand the above procedure by following steps.

First step is to create copies of lists. The first list contains the lists from [left_index,...,middle] and the second
    from [middle+1,?,right_index].
We traverse both copies of list by using the pointer, select the smaller value of the two values and add them to the
    sorted list. Once we add the element to the list and we move forward in the sorted list regardless.
Add the remaining elements in the other copy to the sorted array.
Let's implement the merge sort in Python program

"""


# function to divide the lists in the two sublists
def merge_sort(list1, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(list1, left_index, middle)
    merge_sort(list1, middle + 1, right_index)
    merge1(list1, left_index, right_index, middle)

    # Defining a function for merge the list


def merge1(list1, left_index, right_index, middle):
    # Creating subparts of a lists
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle + 1:right_index + 1]

    # Initial values for variables that we use to keep
    # track of where we are in each list1
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    # traverse both copies until we get run out one element
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):

        # If our left_sublist has the smaller element, put it in the sorted
        # part and then move forward in left_sublist (by increasing the pointer)
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
            # Otherwise add it into the right sublist
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1

            # move forward in the sorted part
        sorted_index = sorted_index + 1

        # we will go through the remaining elements and add them
    while left_sublist_index < len(left_sublist):
        list1[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        list1[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1


list2 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
print("Given  list :", list2)
merge_sort(list2, 0, len(list2) - 1)
print('Sorted list :', list2)

print('-------------------------------------- merge sort by class  ----------------------------------------------')
"""
Sorting Custom Objects
We can also sort the custom objects by using the Python class. This algorithm is almost similar to the above but we 
    need to make it more versatile and pass the comparison function.

We will create a custom class, Car and add a few fields to it. We make few changes in the below algorithm to make it 
    more versatile. We can do this by using the lambda functions.


Let's understand the following example.

"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return str.format("Make: {}, Model: {}, Year: {}", self.make, self.model, self.year)


def merge(list1, l1, r, m, comp_fun):
    left_copy = list1[l1:m + 1]
    r_sublist = list1[m + 1:r + 1]

    left_copy_index = 0
    r_sublist_index = 0
    sorted_index = l1

    while left_copy_index < len(left_copy) and r_sublist_index < len(r_sublist):

        # We use the comp_fun instead of a simple comparison operator
        if comp_fun(left_copy[left_copy_index], r_sublist[r_sublist_index]):
            list1[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            list1[sorted_index] = r_sublist[r_sublist_index]
            r_sublist_index = r_sublist_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        list1[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while r_sublist_index < len(r_sublist):
        list1[sorted_index] = r_sublist[r_sublist_index]
        r_sublist_index = r_sublist_index + 1
        sorted_index = sorted_index + 1


def merge_sort(list1, l2, r, comp_fun):
    if l2 >= r:
        return

    m = (l2 + r) // 2
    merge_sort(list1, l2, m, comp_fun)
    merge_sort(list1, m + 1, r, comp_fun)
    merge(list1, l2, r, m, comp_fun)


car1 = Car("Renault", "33 Duster", 2001)
car2 = Car("Maruti", "Maruti Suzuki Dzire", 2015)
car3 = Car("Tata motor", "Jaguar", 2004)
car4 = Car("Cadillac", "Seville Sedan", 1995)

list2 = [car1, car2, car3, car4]

merge_sort(list2, 0, len(list2) - 1, lambda carA, carB: carA.year < carB.year)

print("Cars sorted by year:")
for car in list2:
    print(car)

print()
merge_sort(list2, 0, len(list2) - 1, lambda carA, carB: carA.make < carB.make)
print("Cars sorted by make:")
for car in list2:
    print(car)


"""
Merge Sort Complexity
Time                Complexity	 
Best	            O(n*log n)
Worst	            O(n*log n)
Average	            O(n*log n)
Space Complexity	O(n)
Stability	Yes

Time Complexity
Best Case Complexity:       O(n*log n)

Worst Case Complexity:      O(n*log n)

Average Case Complexity:    O(n*log n)

Space Complexity
The space complexity of merge sort is O(n).

Merge Sort Applications

Inversion count problem
External sorting
E-commerce applications
"""