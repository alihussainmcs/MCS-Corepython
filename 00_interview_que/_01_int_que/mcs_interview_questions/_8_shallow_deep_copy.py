"""
8. shallow and deep copy?

Shallow Copy:

A shallow copy is a copy of an object that stores the reference of the original elements.
It creates the new collection object and then occupying it with reference to the child objects
found in the original.

It makes copies of the nested objects' reference and doesn't create a copy of the nested objects.
So if we make any changes to the copy of the object will reflect in the original object.

A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of
nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

Example : Create a copy using shallow copy

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)#Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("New list:", new_list)#New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Deep Copy

A deep copy is a process where we create a new object and add copy elements recursively. We will
use the deepcopy() method which present in copy module. The independent copy is created of original
object and its entire object.

A deep copy creates a new object and recursively adds the copies of nested objects present in the
original elements.The deep copy creates independent copy of original object and all its nested objects.

#example:

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)#Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print("New list:", new_list)#New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]



Shallow Copy	                                                Deep Copy


Shallow Copy stores the references of objects
to the original memory address.   	                        Deep copy stores copies of the object’s value.


Shallow Copy reflects changes made to the
new/copied object in the original object.	                Deep copy does’t reflect changes made to the
                                                            new/copied object in the original object.

Shallow Copy stores the copy of the original
object and points the references to the objects.	        Deep copy stores the copy of the original
                                                            object and recursively copies the objects as well.

Shallow copy is faster.                                    	Deep copy is comparatively slower.


#example:


import copy
a = [1,2,3,4,5,[1,2,3,4,5,6,7]]
b = a
shallow = copy.copy(a)
deep = copy.deepcopy(a)
a.append(10)
print('a:',a, end = '\n')
print('shallow: ',shallow,  end = '\n')
print('deep: ', deep)

output:

#a: [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7], 10]
#shallow:  [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7]]
#deep:  [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7]]

when we modify nested object, changes will get reflect in shallow copy but not in deep copy.

a = [1,2,3,4,5,[1,2,3,4,5,6,7]]
b = a
shallow = copy.copy(a)
deep = copy.deepcopy(a)
a[5].append(23)
print('a:',a, end = '\n')
print('shallow: ',shallow,  end = '\n')
print('deep: ', deep)

output:

#a: [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7, 23]]
#shallow:  [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7, 23]]
#deep:  [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6, 7]]


A shallow copy constructs a new compound object and then (to the extent possible) inserts *the
same objects* into it that the original contains.

A deep copy constructs a new compound object and then, recursively, inserts *copies* into it of
the objects found in the original.

"""
