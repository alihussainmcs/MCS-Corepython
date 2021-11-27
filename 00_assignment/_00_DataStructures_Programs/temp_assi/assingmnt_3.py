# 1
import collections
string = 'karnataka'
results = collections.Counter(string)
print(results)

# 2
for i in string:

    print("%s" % i, string.count(i))

# 3
st = 'karnataka'
arr = [0]*256
for i in range(len(st)):
    if st[i] == ' ':
        continue
    num = ord(st[i])
    arr[num] += 1
print("Repeated character in a string are:")
for i in range(256):
    if arr[i] > 0:
        print(chr(i), " occurs ", arr[i], " times")
