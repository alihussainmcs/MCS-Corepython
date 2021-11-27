class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)
        return self.r_no + self.name + self.marks


madhu = Student(16, 10, 65)
a = madhu.get_sinfo()
print(a)
