class Company:
    # State
    def __init__(self, c_name, c_id, c_add):
        self.c_name = c_name
        self.c_id = c_id
        self.c_add = c_add
    # Behaviour

    def Comp_det(self):
        print("Company Details :", self.c_name, self.c_id, self.c_add)


compny = Company("MCS", "0001", 'Hydarabad')
compny.Comp_det()
