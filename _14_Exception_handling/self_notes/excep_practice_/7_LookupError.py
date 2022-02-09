"""
LookupError
│   ├── IndexError
│   └── KeyError

"""

print("-----------------------IndexError-----------------------")

# list_1 = [1, 2, 3, 4, 'Ali']
# list_1[101] IndexError: list index out of range

try:
    tup = 1, 2, 3, 4, 5
    tup[101]
except IndexError as i:
    print(i)


def index_error(list_n):
    try:
        list_n[101]
    except IndexError as i:
        print(i)


index_error('i am the hulk !')

print("-----------------------KeyError-----------------------")
"""

A Python KeyError is raised when you try to access an item in a dictionary that does not exist. You can fix this error 
by modifying your program to select an item from a dictionary that does exist. Or you can handle this error by checking
if a key exists first.

"""
raspberry_pi = {
    "name": "Raspberry Pi 4",
    "price": 35.00,
    "RAM": "4GB"
}

# print(raspberry_pi["usb_ports"])  # KeyError: 'usb_ports'

try:
    print(raspberry_pi["usb_ports"])
except KeyError as k:
    print(k)
finally:
    print(" end of execution !")
