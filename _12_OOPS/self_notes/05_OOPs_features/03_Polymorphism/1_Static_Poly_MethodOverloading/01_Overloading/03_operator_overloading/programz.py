# https://www.programiz.com/python-programming/operator-overloading
# https://www.geeksforgeeks.org/operator-overloading-in-python/

# Python program to show use of  + operator for different purposes.

print(1 + 2)  # 1.__add__(2)  obj.method(arg)

print("Python" + "For")  # "Python".__add__("For")

print(3 * 4)  # 3.__mul__(4)

print("Python" * 4)  # "Python".__mul__(4)

p = int(10)
x = 10

# x.__add__()
y = 20
print(x + y)  # x.__add__(y)
print(10 == 20)  # 10.__eq__(20)

'''
class Employee(object):
    def __init__(self,sal):
        self.sal = sal

ali = Employee(1000)
hulk = Employee(2000)
print(ali+hulk) # ali.__add__(hulk)
'''


# With Operator overloading with +
class Employee:
    def __init__(self, sal):
        self.sal = sal

    # adding two objects
    def __add__(self, obj):
        return self.sal + obj.sal  # ==> 1000 + 2000  ==> 1000.__add__(2000)


ali = Employee(1000)
hussain = Employee(2000)
print("Adding 2 emp objects ", ali + hussain)  # ali.__add__(hussain)


# With Operator overloading with gt >=


class Student(object):

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, obj):
        if self.marks >= obj.marks:  # 25 > 32 ==>25.__gt__(32)
            return True
        else:
            return False


ali = Student(25)
ila = Student(32)
if ali > ila:  # ali.__gt__(ila)
    print("ali got marks greater than ila")
else:
    print("ila got marks greater than ali")

list1 = list([1, 23])

x = 10
print(x)  # x.__str__()


class Employee:  # class Employee(object)

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal


ali = Employee(10, 'aliH', 10000)
print(ali)  # ==> ali.__str__() # It will give only address of variable


class Employee(object):

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def get_emp_details(self):
        print("Employee Details are : ", self.id, self.name, self.sal)

    def __str__(self):  # Method overriding
        obj = str(self.id) + " || " + self.name + " || " + str(self.sal)
        return obj


ali = Employee(100, 'AliH', 4000)
print("Ali object address :", ali)  # ali.__str__()

li = [1, 2, 3, 4]
print(li)  # li.__str__()

# ali.get_emp_details()

print("----------------------------------")
# ali.__getattribute__()
print("ali hash val ", ali.__hash__())
print("ali obj :", ali)  # ali.__str__()

'''
str vs repr
init vs new
object class in detail


'''

list_1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list_1 + list2)  # list_1.__add__(list2)
print(list_1 * 3)  # list_1.__mul__(3)

x = 10


# list_1.append()


class Employee(object):

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def __add__(self, other):
        return self.sal + other.sal


ali = Employee(100, 'AliH', 15000)
hussain = Employee(102, "Hussain", 20000)
print(ali + hussain)  # ali.__add__(hussain)
