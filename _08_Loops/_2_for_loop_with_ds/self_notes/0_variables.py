# Variable

"""
if we want to use value in one place,
then directly use the value
"""
print('10 is ', 10)

print('10 + 20 is ', 10+20)

print('10 - 20 is ', 10-20)

print('10 * 20 is ', 10*20)

print('10 / 20 is ', 10/20)

print('10 // 20 is ', 10//20)

print('10 ** 20 is ', 10**20)

'''
if we want to use value in multiple places,
then assign the value to a variable 
'''
a = 10
b = 20
c = a + b
print("a is ", a)
print("b is ", b)
print("c is a + b : ", c)

x = 50
y = 20
print("Addition is : ", x+y)
print("Subtraction is : ", x-y)
print("Multiplication is : ", x*y)
print("Division is : ", x/y)
print("Floor Division is : ", x//y)

print("-----Single usage------")

for char in 'Hello Python':
    if char == ' ':
        continue
    else:
        print("Character : ", char)

print("-----Multiple usage-----")

msg = 'Hello Python'
print("................With space............")

for char in msg:
    print("Character : ", char)
print("................Without space............")
for char in msg:
    if char == ' ':
        continue
    else:
        print("Character : ", char)
