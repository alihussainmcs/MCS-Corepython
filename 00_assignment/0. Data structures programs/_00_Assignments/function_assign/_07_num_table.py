# P07. table of the given number
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =      |   for
"""

# 0. Mathematics
"""
num = 5
table --> 5 10 15 20 25 30 35 40 45 50
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")


# 2. Algorithm

print("--------2 Algorithm              ----------")
num = 5
print("Given number :", num)
print("Table")
for i in range(1, 11):
    print(i, " X ", num, ':', i*num)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def table(num_1):
    print("Given number :", num_1)
    print("Table")
    for i in range(1, 11):
        print(i, " X ", num_1, ':', i * num_1)


table(6)
# 4 OOPS
print("--------4 Object Oriented        ----------")


class Table:
    def __init__(self, num_2):
        self.num_2 = num_2

    def table_method(self):
        print("Given number :", self.num_2)
        print("Table")
        for i in range(1, 11):
            print(i, " X ", self.num_2, ':', i * self.num_2)


t = Table(10)
t.table_method()

# 5 Exception handling
print("--------5 Exception handling     ----------")
try:
    class Table:
        def __init__(self, num_2):
            self.num_2 = num_2

        def table_method(self):
            print("Given number :", self.num_2)
            print("Table")
            for i in range(1, 11):
                print(i, " X ", self.num_2, ':', i * self.num_2)


    t = Table(10+'a')
    t.table_method()
except TypeError as te:
    print("Exception part ! ", te)


# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
