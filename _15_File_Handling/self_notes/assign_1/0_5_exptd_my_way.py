import csv

csv_data = []

with open("phone_data1.csv", 'r') as phone_data:
    my_csv = csv.reader(phone_data, delimiter=',')
    for i in my_csv:
        csv_data.append(i)
print(csv_data)
print(csv_data[0][0])
print(csv_data[0][1])
print(csv_data[0][2])

with open("C:/Users/ali hussain/Downloads/query - Copy.txt", "r") as query_data:
    input_data = query_data.read()
    input_data = input_data.splitlines()

for inpt in input_data:
    count = 1
    matches = False
    print(f"matches for {inpt}")
    for csv_d in csv_data:
        temp_csv = csv_d
        csv_d = csv_d[0].split(',')
        print(csv_d[0])

        if csv_d[0].strip() == inpt or csv_d[1].strip() == inpt:
            print(f"Result {count} : {temp_csv}")
            count = count + 1
            matches = True
    if not matches:
        print("No Result Found")
