"""
 extend  : only sequence str,list,tuple
         : list1.extend(seq)         Appends the contents of seq to list

"""

list1 = [1, 2, 3, 4, 5, 6]

print("DEBUG : Before extend : ", list1)

# append([10,20,30]) :       ==> [1,2,3,4,5,6,[10,20,30]]

list1.extend([10, 20, 30])   # ==> [1,2,3,4,5,6,10,20,30]

print("DEBUG : After extend  : ", list1)

list1.extend('Hello World')

list1.extend((1, 2, 3))

list2 = [True, 10, 11.3, 'a', (10+12j)]
list1.extend(list2)

print("DEBUG : After extend  : ", list1)
