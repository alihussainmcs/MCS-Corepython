class Door:
    def __init__(self, d_mat, d_height, d_weight):
        self.d_mat = d_mat
        self.d_height = d_height
        self.d_weight = d_weight

    def door(self):
        print("Table Details :", self.d_mat, self.d_height, self.d_weight)


door1 = Door("Wood", 6, 30)
door1.door()
