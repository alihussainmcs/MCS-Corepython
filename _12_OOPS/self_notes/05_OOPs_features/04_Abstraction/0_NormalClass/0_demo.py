"""


Solution : Use Inheritance
           Implement classes as Super class - Sub class mechanism
"""


class University:
    def __init__(self):
        print("Super Pass")

    @staticmethod
    def branch(b_name):
        print("Branch :", b_name)


class College(University):
    def __init__(self):
        super().__init__()
        print('Sub Pass')


u1 = College()
u1.branch('CSE')

print()

u1 = College()
u1.branch('EC')
