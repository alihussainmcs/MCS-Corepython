import json
import csv

f = open('json_file.json')
data = json.load(f)

cntry_data = exec("tempvar = " + data)
f.close()
"""
import json

mystring = "{'Date': 'Fri, 19 Apr 2019 03:58:04 GMT', 'Server': 'Apache/2.4.39', 'Accept-Ranges': 'bytes'}"

exec("tempvar = " + mystring)
mystring = json.dumps(mystring)
myJson = json.loads(mystring)

print(str(tempvar['Date']))
print(str(myJson))
"""
f = open('json_to_csv1.csv', 'w')
csv_file = csv.writer(f)

# Counter variable used for writing
# headers to the CSV file
count = 0

for cntry in cntry_data:
    if count == 0:
        # Writing headers of CSV file
        header = cntry.keys()
        csv_file.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_file.writerow(cntry.values())
