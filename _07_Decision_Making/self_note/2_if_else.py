# if....else  ==> 2  conditions

# REQ: User always give 2 different values.Compare them

a = 10

b = 101

if a > b:
    print("a is greater than b ")
else:
    print("a is less than b")

print()

a = 11
b = 10

if a > b:
    print("a is greater than b ")
else:
    print("a is less than b")

print()

i = 10
if i == 10:

    #  First if statement
    if i < 15:
        print("i is smaller than 15")

    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

print()

i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")
