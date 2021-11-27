# for unpickling, as we stored employee class objects in emp.dat file, to retrieve those
# objects we have to unpickle
# obj = pickle.load(f)

# Reads an object from file f, and returns into obj
# since obj belongs to Emp class  we can use display method use obj.display()
# use loop when we reach end of file and could not find any objects to read then
# raise an EOFError

import pickle

f = open('emp.dat', 'rb')
print('Employee details: ')
while True:
    try:
        # read object from file f
        obj = pickle.load(f)
        # display the contents of employee obj
        obj.emp_data()
    except EOFError:
        print('End of file reached...')
        break
