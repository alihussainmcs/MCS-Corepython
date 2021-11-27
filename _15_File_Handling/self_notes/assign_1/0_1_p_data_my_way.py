"""
Steps to read a CSV file:
--> Import the csv library. import csv.
--> Open the CSV file. The . ...
--> Use the csv.reader object to read the CSV file.csvreader = csv.reader(file)
--> Extract the field names. Create an empty list called header. ...
--> Extract the rows/records. ...
--> Close the file
"""

'''f = open("E:\MCS-Core Python\phone_dataset.csv", 'r')
list_data = [[] for i in range(4)]
for i, j in zip(range(len(list_data)), f):
    list_data[i] = j
print(list_data)

q = open("E:\MCS-Core Python\query - Copy.txt")
for i in q:
    print(i)'''
import csv

f = open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv")
read = csv.reader(f)
list1 = []
for i in read:
    list1.extend(i)
print(list1)

f1 = open("C:/Users/ali hussain/Downloads/query - Copy.txt")
query_list = []
read1 = csv.reader(f1)
for j in read1:
    query_list.extend(j)
print(query_list)

for i in query_list:  # This is for comparing the list
    for j in range(len(list1)):
        if i in list1[j]:
            print("Matches for Given list", i, ':', list1[j])
