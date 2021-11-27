print(".............For loop in range .........................")

'''
Range:   single value:  (end_val+1)                -  10     - 0,1,2,3..9
         two values  : (st_val, end_val+1)         - (1,21)  --> 1,2,3..20
         three values: (st_val, end_val+1, diff)   - (5,101,6) --> 5,11,17,23..
'''
# here range is special function
print("value of range(3) is ")

for i in range(3):
    print(i)

print("value of range(11) is ")

for i in range(11):
    print(i)

print("value of range(1, 11, 12) is ")
for i in range(1, 11, 2):
    print(i)

print("value of range(1, 21, 16) is ")
for i in range(1, 21, 6):
    print(i)

print("value of range(10, 1, -3) is ")
for i in range(10, 1, -3):
    print(i)

print("value of range(10, 1, -2) is ")
for i in range(10, 1, -2):
    print(i)
