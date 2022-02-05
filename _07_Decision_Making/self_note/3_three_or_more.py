# REQ: Find whether given number is positive or negative or 0
a = 10

if a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative ")
else:
    print("Number is zero ")

a = -10

if a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative ")
else:
    print("Number is zero ")

a = 0

if a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative ")
else:
    print("Number is zero ")

print()

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

print()

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

print()

age = 24  # int(input("Enter your age? "))
if age >= 18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")
