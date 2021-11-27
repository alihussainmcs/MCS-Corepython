import json
import csv

f = open('json_file.json')
data = json.load(f)
cntry_data = data['england-and-wales']['events']
f.close()

f = open('json_to_csv.csv', 'w')
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
