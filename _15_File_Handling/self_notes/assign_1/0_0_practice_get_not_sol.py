data = open("C:/Users/ali hussain/Downloads/phone_dataset - Copy.csv")
# print(data.readlines())
my_da_1 = []
my_da_2 = []
f_name = []
l_name = []
for line in data:
    w = line.strip().split(',')
    my_da_1.append(w[-1])
    my_da_2.append(w[-2])
    f_name.append(w[0])
    l_name.append(w[1])

# print(f_name)
# print(l_name)
# print(my_da_1)
# print(my_da_2)

d = [list(zip(my_da_1, my_da_2))]
# print(d)
s = str(my_da_1)
is_num = any(i.isdigit() for i in s)
if is_num:
    if s.isnumeric():
        print(s)

a = []
b = []
for i in my_da_1:
    # print(i)
    for j in my_da_2:
        is_num = any(chr(j.isdigit()))
        if is_num:
            #print(j)
            a.append(j)
        else:
            b.append(i)

# print(a)
# print(b)


# mobile number separation
my_data = ''
n = ' '
for line in data:
    my_data = line.strip()
    for i in my_data:
        for j in i:
            # print(j)
            if j.isnumeric():
                n += i


n = n.strip()
m = 10
p_num = [n[i:i+m] for i in range(0, len(n), m)]
print('-----------',p_num)

my_data = ''
n = ' '
p = []
for line in data:
    my_data = line.strip()
    for i in my_data:
        for j in i:
            # print(j)
            if j.isnumeric():
                n += i
            else:
                p.append(i)


b = ' '
c = []


for i in my_da_1:
    #print(i)
    for j in my_da_2:
        print(j)
    n_1 = 65
    n_2 = 122
    for a in range(n_1, n_2):
        if chr(a) in i:
            b.replace(i,chr(a))

print(b)
print(c)

n_1 = 65
n_2 = 122
for i in range(n_1,n_2):
    print(chr(i))

a = ' '
d = [my_da_1, my_da_2]
for i in str(d):
    # print(i)
    for j in i:
        if j.isnumeric():
            str(d).replace(i,j)

print(d)

z = lambda x, y: x + y
print('z(10, 11) :', z(10, 11))

import re

c_data = []


def processString3(txt_2):
    txt_2 = re.sub('[0-9,"()-]', '', txt_2)
    c_data.append(txt_2.strip())


# print(my_da_1)
# print(my_da_2)

result = list(map(lambda x, y: x + y, my_da_1, my_da_2))
# print(result)
for i in result:
    processString3(i)

print(c_data)
