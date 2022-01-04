# P05. convert list/tuple/set to list/tuple/set

"""
1. CRUD       -->  Update
2. STATE      -->  integer
3. BEHAVIOR   -->  int  |   for  |  ==
"""

# 0. Mathematics
"""
list_1 =  [1, 2, 3]    --> set  --> {1,2,3}  --> tuple --> (1,2,3)
set_1 =   {1, 2, 3}    --> list --> [1,2,3]  --> tuple --> (1,2,3)
tuple_1 = (1,2,3)      --> list --> [1,2,3]  --> set   --> {1,2,3}
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")
list_1 = [1, 2, 3]
print("Given list :", list_1)
print('list to tuple :', tuple(list_1))
print('list to set :', set(list_1))
print()

tuple_1 = ('a', True, 1)
print("Given tuple :", tuple_1)
print("Tuple to list :", list(tuple_1))
print('tuple to set ', set(tuple_1))
print()

set_1 = {1, 'python', 1 + 1j, True}
print('Given set :', set_1)
print('set to list :', list(set_1))
print('set to tuple :', tuple(set_1))
print()

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")
# data = [1, 2, 3, 4, 5]
data = {1, 2, 3, 4, 'python'}


# data = {1, 'a', False}


def list_set_tuple_vise_versa(line):
    if type(line) is list:
        print("Given list :", line)
        print('list to tuple :', tuple(line))
        print('list to set :', set(line))

    elif type(line) is tuple:
        print("Given tuple :", line)
        print("Tuple to list :", list(line))
        print('tuple to set ', set(line))

    elif type(line) is set:
        print('Given set :', line)
        print('set to list :', list(line))
        print('set to tuple :', tuple(line))

    else:
        print("Given input is not list , tuple or set !")


list_set_tuple_vise_versa(data)

# 4 OOPS
print("--------4 Object Oriented        ----------")


class ListSetTuple:
    def __init__(self, line_1):
        self.line_1 = line_1

    def list_set_tuple(self):
        if type(self.line_1) is list:
            print("Given list :", self.line_1)
            print('list to tuple :', tuple(self.line_1))
            print('list to set :', set(self.line_1))

        elif type(self.line_1) is tuple:
            print("Given tuple :", self.line_1)
            print("Tuple to list :", list(self.line_1))
            print('tuple to set ', set(self.line_1))

        elif type(self.line_1) is set:
            print('Given set :', self.line_1)
            print('set to list :', list(self.line_1))
            print('set to tuple :', tuple(self.line_1))

        else:
            print("Given input is not list , tuple or set !")


lst = ListSetTuple([1, 2, 3, 4, 5])
lst.list_set_tuple()


# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
