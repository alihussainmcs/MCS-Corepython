class College:
    # State
    def __init__(self, c_name, c_id, c_add):
        self.c_name = c_name
        self.c_id = c_id
        self.c_add = c_add
    # Behaviour

    def college_info(self):
        print("College information : ", self.c_name, self.c_id, self.c_add)


coll_1 = College("IES", 177, "Bhopal")
coll_1.college_info()

coll_2 = College('Victoria memorial inter college', 10002, 'Siwan')
coll_2.college_info()
