print("........................Conversions...........................")

print(".........................Converting int in other data types ...........................")

a = 10
print("Number a is ", a)

print(("Type ", type(a)))

print("Converting int a=10 to float  ", float(a))

print("Converting int a=10 to string  ", str(a))

print("Converting int a=10 to bool  ", bool(a))

print("Converting int a=10 to bool  ", complex(a))

print(".........................Converting float in other data types ...........................")

b = 10.7

print("Number b is ", b)

print(("Type ", type(b)))

print("Converting float b=10.7 to int  ", int(b))

print("Converting float b=10.7 to string  ", str(b))

print("Converting float b=10.7 to bool  ", bool(b))

print("Converting float b=10.7 to bool  ", complex(b))

print(".........................Converting String in other data types ...........................")

c = '10'

print("String c is ", c)

print("Converting string c='10' to int ", int(c))

print("Converting string c='10' to float ", float(c))

print("Converting string c='10' to bool ", bool(c))

print("Converting string c='10' to complex ", complex(c))

print("..................Converting boolean to other data type........................")

d = True

print("Boolean value d is ", d)

print("Converting bool d = True to int ", int(d))

print("Converting bool d = True to float ", float(d))

print("Converting bool d = True to string ", str(d))

print("Converting bool d = True to complex ", complex(d))

print("....................Converting complex to data type .................................... ")

e = 10 + 11j

print("Complex value e is ", e)

# print("Converting complex e = 10 +11j in int ", int(e)) # TypeError: can't convert complex to int

# print("Converting complex e = 10 +11j in float ", float(e)) #  TypeError: can't convert complex to float

print("Converting complex e = 10 +11j in String ", str(e))

print("Converting complex e = 10 +11j in boolean ", bool(e))
