class Employee:
    pass


"""
converts as below
                        class Employee:
                            def __init__(self):
                                pass
"""
print("Employee class @ :", Employee)
obj = Employee()

print("Employee object @ :", obj)


# Default constructor


class Employee:

    def __init__(self):  # Default constructor
        pass  # to perform any generic action

    @staticmethod
    def get_edata(eid, sal):
        print("Employee Data :", eid, sal)


ali = Employee()
ali.get_edata(101, 10000)  # Employee.get_edata(ali,101,10000)

# while defining class, default constructor is not mandatory. Python give automatically

# Employee CRUD Operations

'''
REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details 
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike

4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb
'''

print("-----------Employee hike---------------")


class Employee:
    # State
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # behaviour
    def e_data(self):
        print("Employee data :", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''

    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if 0 <= exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif 2 <= exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif 3 <= exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


ali = Employee(101, 'ILA', 20000)
ali.e_data()
ali.update_emp_sal(3)
ali.update_emp_sal(-10)

'''
UI PAGE:
---------
eid   : 101
name  : ILA
exp   : -10 

# client validations 
# server validations
'''

print("........................................................")


class DemoClass:
    num = 101

    # non-parameterized constructor
    def __init__(self):
        self.num = 999

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()

print("................................................")


class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()

print("The number of students:", Student.count)

print(".....................................")


class Student:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    @staticmethod
    def show(name):
        print("Hello", name)


student = Student()
student.show("Ali")

print("............ Default Constructor ................")


class Student:
    roll_num = 101
    name = "Ali"

    def display(self):
        print(self.roll_num, self.name)


st = Student()
st.display()
