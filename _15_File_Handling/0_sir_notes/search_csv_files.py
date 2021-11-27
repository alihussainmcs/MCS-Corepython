import csv

f = open('C:/Users/LENOVO PC/Desktop/student1.csv', 'r')
stud = csv.reader(f)
for i in stud:
    print(i)

f.close()

f1 = open('C:/Users/LENOVO PC/Desktop/student1.csv', 'r')
csvread = csv.reader(f1)
search_roll = input("enter roll number:")
flag = False
for rec in csvread:
    if rec[0] == search_roll:
        print("Record found")
        print("First_Name:", rec[1])
        print("Last_Name:", rec[2])
        print("DOB:", rec[3])
        print("ethinicity:", rec[4])
        print("gender:", rec[5])
        flag = True

if flag == False:
    print("Record not found")
f1.close()

import csv

f2 = open("C:/Users/LENOVO PC/Desktop/student1.csv", 'w')
csvread = csv.reader(f2)
                  



