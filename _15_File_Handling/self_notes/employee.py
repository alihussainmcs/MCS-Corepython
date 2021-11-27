class Employee:
    def __init__(self, e_id, e_name, e_sal):
        self.e_id = e_id
        self.e_name = e_name
        self.e_sal = e_sal

    def emp_data(self):
        print('Employee :', self.e_id, self.e_name, self.e_sal)
