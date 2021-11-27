class School:
    # State
    def __init__(self, s_name, s_id, s_loc):
        self.s_name = s_name
        self.s_id = s_id
        self.s_loc = s_loc

    # Behaviour
    def school_det(self):
        print("School Detail :", self.s_name, self.s_id, self.s_loc)


school_1 = School("Victoria Memorial ", 8414, "Siwan")
school_1.school_det()
