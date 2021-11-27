import csv

csv_data = []

with open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv", 'r') as phone_data:
    my_csv = csv.reader(phone_data, delimiter=',')

    for i in my_csv:
        csv_data.append(i)

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
        if csv_d[0].strip() == inpt or csv_d[1].strip() == inpt:
            print(f"Result {count} : {temp_csv}")
            count = count + 1
            matches = True
    if not matches:
        print("No Result Found")
