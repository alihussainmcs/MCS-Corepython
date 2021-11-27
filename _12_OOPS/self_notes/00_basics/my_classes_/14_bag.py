class Bag:
    def __init__(self, b_clr, b_size, b_price):
        self.b_clr = b_clr
        self.b_size = b_size
        self.b_price = b_price

    def ba(self):
        print("Bag Details :", self.b_clr, self.b_size, self.b_price)


bag1 = Bag("Black", '15 cm', 900)
bag1.ba()
