"""
         Write the program and fetch data using http get and point number of holidays in England & Wales the
         group them based of year.
         Export the json data into csv file  using url
"""

# import urllib library
from urllib.request import urlopen

# import json
import json
import csv
# store the URL in url as
# parameter for urlopen
url = "https://www.gov.uk/bank-holidays.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())
cntry_data = data_json['england-and-wales']['events']
# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for cntry in cntry_data:
    if count == 0:
        # Writing headers of CSV file
        header = cntry.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(cntry.values())

data_file.close()

# import pandas to read csv file
import pandas as pd

x = []
csv_f = pd.read_csv('data_file.csv', encoding='cp1252')
# print(csv_f)

date = []
for i in csv_f.iloc[:, 1]:
    date.append(i)

# print(date)
print('Number of holidays are :', len(date))
# print(date)

temp_date = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
str_1 = str(date)
# print(str_1)
for i in temp_date:
    print(f'the number of holiday in {i} is : {str_1.count(i)}')
