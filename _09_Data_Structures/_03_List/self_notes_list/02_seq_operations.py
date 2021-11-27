list1 = [1, 2, 5, 6, 8, 9, 1]
print("List1 is : ", list1)

# 1. Sequence operations

print("----------1. Indexing-------------")

'''                                                                     
      [1, 2, 5, 6, 8, 9, 1]   1 2 3 4 5 6 7 8 9 10 
       0  1  2  3  4  5  6    
'''
print("list1 [1]    : ", list1[1])

print("list1 [5] list1 [6] list[-1] : ", list1[5], list1[6], list1[-1])

print("----------2. Slicing-------------")

print("Slicing operation list1[2:] : ", list1[2:])
print("Slicing operation list1[2:5] : ", list1[2:5])
print("Slicing operation list1[:5] : ", list1[:5])
print("Slicing operation list1[::1] : ", list1[::1])
print("Slicing operation list1[::2] : ", list1[::2])

print("----------3. Adding-------------")

print("Adding 2 lists   [1, 2, 3] + [4, 5, 6] :", [1, 2, 3] + [4, 5, 6])  # print(10+20)

print("Adding 2 lists   [1, 2, 3] + ['a', 5, True] :", [1, 2, 3] + ['a', 5, True])  # print(10+20)

print("Adding 2 lists   [(10, 20, 30), 2, 3] + ['a', 5, True] :", [(10, 20, 30), 2, 3] + ['a', 5, True])  # print(10+20)

list1 = [10, 20, 30]

list2 = [11, 12, 13]

print("Adding 2 lists (list1 = [10, 20, 30], list2 = [11, 12, 13] ) is :", list1+list2)   # x=10 y= 20   print(x+y)

print("----------4. Multiplying-------------")

print("Multiply 2 lists [1, 2, 3] * 2 :", [1, 2, 3] * 2)

print("Multiply 2 lists ['a', 2, False] * 2 :", ['a', 2, False] * 2)


print("----------5. Membership-------------")

print("Check value membership 1 in [1, 2, 3] : ", 1 in [1, 2, 3])

print("Check value membership True in [True, 2, 3]: ", True in [True, 2, 3])

print("Check value membership 'a' in [1, 2, 's'] : ", 'a' in [1, 2, 's'])



print("----------6. length-------------")

print("Length of list1 : ", len(list1))



print("----------7. max-------------")
print("Length of list1 : ", max(list1))

print("----------8. min-------------")
print("Length of list1 : ", min(list1))

