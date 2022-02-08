class Company:
    # State
    def __init__(self, c_name, c_id, c_add):
        self.c_name = c_name
        self.c_id = c_id
        self.c_add = c_add
    # Behaviour

    def Comp_det(self):
        print("Company Details :", self.c_name, self.c_id, self.c_add)


comp = Company("MCS", "0001", 'Hyderabad')
comp.Comp_det()


comp1 = Company("Google", "0143", 'Bangalore')
comp1.Comp_det()
