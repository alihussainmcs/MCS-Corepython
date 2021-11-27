# import pandas module
import pandas as pd

csv_f = pd.read_csv('data_file.csv', encoding='cp1252')
# print(csv_f)

date = []  # create a list to store date list from file
for i in csv_f.iloc[:, 1]:
    date.append(i)

# print(date)

print('Number of holidays are :', len(date))
# print(date)

# Create a temporary list of years list which are present and not present in date of data
temp_date = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
str_1 = str(date)
# print(str_1)
for i in temp_date:
    print(f'the number of holiday in {i} is : {str_1.count(i)}')  # get the required output
