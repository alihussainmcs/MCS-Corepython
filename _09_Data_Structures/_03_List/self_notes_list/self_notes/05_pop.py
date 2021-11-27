"""
 5. pop
     list.pop(obj=list[-1]) Removes and returns last object or obj from list

"""
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before pop   : ", list1)

list1.pop(3)  # index
print("After  pop(3)   : ", list1)  # [23, 12, 46, 14, 7, 2, 19, 25]

list1.pop()
print("After  pop()   : ", list1)  # [23, 12, 46, 14, 7, 2, 19]

rem_ele = list1.pop(0)

print("Popped element : ", rem_ele)
print("After  pop   : ", list1)
