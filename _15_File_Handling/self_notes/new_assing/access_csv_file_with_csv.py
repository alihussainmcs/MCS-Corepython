import csv  # import pandas module
date = []  # create a list to store date list from file

with open('data_file1.csv', newline='') as csv_file:
    data = csv.DictReader(csv_file)
    for row in data:
        date.append(row['date'])

# print(date)
print('Number of holidays are :', len(date))
# print(date)

# Create a temporary list of years list which are present and not present in date of data
temp_date = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
str_1 = str(date)
# print(str_1)

for i in temp_date:
    print(f'the number of holiday in {i} is : {str_1.count(i)}')  # get the required output
