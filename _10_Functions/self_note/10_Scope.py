# scope of variable  LEGB Rule in python
print("...............Without global keyword ...................")
x = 100
print("Value of x1 :", x)


def get_data():
    # print("Value of x2 :", x) UnboundLocalError: local variable 'x' referenced before assignment
    x = 25
    print("Value of x3 :", x)


get_data()

print("Value of x4 :", x)

print("...............With global keyword 1st...................")
b = 20


def msg():
    a = 10
    global c
    c = 20
    print("Value of a inside function is", a)
    print("Value of b inside function is", b)
    print("Value of c inside function is", c)


msg()
#  print("Value of a outside function is", a) NameError: name 'a' is not defined
print("Value of b outside function is", b)
print("Value of c outside function is", c)

print("...............With global keyword with function call ...................")

x = "awesome"


def myfunc():
   global x
   x = "fantastic"
   print("Value of x inside function is", x)


myfunc()

print("Value of x outside function is", x)

print("...............With global keyword without function call ...................")
x = "awesome"


def myfunc():
   global x
   x = "fantastic"
   print("Value of x inside function is", x)


print("Value of x outside function is", x)


print("................With two global variable ...................")
print("...............With global keyword with function call ...................")

global y
y = "Python"


def myfunc():
   global y
   y = "World"

myfunc()
print("Global variable y is :" + y)

print("................With two global variable ...................")
print("...............With global keyword without function call ...................")

global h
h = "Python"


def myfunc():
   global h
   h = "World"


print("Global variable h is :" + h)
