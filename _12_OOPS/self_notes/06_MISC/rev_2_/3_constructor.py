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
