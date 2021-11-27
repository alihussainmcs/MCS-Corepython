# Everything is an object in Python

# string list tuple dictionary set
ag = 10
'''
age = int(10) object creation   
      Employee(101,'Ali',10000)
'''
age = int(10)  # int() float() long() str() list() tuple() dict() set()
print(age)
print(id(age), type(age))

lst = [1, 2, 3]  # list([1,2,3])
li = list([1, 2, 3])
li.append(100)
# li.xyz()


ms = 'Hello World'  # str('Hello World')
msg = str('Hello World')

'''
ali = Employee(101, 'Ali')
li = list( [1,2,3] )
list    -  classname -> builtins.py module 
[1,2,3] -  argument 
li      -  object**/ instance*/ ref. variable 
'''

# ali = Employee(101,'AliH',1000) ==> object creation

print(li, id(li), type(li))

print(type(10.5), type(True), type('Hello'), type((1, 2, 3)))

print(li)  # list1.__repr__()   str() vs repr()

dict1 = {1: 1, 2: 2}
dict1.keys()

print("......................................................................")

a = "Hello World"  # str
print("String :", a)

b = 20  # int
print("Integer :", b)

c = 20.5  # float
print("Float :", c)

d = 1j  # complex
print("Complex :", d)

e = ["apple", "banana", "cherry"]  # list
print("List :", e)

f = ("apple", "banana", "cherry")  # tuple
print("Tuple :", f)

g = range(6)  # range
print("Range :", g)

h = dict(name="John", age=36)  # dict
print("Dictionary :", h)

i = {"apple", "banana", "cherry"}  # set
print("Set :", i)

j = frozenset(("apple", "banana", "cherry"))  # frozenset
print("Frozenset :", j)

k = bool(5)  # bool
print("Bool :", k)

o = bytes(5)  # bytes
print("Bytes :", o)

m = bytearray(5)  # bytearray
print("Bytearray :", a)

n = memoryview(bytes(5))
print("memoryview :", a)
