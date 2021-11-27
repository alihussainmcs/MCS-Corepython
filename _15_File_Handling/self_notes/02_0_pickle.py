"""
# The process in which conversion of
# class object --> bytes - pickle or serialization. Here,using dump()
# syntax: pickle.dump(object, file)

# bytes --> class object - unpickle or deserialization. Here, using load()
# syntax: object=pickle.load(file)

# we need to create class for structured data of different data types string,int,float
# create a class with instance variables e_id, e_name, e_sal
"""

"""
class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))
"""

# we need to create a object to the class, to store actual data into that object.Later this
# object should be stored into a binary file in the form of bytes.
# pickle.dump(object, file) stores object into binary file
# for unpickling , using load()
# object = pickle.load(file)

# To pickle Emp class objects , we have to import Emp.py file as module is available.

import employee
import pickle

# opening emp.dat file as binary file for writing
f = open('emp.dat', 'wb')
n = int(input('How many employees to add : '))

for i in range(n):
    id = int(input('Enter id:'))
    name = input('Enter name: ')
    sal = float(input('Enter salary: '))

    # create an Emp class object
    e = employee.Employee(id, name, sal)
    # store the object e into file f

    pickle.dump(e, f)

# close the file
f.close()
