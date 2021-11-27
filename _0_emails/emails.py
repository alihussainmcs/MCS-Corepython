
with open('test.txt') as file_obj:
    data = file_obj.readlines()
    # print(data)
    di= {}
    for each in data:
        each = each.strip()
        each = each.split(" ")
        #print(' '.join(each[0:-1]))
        di[' '.join(each[0:-1])] = each[-1]
        #print(each[-1])
        #li3.append(each[-1])
    print(di)
    import collections
    di = collections.OrderedDict(sorted(di.items()))
    li = []
    for name,email in di.items():
        print(name)
        li.append(name)
    for name,email in di.items():
        print(email)
    print(li)