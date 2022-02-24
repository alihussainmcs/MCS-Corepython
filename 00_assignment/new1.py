li = [1, 1, 2, 3, 3, 2, 4, 5, 4, 5, 5]
li.sort()
print(li)
l1 = list(set(li))
print(l1)
"""for i in li:
    print(i)"""

for i in range(2, 6):
    print(i * li.count(i))


dict_of_counts = {item: li.count(item) for item in li}
print(dict_of_counts)


st1 = 'python world'


def reverseWordSentence(st):
    words = st.split(" ")

    newWords = [word[::-1] for word in words]

    newSentence = " ".join(newWords)

    return newSentence


print(reverseWordSentence(st1))

import re
add = '0000000000092000.000000168.000024'
ab = add.split('.')
c = ''
print(ab)
for i in ab:
    c += i.lstrip('0') +'.'
print(c)