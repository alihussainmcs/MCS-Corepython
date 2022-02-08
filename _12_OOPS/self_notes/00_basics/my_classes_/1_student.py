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


class Student1:
    # State
    def __init__(self, name, id, loc):
        self.name = name
        self.id = id
        self.loc = loc

    # Behavior
    def stu_data(self):
        print('Student data :', self.name, self.id, self.loc)


st1 = Student1('Ali', '0044', 'India')
st1.stu_data()


