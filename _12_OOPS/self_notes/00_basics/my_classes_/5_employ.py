class Employee:
    # State
    def __init__(self, e_name, e_id, e_sal):
        self.e_name = e_name
        self.e_id = e_id
        self.e_sal = e_sal

    # Behaviour
    def emp(self):
        print("Employee detail :", self.e_name, self.e_id, self.e_sal)


empl_1 = Employee("Abc", 101, 29000)
empl_1.emp()
