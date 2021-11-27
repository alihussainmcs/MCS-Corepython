class Mobile:
    def __init__(self, m_name, m_size, m_price):
        self.m_name = m_name
        self.m_size = m_size
        self.m_price = m_price

    def mobi(self):
        print("Mobile details :", self.m_name, self.m_size, self.m_price)


mob1 = Mobile("Realme2", "5 inch", 12000)
mob1.mobi()
