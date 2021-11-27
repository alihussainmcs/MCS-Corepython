class Employee:
    # STATE --> data members  *  logical
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical

    @staticmethod
    def get_details():
        print("Employee details")


# Employee.get_details()
obj = Employee(1001, 'Ali', 10000)  # data physical methods logical
obj.get_details()
'''
Class   - Variables - Logical    <===>  Methods  - Physical
Object  - Variables - Physical    <===>  Methods  - Logical

'''


class University:
    # State
    def __init__(self, u_id, u_name, u_loc):
        self.u_id = u_id
        self.u_name = u_name
        self.u_loc = u_loc

    # Behaviour

    def u_data(self):
        print("Instance method ..........")
        print("University Data :", self.u_id, self.u_name, self.u_loc)

    @staticmethod
    def dep_data():
        dep = 'Electronics'
        print("Static method ...........")
        print("Department :", dep)

    @classmethod
    def branch_data(cls, branch):

        print("Class method ..............")
        print("Branch :", branch)


u = University(123456, "FALTU", 'Faltupur')
u.u_data()
u.dep_data()
u.branch_data('CS')


print("....................................................................")


class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0


counter = Counter()


counter.increment()
counter.increment()
counter.increment()
print(counter.value())
print(".................")

counter = Counter()

counter.increment()
counter.increment()
counter.current = -999

print(counter.value())
