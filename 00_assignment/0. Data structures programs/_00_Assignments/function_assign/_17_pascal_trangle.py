# P17. REQ :  print given Pascal's triangle
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""
Pascal triangle is an exciting concept of mathematics where a triangular array is formed by summing adjacent elements 
in the preceding row. In simple words, every number is generated by taking up the sum of the adjacent row, and the 
outside edges of a triangle are always 1. It is named after the famous French mathematician Blaise Pascal. Below is 
the representation of the Pascal triangle.
                             1
                              
                          1     1
                          
                      1      2     1
                      
                  1     3     3     1
                  
               1     4     6     4     1
               
            1    5    10    10     5     1
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
# input n
n = 5

# iterate up to n
for i in range(n):
    # adjust space
    print(' ' * (n - i), end='')

    # compute power of 11
    print(' '.join(map(str, str(11 ** i))))

print("Second method ")

num = 6
list1 = []  # an empty list
for i in range(num):
    list1.append([])
    list1[i].append(1)
    for j in range(1, i):
        list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
    if (num != 0):
        list1[i].append(1)
for i in range(num):
    print(" " * (num - i), end=" ", sep=" ")
    for j in range(0, i + 1):
        print('{0:6}'.format(list1[i][j]), end=" ", sep=" ")
    print()
# 3 Using Functions
print("--------3 Using Functions        ----------")


def pascal_triangle(n_1):
    # iterate up to n
    for j in range(n_1):
        # adjust space
        print(' ' * (n_1 - j), end='')

        # compute power of 11
        print(' '.join(map(str, str(11 ** j))))


pascal_triangle(7)
# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
