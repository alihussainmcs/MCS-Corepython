# CRUD  ----- Retrieve
data = open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv")
# print(data.readlines())
my_da_1 = []
my_da_2 = []
f_name = []
l_name = []
# Separating the data
for line in data:
    w = line.strip().split(',')
    my_da_1.append(w[-1])
    my_da_2.append(w[-2])
    f_name.append(w[0])
    l_name.append(w[1])
import re

# fist name
fst_name = []


def processString2(txt_1):
    txt_1 = re.sub('["]', '', txt_1)
    fst_name.append(txt_1.strip())


for i in f_name:
    processString2(i)
# print(fst_name)


# city data
c_data = []

# function for replacing more than one characters from a list of string


def processString3(txt_2):
    txt_2 = re.sub('[0-9,"()-]', '', txt_2)
    c_data.append(txt_2.strip())


result = list(map(lambda x, y: x + y, my_da_1, my_da_2))
# print(result)
for i in result:
    processString3(i)

# print(c_data)

# mobile number separation
m_data = []
# function for replacing more than one characters from list of string


def processString4(txt_3):
    txt_3 = re.sub('[a-z,' 'A-Z"()-]', '', txt_3)

    m_data.append(txt_3.strip())


for i in result:
    processString4(i)

p_num = []
for i in m_data:
    p_num.append(i.replace(' ', ''))
# print(p_num)

# Combing all separate data like first name, last name, city details , phone number in one list
final_data = list(zip(fst_name, l_name, c_data, p_num))
# print(final_data)

# Creating a new txt file
a_data = open('phone_data1.csv', 'w')

for i in final_data:
    for j in i:
        a_data.write(j + ',')

    a_data.write('\n')
a_data.close()


# Creating a new csv file
a_data = open('phone_data.csv', 'w')

for i in final_data:
    a_data.write((re.sub('[()]', '', str(i))))
    a_data.write('\n')
a_data.close()

print('Execution done !')
