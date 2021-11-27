print("--------------------------------------------------------------------------")
import csv
f = open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv", 'r')
read = csv.reader(f)
list1 = []
for i in read:
    list1.extend(i)
# print(list1)

f1 = open("C:/Users/ali hussain/Downloads/query - Copy.txt", 'r')
query_list = []
read1 = csv.reader(f1)
for j in read1:
    query_list.extend(j)
# print(query_list)

for i in query_list:  # This is for comparing the list
    for j in range(len(list1)):
        if i in list1[j]:
            print("Matches for Given list", i, ':', list1[j])
