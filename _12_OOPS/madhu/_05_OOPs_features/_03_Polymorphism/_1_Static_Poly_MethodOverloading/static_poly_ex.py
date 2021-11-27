'''
python interpreted programming language

 .java   ---compilation ---> .class   --runtime->


Polymorphism : Ability to exists in multiple forms
2 types : Static polymorphism - compile time - Ex => Method Overloading
          Dynamic polymorphism - run time    - Ex => Method Overriding
'''
# Static polymorphism

'''
Method overloading in other languages:
---------------------------------------
class Employee:
    def getdata(eid):
        pass
    def getdata(eid,name):
        pass
    def getdata(eid,name,sal):
        pass
   
0_sir_notes = Employee()
0_sir_notes.getdata(10)  17th line
0_sir_notes.getdata(10,'Madhu')  19th line
0_sir_notes.getdata(10,'Madhu',1000) 21st line

in Python:
----------
def getdata(eid = 0, name = None, sal = 0):  # Method Overloading
    pass

getdata(10)
getdata(10,'Madhu')
getdata(10,'Madhu',1000)   
getdata(name='Madhu', sal=1000) 
getdata(name='Madhu')
getdata(sal=1000) 
 

'''
x = 10
print(x)
x = 20
print(x)

def getdata(eid):
    print("Data is : ", eid)
getdata(10)

def getdata(eid, name):
    print("Data is : ", eid, name)

getdata(10) # ERROR
getdata(10,'Madhu') # WORKS

def getdata(eid, name, sal):
    print("Data is : ", eid, name, sal)

getdata(10) # ERROR
getdata(10, 'Madhu') # ERROR
getdata(10, 'Madhu', 1000)

# Solution is use one single method with default arguments for parameters


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()                   # getdata(id=None,name=None,sal=None)
getdata(10)                 # getdata(id=10,name=None,sal=None)
getdata(10, 'Madhu')        # getdata(id=10,name='Madhu',sal=None)
getdata(10, 'Madhu', 1000)  # getdata(id=10,name='Madhu',sal=1000)

'''
This method will exhibit Static polymorphism'''




# *args  **kwargs : Will see in decorator concept

