class Baloon:
    def __init__(self, b_shape, b_radius, b_clr):
        self.b_shape = b_shape
        self.b_radius = b_radius
        self.b_clr = b_clr

    def balo(self):
        print("Baloon Dtails :", self.b_shape, self.b_radius, self.b_clr)


bal1 = Baloon("Oval", 20, "blue")
bal1.balo()
