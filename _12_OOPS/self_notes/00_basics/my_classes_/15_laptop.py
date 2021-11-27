class Laptop:
    def __init__(self, l_brand, l_gen, l_price):
        self.l_brand = l_brand
        self.l_gen = l_gen
        self.l_price = l_price

    def lap(self):
        print("Laptop Details :", self.l_brand, self.l_gen, self.l_price)


lap1 = Laptop("HP", 5, 48000)
lap1.lap()
