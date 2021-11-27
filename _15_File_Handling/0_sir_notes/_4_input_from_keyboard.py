

print("-----Program to calculate Simple Interest-----------------")
# Example to calculate Simple Interest

principle = int(input("Enter Principal  ="))
roi = int(input("Enter Rate of Interest ="))
time = int(input("Enter Time to Repay   ="))
sim_interest = (principle * roi * time)/100
print("Simple Interest is  = ", sim_interest)

print("-----Program to accept user details-----------------")

name = input("Enter your name ")
math = float(input("Enter your marks in Math"))
physics = float(input("Enter your marks in Physics"))
telugu = float(input("Enter your marks in Telugu"))
rollno = int(input("Enter your Roll no"))
print("Welcome ", name)
print("Your Roll no is ", rollno)
print("Marks in Maths is ", math)
print("Marks in Physics is ", physics)
print("Marks in Telugu is ", telugu)
print("Average marks is ", (math+physics+telugu)/3)
