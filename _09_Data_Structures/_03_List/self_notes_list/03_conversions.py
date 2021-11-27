y = 10
x = str(y)
print("To str  : ", x, type(x))


str1 = 'Python World'
print("Convert to list : ", list(str1))


list1 = [19, 21, 34, 46, 59, 60]

print("List to string : ", list1, type(list1))

st = str(list1)
print("List to string : ", st, type(st))  # "[1, 2, 3, 4, 5, 6]"
"""
[1, 2, 3,  4 ,  5 ,   6]
012345678910 11 121314 15
"""
list1 = ['11', '22', '36', '48', '59', '63']
num_str = ''.join(list1)
print(num_str, type(num_str))

num_str = ' '.join(list1)
print(num_str, type(num_str))

num_str = '-'.join(list1)
print(num_str, type(num_str))

num_str = '='.join(list1)
print(num_str, type(num_str))
