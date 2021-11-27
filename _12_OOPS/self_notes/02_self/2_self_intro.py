print("Hello World")
x = 10  # int(10) --> Int(10)
print(x)
print(x, type(x))
list1 = [1, 2, 3]
print("List data : ", list1)
print(" Type : ", type(list1))


def get():
    print("Function get()")
    # ....


print("Function name :", get)  # Function name    x = 10   get = <func addr>
get()  # Function call

# print("Employee address : ",Employee)


'''
Here python will load the class Employee and provides memory for class body'''


class Employee:
    def __init__(self, eid, name, sal, adddr):
        print("Self address  ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
        self.adddr = adddr

    def get_e_info(self):
        print("Employee details are : ", self.eid, self.name, self.sal, self.adddr)


print("Employee address : ", Employee)

ali = Employee(101, 'Ali Hussain', 10000, {'hno': 67, 'area': 'BLR'})  # object creation
ali.get_e_info()

'''
Step1 : 2 parts : 
             I. Employee  
            II. (100, 'Ali Hussain', 10000)
Step2 : Python will check and find the address of Employee
Step3 : First python creates empty object of Employee class
        Employee class __init__ method will be called, passes 
                1. Address of empty object to self parameter         ==> self
                2. the tuple of arguments will be passed to remaining parameters  ==> (eid, name, sal) 
Step4 : Data passes to local variables (eid, name, sal)               
Step5 : self.eid = eid 
        LHS eid = instance variable
        RHS eid = local variable 
        ==> Local variable eid data,we are setting to instance variable 

        self.name = 'Ali Hussain'
        self.sal = '10000'

        - Empty object will be created by python and gives to self
        - __init__ method helps to initialize the STATE of object(instance)


'''

print("Ali object : ", ali)
ali.get_e_info()

# string list tuple dictionary set
msg = 'Hello world'  # STATE
msg.capitalize()  # BEHAVIOR
lst1 = [1, 2, 3, 4, 5, 10]  # STATE

# STATE
item_id = 1001
ch_name = 'Chocolate'
price = 15


def get_final_price(c_price):
    if c_price <= 5:
        disc = 5 * 10 / 100
        final_price = c_price - disc
        print("Final price : ", final_price)
    elif 5 <= c_price <= 10:
        print("10")


get_final_price(4)

print("...........................................................................")


# It is clearly seen that self and obj is referring to the same object

class Check:
    def __init__(self):
        print("Address of self = ", id(self))


obj = Check()
print("Address of class object = ", id(obj))

print("..........................................................................")


class Car:

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


# both objects have different self which
# contain their attributes
audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)


print(".............................")


# Self is always required as the first argument
class Check:
    def __init__(self):
        print("This is Constructor")


obj = Check()
print("Worked fine")

print(".........................................")


class ThisIsClass:
    def __init__(in_place_of_self):
        print("we have used another "
              "parameter name in place of self")


ob = ThisIsClass()
