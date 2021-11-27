import csv

f = open("student1.csv", 'a')
w = csv.writer(f)
data1 = ["Rollnum", "Name", "Marks"]
w.writerow(data1)
n = int(input("Enter the number of student:"))
for x in range(n):
    Roll = int(input("enter the Rollnum:"))
    Name = input("enter name of student:")
    Marks = int(input("enter marks:"))
    data1 = ["Roll", "Name", "Marks"]
    w.writerow(data1)
f.close()
f = open("student.csv", 'r')
stud = csv.reader(f)
for i in stud:
    print(i)
f.close()







