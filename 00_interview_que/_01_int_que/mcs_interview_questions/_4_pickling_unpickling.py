"""
4. what is pickling and unpickling:

“Pickling” is the process whereby a Python object hierarchy is converted into a
byte stream, and “unpickling” is the inverse operation, whereby a byte stream
(from a binary file or bytes-like object) is converted back into an object hierarchy.

4.1:Pickling and unpickling modules:

The first one is a dump, which dumps an object to a file object and the second
one is load, which loads an object from a file object.

pickle.dump(object, file_obj, protocol)

This function takes three arguments -

    1.Python object to serialize.
    2.File object in which the serialized python object must be stored.
    3.Protocol (If a protocol is not specified, protocol 0 is used. If the protocol is specified as a negative value or
    HIGHEST_PROTOCOL, the highest protocol version available will be used.)

the Pickle module provides the dump() and dumps() methods for pickling.
For unpickling, the load and loads() methods are used.

#pickling via dump()method:

The dump() method in Python is used to pickle objects and store them on a disk.
The dump() method takes two parameters. The first parameter is the object to be
pickled and the second parameter is the file path that stores the pickled object.

#example:

import pickle

car_list = ["Honda", "Toyota", "Kia", "Mercedes", "Ford", "BMW"]
car_pickle = open ("E:/Datasets/car_pickle_file", "wb")
pickle.dump(car_list, car_pickle)

To unpickle a pickled object stored on a disk, you need to use the load() method.

#example:

car_contents = open("E:/Datasets/car_pickle_file", "rb").read()
print(car_contents)

output confirms that the pickled object has stored data in the form of bytes.

#pickling via dumps()method:

The dumps() method also pickles the data. However, instead of writing the pickled
object to disk, the dumps() method returns a string that contains serialized or
pickled object contents.

#example:
import pickle

car_list = ["Honda", "Toyota", "Kia", "Mercedes", "Ford", "BMW"]
car_list = pickle.dumps(car_list)
print(car_list)

the car_list object has been pickled into a string which is printed on the console.

4.2:unpickling via load() method:

the load() method can be used to unpickle the pickled Python object.
You have to first open the pickled file using rb (read-binary) permission
and pass the opened file to the load() method

#example:

car_pickle = open ("E:/Datasets/car_pickle_file", "rb")
car_contents = pickle.load(car_pickle)
print(car_contents)

#output:

['Honda', 'Toyota', 'Kia', 'Mercedes', 'Ford', 'BMW']


you can see contents of the actual car_list object that was pickled in the previous section.
As expected, it matches the original list from before we pickled it.

#unpickling via loads()method:

the loads() method to unpickle an object that is pickled in the form of a
string using the dumps() method, instead of being stored on a disk via the the dump() method.

#example:
import pickle

car_list = pickle.loads(car_list)
print(car_list)

the car_list object that was pickled to a car_list string is unpickle via the loads() method.



"""