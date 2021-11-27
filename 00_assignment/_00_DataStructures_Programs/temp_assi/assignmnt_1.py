x = [1, 2, 3, "MCS", 4, "Software", 5, "Python", 6]

intList=sorted([i for i in x if type(i) is int])
strList=sorted([i for i in x if type(i) is str])
print(strList + intList)

























# 2
"""
def func(i):
    return isinstance(i, str), i

x = ['Tractor', 184 ,'Lada', 11 ,'Ferrari', 5 , 'Chicken' , 68]
x.sort(key=func)

for i in stuff:
    print(x)
"""