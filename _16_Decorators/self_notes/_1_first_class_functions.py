"""
@classmethod
@staticmethod

Decorator : Provides additional functionality for class or method/function
"""

''' 


#1 one time usage
print(10)

# 2 or more places
x = 10  
print(x)         XXX ---> print(10)
print(x+100)     XXX ---> print(10+100)
'''


def some_function():
    return 'ali'


call = some_function
print(call())


def some_function2():
    def inner_function():
        print('im from inner function')

        def innermost_function():
            print('im from innermost function')

        return innermost_function

    print('harsha in some_func2')
    return inner_function


call2 = some_function2()
print('printing from call2', call2)
print('...................................')

call3 = some_function2()()()


def some_function3(func):
    print('im executing before calling main_function')
    func()
    print('im executing after calling main_function')


def main_function():
    print('im executing from main function')


call4 = some_function3(main_function)


def decorator_function(func):
    def wrapper():
        print('im calling from wrapper')
        func()
        print('im below calling decorator func withing wrapper')

    return wrapper


@decorator_function
def main2_function():
    print('im from main2')


@decorator_function
def main3_function():
    print('im from main3')


print('...........................below main func2...........')
main2_function()

print('...........................below main func3...........')
print('................', main3_function())


# call5 = decorator_function()
# print('...............call5..........',call5)

# call5(main2_function)


def sum1(num1, num2):
    res = num1 + num2
    return res


sum1(10, 20)  # No use

# 1 one time usage
print("Sum is : ", sum1(10, 20))

# 2 two or more places
output = sum1(10, 20)

print(output)
output()
output = sum1(10, 20)
print("First usage: ", output)
print("Second usage: ", output + 24)


def sum2(num1, num2):
    res = num1 + num2
    print("Addition is : ", res)


sum2(10, 20)  # Direct function call
n1 = 10
n2 = 20
sum2(n1, n2)

# IF function has return type
# 1  Single time
print("Type 1 :", sum1(10, 20))  # print(10)
print("Type 1 :", sum1(10, 20) + 100)

# 2 Mulitple times
output = sum1(10, 20)
print(output)  # x = 10 print(x)
print(output + 100)
print(output + 200)

# IF function has no return type
sum2(10, 20)  # We are not expecting function return type

print("------------------Function details------------------  ")


def getdata():
    print("I am in getdata")
    return 100


print("Function call  : ", getdata())
print("Function name**: ", getdata)  # return a reference to a function
print("Function type  : ", type(getdata))
print("Function name  : ", id(getdata))


# output = getata
# output()


class Employee:
    pass


print("Class details  ")

print("----Name :", Employee)
print("----Type :", type(Employee))
print("----Type :", id(Employee))

# Concept : We can pass "function name" as an argument to any other function

print("---------Variable concept------")
x = 10
print(x, type(x))  # x.__str__()

x = 10
y = 20
print("Sum function call ", sum1(x, y))  # sum1(x, foo(10))
print("Sum function def  ", sum1)

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1. First Class functions
2. Nested Functions
3. Returning Functions
'''
print("----------Function calls------------------")


def foo(bar):
    # print("Output is :", bar + 1)
    return bar + 1


# 1
foo(10)  # if print statement is there inside function
# 2
print(foo(10))  # if return stmt exists
# 3
x = foo(10)  # if return stmnt exits and output is being used in 2 or more places
print(x)

print("Sum result1 : ", sum1(10, 20))
print("Sum result2 : ", sum1(10, foo(19)))

print("Comparison :", foo(20) > 3 + 10)  # functions return a value based on the given arguments.
print("----------Function calls------------------")

'''
                Steps execution:
                1. foo(20) - function call   will get response         ==> 21   
                2. 3+10    - perform arithmetic ops. and give result   ==> 13
                3. compare function response with arithm ops result   ==> 21 > 13  => True
                4. Give result to print function
                
                print("Comparison ", 10)      # 0
                print("Comparison ", 10+20)   # 1
                print("Comparison ", 10+20 == 30)   # 2
                print("Comparison ", 10+20 == 10+30)   # 3
                print("Comparison ", foo(10+20) == 10+30)   # 4
'''


def foo2(bar):
    return bar + 1


foo2(2)
print(foo2(3))
print(type(foo2))
print(foo2)

print("---Function calling Chain-----")


def x():
    print("x function")


def y():
    print("y function")
    x()


def z():
    print("z function")
    y()


z()

# 1. FIRST CLASS FUNCTIONS:
print("============1. FIRST CLASS FUNCTIONS=============")

'''

Functions where reference is passed
Here foo_func requires function name why because we have used 
the same parameter during function call

X                Y                       Z        
Chandra   <--    paytm           <--  Vinay     10             
            10K
          --->                     --> 
          
foo(bar)           medium(f_name, var)  <==    get_data()
   return bar+1      out = f_name(var)                  functionname -   foo  
                     return out                         args         -   10 
                    meium(foo,10)                             resp = medium(foo, 10)
                    out = foo(10)                             resp = meium(chanra,10)  # 11
                      out = 11                           # business logic    
   
def get-data():
   resp = medium(foo,10)   resp = 12
   return resp

def medium(func_name, var):  def medium(foo,10)
    out = func_name(var)            out = foo(10)  out = 12
    return out

def foo(var):
    return var + 2
    
    
final_result = get_data() 
print(final_result) --> 12      
'''

print(" *** Without first class function  ***")


# foo - Chandra
# get_data - Vinay

def foo2(bar):  # Chandra
    return bar + 1


def get_data():  # Vinay
    res = foo2(100)  # We are calling other function from our function
    print("Val from foo is : ", res)


get_data()

print(" *** With first class function  ***")


def foo11(bar):  # Chandra
    return bar + 1


def mediator(foo_func, val):  # Naveen
    output2 = foo_func(val)  # foo(100)
    return output2


def get_daata():  # Vinay
    res = mediator(foo11, 100)
    print("Val from foo is : ", res)


get_daata()

print("------------------------------------")
print(" *** With first class function  mulitple args***")


def foo(*args):  # Chandra
    sum = 0
    for each in args[0]:
        sum += each
    return sum


def mediator1(foo_func, *args):  # Naveen
    output1 = foo_func(*args)  # # foo((10,20,30))
    return output1


def get_daata():  # Vinay
    res = mediator1(foo, (10, 20, 30, 20))
    print("Val from foo is : ", res)


get_daata()

print("------------------------------------")
