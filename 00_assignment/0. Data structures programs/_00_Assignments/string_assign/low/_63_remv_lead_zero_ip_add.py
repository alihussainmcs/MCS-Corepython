# P63. REQ : remove leading zeros from an IP address
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
ip = "216.08.094.196"

o/p  "216.8.94.196"

"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")
ip = "0216.08.094.01960"
print("IP Address :", ip)
new_ip = ".".join([str(int(i)) for i in ip.split(".")])
print("IP Address without leading zero : ", new_ip)

"""  2nd method
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)
"""

# 3 Using Functions
print("--------3 Using Functions        ----------")

# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
