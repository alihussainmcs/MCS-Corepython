class Employee:

    def __init__(self, eid, name='Ali Hussain', sal=10000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading


ali = Employee(100)

ila = Employee(101, 'Ila H')

kartik = Employee(102, 'Kartik Patel', 20000)

mic = Employee(103, 'Mic', )

nic = Employee('nic')


print("................................................................")


class Mango:
    def __init__(self, m_name='Maldev', m_taste='Sweet', m_price=50):
        self.m_name = m_name
        self.m_taste = m_taste
        self.m_price = m_price

        print("Mango Name :", self.m_name, ', Taste :', self.m_taste, ', Price :', self.m_price)


m1 = Mango()
m2 = Mango('Dasher')
m3 = Mango('Bambi', m_price=80)
m4 = Mango('Saved', m_price=30, m_taste='Light sweet')
