from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        # "Abstarct Method"
        pass

    def offers(self):
        print("Providing offers")
    # Sub class/ child class of abstract class


class SBI(Bank):
    def interest(self):
        print("In SBI bank 5 % interest")


class HDFC(Bank):
    def interest(self):
        print("In HDFC 7 % interest")


s = SBI()
h = HDFC()
s.bank_info()
s.interest()
h.bank_info()
h.interest()

"""
b = Bank()   # 5L CAN - 5L Water   # ERROR
b.interest() # ERROR
b.offers() # ERROR

s = SBI() # 2L CAN - 2L Water
s.bank_info()
s.interest()

h = HDFC()   # 2L CAN - 2L Water
h.bank_info()
h.interest()

5L Can - 5L Water
2L Can - 2L Water


Java, .Net:
---------------

# 1:  5L Can - 5L Water  
b = Bank()   # 5L CAN - 5L Water   
b.interest() 
b.offers() 

# 2: # 2L CAN - 2L Water
s = SBI() # 2L CAN - 2L Water
s.bank_info()
s.interest()


# 3: # 5L CAN - 2L Water   -- Upcasting
Bank b = SBI()
b.interest() 
b.offers()  # ERROR


# 4: 2L Can - 5L Water    -- Down casting
SBI s = Bank()   XXX

SBI s = (s)Bank()   XXX


"""
