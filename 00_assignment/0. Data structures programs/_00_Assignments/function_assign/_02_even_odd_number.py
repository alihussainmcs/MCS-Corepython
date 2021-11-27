# P02. print even and odd numbers

"""
1. CRUD       -->  Retrieve
2. STATE      -->  integer
3. BEHAVIOR   -->  int  |   for  |  ==
"""

# 0. Mathematics
"""
list_1 = [1, 2, 3, 4, 5, 6]
          |  |  |  |  |  |
          o  e  o  e  o  e 
odd = o
even = e
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
list_1 = [1, 2, 3, 4, 5, 6]

for i in list_1:
    if i % 2 == 0:
        print(i, "is even ")
    else:
        print(i, "is odd ")

# 3 Using Functions
print("--------3 Using Functions        ----------")


def even_odd_fun(num_list):
    for k in num_list:
        if k % 2 == 0:
            print(k, "is even ")
        else:
            print(k, "is odd ")


even_odd_fun(list_1)

# 4 OOPS
print("--------4 Object Oriented        ----------")


class EvenOddClass:
    def __init__(self, list_v):
        self.list_v = list_v

    def even_odd_method(self):
        for j in self.list_v:
            if j % 2 == 0:
                print(j, "is even ")
            else:
                print(j, "is odd ")


even_odd_obj = EvenOddClass(list_1)
even_odd_obj.even_odd_method()

# 5 Exception handling
print("--------5 Exception handling     ----------")

try:
    list_1 = [1, 2, 3, 4, 5, 'MCS']

    for i in list_1:
        if i % 2 == 0:
            print(i, "is even ")
        else:
            print(i, "is odd ")

except TypeError as te:
    print(te)

# 6 File Handling
print("--------6 File Handling          ----------")
data = open("sample2.txt")
data_1 = data.readline().split(',')
list_2 = []
for i in data_1:
    list_2.append(int(i))

print(list_2)

for m in list_2:
    if m % 2 == 0:
        print(m, "is even ")
    else:
        print(m, "is odd ")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
