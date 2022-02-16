def ret_pallindrome(num : str):
    a = 0
    outnum = [[], []]
    if len(num) % 2 == 0:
        a = 1
    dic1 = {}
    for i in num:
        if i not in dic1:
            dic1[i] = num.count(i)
    # print(dic1)
    if a == 1:
        for key, value in dic1.items():
            if value % 2 != 0:
                return -1
            else:
                for _ in range(value//2):
                    outnum[0].append(key)
                    outnum[1].append(key)
        outnum = outnum[0] + outnum[1][::-1]
        # print(outnum)
        return ''.join(outnum)
    if a == 0:
        temp_list = []
        for key, value in dic1.items():
            if value % 2 == 0:
                temp_list.append(True)
                for _ in range(value // 2):
                    outnum[0].append(key)
                    outnum[1].append(key)
            else:
                temp_list.append(False)
                key1 = key
                value1 = value
                # print(temp_list)
        outnum[0] += [key1*value1]
        if temp_list.count(False) > 1:
            return -1
        else:
            outnum = outnum[0] + outnum[1][::-1]
            # print(outnum)
            return ''.join(outnum)


print(ret_pallindrome('1122334455667777888990000'))

num = 1122334455667777888990000
st = str(num)
d = []
for i in st:
    d.append(i)

print(d)
poss = []
import itertools

for x in itertools.permutations(d):
    poss.append(x)

print(poss)

res = set([''.join(i) for i in poss])

# printing result
print("The list after conversion to list of string : " + str(res))

for i in res:
    if i[::-1] == st:
        print('p')
    else:
        print(-1)
