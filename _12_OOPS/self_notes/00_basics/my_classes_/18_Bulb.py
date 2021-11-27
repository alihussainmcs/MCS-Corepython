class Bulb:
    def __init__(self, b_name, b_type, b_clr):
        self.b_name = b_name
        self.b_type = b_type
        self.b_clr = b_clr

    def bul(self):
        print("Bulb Details", self.b_name, self.b_type, self.b_clr)


bulb1 = Bulb("LED", "Cool", "White")
bulb1.bul()
