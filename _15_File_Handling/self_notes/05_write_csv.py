# write the data into csv file
import csv

with open('csv_pyhton.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'mobile_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'mobile_number': '9198765432', 'first_name': 'Iron', 'last_name': 'Man'})
    writer.writerow({'mobile_number': '9878765432', 'first_name': 'Smith','last_name': 'John'})
    writer.writerow({'mobile_number': '9398005432', 'first_name': 'Green', 'last_name': 'Hulk'})
    writer.writerow({'mobile_number': '9998711432', 'first_name': 'Red', 'last_name': 'Skull'})

print("Writing complete")

print("-------------------------------------------------------------------------------------------------------")
# write data using pandas
import pandas

df = pandas.read_csv('username.csv',
                     index_col='Person',
                     parse_dates=['Id'],
                     header=0,
                     names=['Person', 'Id', 'f_name', 'l_name'])
df.to_csv('hr_data_modified.csv')
print("Data Export to csv file completed")
