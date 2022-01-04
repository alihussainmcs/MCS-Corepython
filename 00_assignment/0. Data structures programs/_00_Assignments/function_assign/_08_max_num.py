# P08. find the Max of three numbers
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =      |   if-elif-else
"""

# 0. Mathematics
"""
numbers = 10, 20, 30
max   --> 30
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")

num1 = 10
num2 = 20
num3 = 30

if num1 > num2 and num1 > num3:
    print("Max number num1:", num1)

elif num2 > num1 and num2 > num3:
    print("Max number num2:", num2)

else:
    print("Max number num3:", num3)

# 3 Using Functions
print("--------3 Using Functions        ----------")


def max_num(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print("Max number num_1:", num_1)

    elif num_2 > num_1 and num_2 > num_3:
        print("Max number num_2:", num_2)

    else:
        print("Max number num_3:", num_3)


max_num(40, 50, 60)
# 4 OOPS
print("--------4 Object Oriented        ----------")


class MaxNumber:
    def __init__(self, num__1, num__2, num__3):
        self.num__1 = num__1
        self.num__2 = num__2
        self.num__3 = num__3

    def max_number(self):
        if self.num__1 > self.num__2 and self.num__1 > self.num__3:
            print("Max number num__1:", self.num__1)

        elif self.num__2 > self.num__1 and self.num__2 > self.num__3:
            print("Max number num__2:", self.num__2)

        else:
            print("Max number num__3:", self.num__3)


mn = MaxNumber(70, 80, 90)
mn.max_number()
# 5 Exception handling
print("--------5 Exception handling     ----------")

try:
    class MaxNumber:
        def __init__(self, num__1, num__2, num__3):
            self.num__1 = num__1
            self.num__2 = num__2
            self.num__3 = num__3

        def max_number(self):
            if self.num__1 > self.num__2 and self.num__1 > self.num__3:
                print("Max number num__1:", self.num__1)

            elif self.num__2 > self.num__1 and self.num__2 > self.num__3:
                print("Max number num__2:", self.num__2)

            else:
                print("Max number num__3:", self.num__3)


    mn = MaxNumber(70, 'a', 90)
    mn.max_number()
except Exception as ex:
    print(ex)

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
