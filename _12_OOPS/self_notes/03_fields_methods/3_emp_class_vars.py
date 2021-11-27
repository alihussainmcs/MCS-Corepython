print("...................Class without class variable .......................")


class Employee:
    # instance variables - each object has their own data
    # Here problem is comp name is sharable to all employees(objects)
    def __init__(self, eid, name, sal, comp):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.comp = comp

    def get_edata(self):
        print("Employee Info :", self.eid, self.name, self.sal, self.comp)


mic = Employee(2001, "Mic Herman", 18000, 'IBM')
mic.get_edata()

nic = Employee(2002, "Nic Baba", 18900, "IBM")
nic.get_edata()

print("................Class with class variable .....................")


class Employee:
    comp = "IBM"  # class variable, this is sharable to all objects

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_edata(self):
        #  print("Employee Details :", self.eid, self.name, self.sal, self.comp)
        print("Employee Info :", self.eid, self.name, self.sal, Employee.comp)  # This is correct way


ila = Employee(2003, "Ila H", 19000)
ila.get_edata()  # obj.methodname()  ==> Employee.get_edata(ali)
# Employee.get_edata(ila) same  output

iron = Employee(2004, "Iron M", 20000)
iron.get_edata()


print(".....................................")


class Student:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def avg(self):
        return (self.a + self.b) / 2


s1 = Student(10, 20)
print("Average is :", s1.avg())


print(".............................................")


class Student:
    name = 'Student'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls):
        return cls.name


print(Student.info())
