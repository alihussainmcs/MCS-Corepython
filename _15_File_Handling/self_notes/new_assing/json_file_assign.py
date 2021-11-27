"""
          Write the program and fetch data using http get and point out number of holidays in England & Wales
                 then group them based on year.
"""

# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
url = "https://www.gov.uk/bank-holidays.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
# print(data_json)

# print(data_json['england-and-wales']['events'])
# print(i['date'] for i in data_json['england-and-wales']['events'])
count_1 = 0
date = []  # create a list to store date list from file
for i in data_json['england-and-wales']['events']:
    count_1 += 1
    date.append(i['date'])

print('Number of holidays are :', count_1)
# print(date)


# Create a temporary list of years list which are present and not present in date of data
temp_date = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

str_1 = str(date)
# print(str_1)

for i in temp_date:
    print(f'the number of holiday in {i} is : {str_1.count(i)}')


print("------------------------------- my work ------------------------------------------")
# Retrieving event name from data 
h_name = []
for i in data_json['england-and-wales']['events']:
    for j in i:
        # print(i['date'])
        h_name.append(i['title'])

# print(h_name)


# Combining date and event name together in a list
res = {}
for key in date:
    for value in h_name:
        res[key] = value
        h_name.remove(value)
        break

# print("Result combination of date and events : ", res)


print("-------------------------------------------  extra work     ------------------------------------------------")
"""
m_rep = {}
for line in lines:

    w = line.strip().split(",")
    m = int(w[0].split("/")[0])
    amt = int(w[1])
    if m_rep.get(m)==None:
        m_rep[m]=amt
    else:
        m_rep[m]+=amt
print(m_rep)
----------------------------------------
result = {}

temp_date = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
str_1 = str(date)
# print(str_1)
for j in h_name:
    for i in temp_date:
        amt = h_name
        if result.get(i) is not None:
            result[j] = h_name
        else:
            result[j] = h_name

print(result.keys())
"""
