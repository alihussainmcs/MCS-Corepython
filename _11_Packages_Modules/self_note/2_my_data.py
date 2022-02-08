from _11_Packages_Modules._1_sample import sum1

num1 = sum1.x
num2 = sum1.y

print("Addition of 2 numbers : ", num1+num2)

name = sum1.name
add = sum1.add

print('Name of person :', name)

print('Address of person :', add)

'''
packages/ modules /  variable,functions,class
---------------------------------------------
1.  Builtin/Predefined 
2.  User defined       .......
3.  External           ....... > python -m pip install <libname>

'''


from random import randint
randint(1, 100)
