class Mango:
    # State
    def __init__(self, name_mango, clr_mango, tst_mango):
        self.name_mango = name_mango
        self.clr_mango = clr_mango
        self.tst_mango = tst_mango

    # Behaviour
    def mango_det(self):
        print("Mango Detail :", self.name_mango, self.clr_mango, self.tst_mango)


mango_1 = Mango('Dasahari', 'Yellow', 'Sweet')
mango_1.mango_det()

mango_2 = Mango('Maldev', 'Yellow', 'More Sweet')
mango_2.mango_det()
