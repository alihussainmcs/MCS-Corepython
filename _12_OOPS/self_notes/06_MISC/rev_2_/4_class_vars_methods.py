class University:
    # State
    def __init__(self, u_name, u_id, u_add):
        self.u_name = u_name
        self.u_id = u_id
        self.u_add = u_add

    # Behaviour
    def uni(self):
        print("University Details : ", self.u_name, self.u_id, self.u_add)


clg1 = University("RGPV", 4620, "MP")
clg1.uni()

print(".....................2nd example of class ...................")


class Mask:
    def __init__(self, m_name, m_price, m_clr):
        self.m_name = m_name
        self.m_price = m_price
        self.m_clr = m_clr

    def mas(self):
        print("Mask details :", self.m_name, self.m_price, self.m_clr)


mask1 = Mask("N-95", 75, "Green")
mask1.mas()
