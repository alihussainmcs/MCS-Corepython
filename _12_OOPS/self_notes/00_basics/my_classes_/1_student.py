class Student:
    # State
    def __init__(self, st_name, st_rl_num, st_marks):
        self.st_name = st_name
        self.st_rl_num = st_rl_num
        self.st_marks = st_marks

    # Behaviour
    def std_details(self):
        print("Student details is :", self.st_name, self.st_marks, self.st_rl_num)


stud_1 = Student("Python", 21, 1)
stud_1.std_details()
