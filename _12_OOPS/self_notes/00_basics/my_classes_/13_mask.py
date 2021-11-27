class Mask:
    def __init__(self, m_name, m_price, m_clr):
        self.m_name = m_name
        self.m_price = m_price
        self.m_clr = m_clr

    def mas(self):
        print("Mask details :", self.m_name, self.m_price, self.m_clr)


mask1 = Mask("N-95", 75, "Green")
mask1.mas()
