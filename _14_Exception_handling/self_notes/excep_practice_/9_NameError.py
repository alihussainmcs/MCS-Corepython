"""
Handling NameError Exception in Python

There are several standard exceptions in Python and NameError is one among them. NameError is raised when the identifier
being accessed is not defined in the local or global scope. General causes for NameError being raised are :


"""

# prnt('ali')  # NameError: name 'prnt' is not defined


# print(ali) NameError: name 'ali' is not defined
# ali = "hulk"
"""  
def assign():
    ali = "hulk"

assign()
print(ali)  NameError: name 'ali' is not defined

"""

try:
    ali = 'hulk'
    print(hulk)
except NameError as n:
    print(n)


def name_error():
    try:
        a = 10
        print(b)
    except NameError as n:
        print(n)


name_error()

print("----------------------------  UnboundLocalError  --------------------------------")
""" 
x = 10
def unbound_local_error():
    x += 1
    print(x) # UnboundLocalError: local variable 'x' referenced before assignment


unbound_local_error()
"""

"""
x = 5
def printx():
    print(x)
    x = 7

printx() UnboundLocalError: local variable 'x' referenced before assignment
"""

try:
    x = 5


    def print_x():
        print(x)
        x = 7
    print_x()
except UnboundLocalError as u:
    print(u)

