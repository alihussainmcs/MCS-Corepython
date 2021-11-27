# CRUD: ----- Read

data = open("HR Call.txt")
print(data.readlines())

for lin in data:
    print(lin.strip().split('\n'))

print('----------------------------- with function file read   txt file   -------------------------------------')
path = 'HR Call.txt'


def read_file(pat):
    with open(pat) as p:
        # print(p.readlines())
        for li1 in p:
            print(li1.strip().split('\n'))


read_file(path)

print("-----------------------------------     2nd file read   txt file   -------------------------------------------")

data_1 = open('my_text.txt')
# print(data_1.read())

for li in data_1:
    print(li.split(' '))

print("-----------------------------------    3rd file read  csv file    --------------------------------------------")

data = open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv")
# print(data.readlines())
my_da = []
for line in data:
    my_d = line.strip()
    my_da.append(my_d)

print(my_da[0])

print('-----------------------------------  4th ex. json file  ------------------------------------------------')
data = open("C:/Users/ali hussain/Downloads/sample2.json")
print(data)
print('-----------------------------')

print(data.read(100))
print('-----------------------------')
print(data.readlines(100))
print('-----------------------------')

print(data.readlines())

print('-----------------------------------  5th ex. xls file  ------------------------------------------------')
# data = open("C:/Users/ali hussain/Downloads/MCS_EAF.xls")
# print(data)
#  print(data.readlines())
import xlrd as xl

# data = open("C:/Users/ali hussain/Downloads/MCS_EAF.xls")

data = xl.open_workbook("C:/Users/ali hussain/Downloads/MCS_EAF.xls")
sheet = data.sheet_by_index(0)
print(sheet.cell_value(0, 0))
print(sheet.cell_value(0, 4))
print(sheet.cell_value(1, 4))
print(sheet.cell_value(2, 4))
print(sheet.cell_value(3, 4))
print(sheet.cell_value(4, 4))
print(sheet.cell_value(5, 4))
print(sheet.cell_value(6, 4))
print(sheet.cell_value(7, 4))


print('-----------------------------------  6th ex. xlsx file  ------------------------------------------------')
import openpyxl as opxl
data_3 = opxl.open('matches.xlsx')
print(data_3)
# Get workbook active sheet object
# from the active attribute
sheet = data_3.active
print(sheet)
# Cell objects also have a row, column,
# and coordinate attributes that provide
# location information for the cell.

# Note: The first row or
# column integer is 1, not 0.

# Cell object is created by using
# sheet object's cell() method.
cell_obj = sheet.cell(row=1, column=1)

# Print value of cell object
# using the value attribute

print(cell_obj.value)

cell_obj = sheet.cell(row=2, column=2)

# Print value of cell object
# using the value attribute

print(cell_obj.value)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ py file read  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
data_2 = open("02_write.py", encoding='utf8')
print(data_2)
# print(data_2.readlines())

for line_6 in data_2:
    print(line_6.strip().split('\n'))

print("***************************************************************************************************")
print(data_2.readlines())
