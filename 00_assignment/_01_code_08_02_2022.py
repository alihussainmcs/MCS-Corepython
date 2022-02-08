num = 121
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
