'''

'''

'''
Access modifiers : public private protected default
'''
'''
class Employee:
     Employee(eid,name,sal):  # constructor
         this.eid = eid
         this.name = name
         this.sal = sal
        
     private void getedata(): 
         println("Emp data")

0_sir_notes = Employee(100, 'MadhuN', 10000)
0_sir_notes.getedata()

'''


class Employee:
    def __init__(self):
        pass

    def _getx(self):
        return "hello"

    def get_edata(self):
        val = self._getx()
        print(val)

    def update_edata(self):
        val = self._getx()
        print(val)

emp = Employee()
emp.get_edata()
