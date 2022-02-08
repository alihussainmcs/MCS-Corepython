"""
json**
logging**
unittest**
csv**
datetime**
pdb**
random**

urllib*
copy*
functools*
io*
os*
pickle*
re*
threading*


concurrent
html
http
importlib
multiprocessing
site-packages
sqlite3
venv
xml
base64
calendar
ipaddress
"""
print(10)  # Single usage

x = 10
print(x)   # Multiple usage


# Generate a random number between 1 to 100
# include<stdio.h>

from random import randint, choice, SystemRandom
print("Random number : ", randint(1, 100))
print("Choice number : ", choice([1, 2, 3, 4, 5, 6]))
print("Import class  : ", SystemRandom)

print("--------------------------")

import random
print("Random number : ", random.randint(1, 100))
print("Choice number : ", random.choice([1, 2, 3, 4, 5, 6]))
print("Import class  : ", random.SystemRandom)


'''
sum(10,20)  # function calling
print(sum(10,20))
res = sum(10,20)
print("Result :",res)
'''
# Generate a random number between 1 to 100


# sum1(10,20)

# function definition
def sum1(n1, n2):
    res = n1 + n2
    return res

# function calling


sum1(10, 20)


def sum(n1):
    res = n1
    return res

# print(sum(10,20))


list_1 = [1, 2, 3, 100]

import random   # Here random is a module(in windows file)

print("Hello world ")  # 2 lines       Wrong -> 769 + 1
print("Random number : ", random.randint(1, 100))   # 173 line

'''
module  : .py file ,which contains collection of variables, functions and classes   161 modules
package : folder, group of packages+modules   31 packages  

Folder : either only folders/only files/files+folders
Package:             packages/only modules/packages+modules
'''

# import collections
# x = collections.OrderedDict
from collections import OrderedDict
x = OrderedDict

print("Ordered dict : ", x)
x = OrderedDict({})
x['eid'] = 100
x['name'] = 'MadhuN'
print("Ordered dict : ", x)

# import concurrent.futures.process
import xml.dom.domreg
print("Print given list : ", xml.dom.domreg.well_known_implementations)


from random import randint   # print(10)
print("Random number : ", randint(1, 100))

# import vs from
import random     # x = 10   print(x)
print("Random number : ", random.randint(1, 100))
print("All functions : ", random.__all__)
print("Other attributes  :", random.LOG4, random.RECIP_BPF)
