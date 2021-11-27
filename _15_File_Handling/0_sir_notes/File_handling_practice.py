'''

# create a text file

f = open("myfile.txt", 'w')
str = input("enter the text")
f.write(str)
f.close()


# create py file
f = open("manikanta.py", 'w')
str = input("enter the data:")
f.write(str)
f.close()


f = open("file1", 'w')
var = ("johnbhvvcvlu")
f.write(var)
f.close()

print("____without Exception____")
file_obj = open("myfile1", 'w')
str = input("Enter the string: ")
file_obj.write(str)
file_obj.close()

print("2.____with Exception____")

try:
    file_obj = open("myfile2", 'w')
    print("file data", file_obj)
    print("file type", type(file_obj))
    data = input("Enter the Text :")
    file_obj.write(data)
except FileNotFoundError as fnf:
    print("File not found ")
    print(fnf)
finally:
    file_obj.close()
    print("completed")

print("3.using functions")

def writedata(file, f_mode):

    try:
        file_obj = open(file, f_mode)
        print("file data:", file_obj, type(file_obj))
        data = input("enter data")
        file_obj.write(data)
    except FileNotFoundError as fnf:
        print("file not found")
        print(fnf)
    finally:
        file_obj.close()
        print("file is closed")

file_path = "myfile1.txt"
mode = 'w'
writedata(file_path, mode)

print("4.---using oops instance method---")

class File_Handling:
    def __init__(self, file_obj, mode):
        self.file_obj = file_obj
        self.mode = mode
    def get_fileobj(self, in_data):
        try:
            file_obj = open(self.file_obj, self.mode)
            print("file type", file_obj, type(file_obj))
            file_obj.write(in_data)
        except FileNotFoundError as fnf:
            print("FileNotFoundError")
            print(fnf)

        finally:
            file_obj.close()

f = File_Handling("created_files/write text 4.py", 'w')
data = "shyaamaa sudara"
f.get_fileobj(data)


print("5.using oops static method ")

class File_handling:

    @staticmethod
    def write_data(file_path, in_data):
        try:
            file_obj = open(file_path, 'w+')
            file_obj.write(in_data)
        except FileNotFoundError as fnf:
            print("file not found", fnf)
        finally:
            file_obj.close()

file_p = "C:/Users/LENOVO PC/Desktop/mani45.txt"
data = "welcome to india"
File_handling.write_data(file_p, data)

'''


file_obj = open("created_files/shiva.txt", 'w')
print("data", file_obj)
print("type", type(file_obj))
x = "hello world"
file_obj.write(x)
file_obj.close()


file_obj = open("created_files/raja.txt", 'w')
string = "super super"
file_obj.write(string)
file_obj.close()


print("____ without context manager____")  # open, write, close

file = open("created_files/x.txt", 'w')
file.write("hello")
file.close()

try:
    file_obj = open("created_files/y.txt", 'w')
    file_obj.write("hello")
except Exception as ex:
    print("exception", ex)
finally:
    file_obj.close()

print("operation completed")

with open("created_files/y.txt", 'r') as f:
    f.read()

print("2.____with context manager___")


with open("context.txt", 'w') as file21:
    file21.write("may i come in")
    file21.close()
'''
file_descriptors = []
for x in range(10000):
    file_descriptors.append(open("context.txt", 'w'))
'''
print("___using context manager___")


class Contextmanager():

    def __init__(self):
        print("init method")

    def __enter__(self):
        print("enter method")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit method")


with Contextmanager() as manager:
    print("statement block")

# file management using context manager


class Contextmanager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Contextmanager("created_files/seeta.txt", 'w') as x:
    x.write("help each other")

print(x.close())

print("___connecting to database server____")

# Python program shows the connection management for MongoDB

from pymongo import MongoClient

class MongoDBConnectionManager():

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.host = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

with MongoDBConnectionManager('localhost', '27017') as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({'_id': 1})
    print(data)





