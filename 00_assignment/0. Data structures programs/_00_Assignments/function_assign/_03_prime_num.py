# P03. print prime numbers

"""
1. CRUD       -->  Retrieve
2. STATE      -->  integer
3. BEHAVIOR   -->  int  |   for  |  == +=   if/else  class
"""

# 0. Mathematics
"""
prime number : 
                If a number is divisible by 1 and itself then that number is called prime number.   
num1 = 5  --> prime
num2 = 6  --> not prime
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
num_1 = 2
num_2 = 6
count = 0
for i in range(1, num_1 + 1):
    if num_1 % i == 0:
        count += 1

if count == 2:
    print("prime")
else:
    print("Not prime number ! ")

print("---------------------------------")
for i in range(1, num_2 + 1):
    if num_2 % i == 0:
        count += 1

if count == 2:
    print("prime")
else:
    print("Not prime number ! ")
# 3 Using Functions
print("--------3 Using Functions        ----------")


def prime_num(num):
    count_1 = 0
    for k in range(1, num + 1):
        if num % k == 0:
            count_1 += 1

    if count_1 == 2:
        print("prime")
    else:
        print("Not prime number ! ")


prime_num(6)

print("----------------------------")

prime_num(7)
# 4 OOPS
print("--------4 Object Oriented        ----------")


class PrimeNum:
    def __init__(self, num_c):
        self.num_c = num_c

    def prime_num_m(self):
        count_1 = 0
        for j in range(1, self.num_c + 1):
            if self.num_c % j == 0:
                count_1 += 1

        if count_1 == 2:
            print("prime")
        else:
            print("Not prime number ! ")


class_obj = PrimeNum(11)
class_obj.prime_num_m()

print("--------------------------------")
class_obj = PrimeNum(10)
class_obj.prime_num_m()

# 5 Exception handling
print("--------5 Exception handling     ----------")

try:
    num_3 = 'a'
    count_2 = 0
    for i in range(1, num_3 + 1):
        if num_3 % i == 0:
            count_2 += 1

    if count_2 == 2:
        print("prime")
    else:
        print("Not prime number ! ")
except TypeError as te:
    print(te)

print("-------------------------------------------------")

try:
    num_3 = 11
    count_2 = 0
    for i in range(1, num_3 + 1):
        if num_3 % i == 0:
            count_2 += 1

    if count_2 == 2:
        print("prime")
    else:
        print("Not prime number ! ")
except TypeError as te:
    print(te)

print("-------------------------------------------------")

try:
    num_3 = 10
    count_2 = 0
    for i in range(1, num_3 + 1):
        if num_3 % i == 0:
            count_2 += 1

    if count_2 == 2:
        print("prime")
    else:
        print("Not prime number ! ")
except TypeError as te:
    print(te)

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
