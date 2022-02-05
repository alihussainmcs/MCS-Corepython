print(10)

print()

print(10+20)

print()

'''Immutable'''
'''
Immutable:
-----------
Numbers : int float 
Boolean : bool
String 
Tuple 

Mutable : 
---------
List Dictionary Set
'''
x = 10
print(x)
print()

print(id(x))
print()

x = 20
print(x)

print()

print(id(x))

print()

x = 10
print(x)
x = x + 10
print(x)
print(id(x))

msg = 'Hello'
print("Message : ", msg)
msg = 'World'
print("Message : ", msg)

msg = 'Hello'
print("Message : ", msg)
msg = msg + 'World'
print("Message : ", msg)
