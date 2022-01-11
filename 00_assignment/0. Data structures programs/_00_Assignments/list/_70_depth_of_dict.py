"""
Get the depth of a dictionary
"""


# Python3 Program to find depth of a dictionary
def dict_depth(dic):
    str_dic = str(dic)
    counter = 0
    for i in str_dic:
        if i == "{":
            counter += 1
    return counter


# Driver code
dict1 = {1: 'Ali', 2: {3: {4: {}}}}
print(dict_depth(dict1))
