"""
          Write the program and fetch data using http get and convert in json file

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
print(data_json)

# Python program to write JSON
# to a file

# Data to be written

# Serializing json
# json_object = json.dumps(data_json, indent=4)
json_object = json.dumps(data_json)
# Writing to sample.json
with open("json_file.json", "w") as outfile:
    outfile.write(json_object)
