"""
Convert String to List
"""

str1 = 'Python Engineer'


def str_to_list(s1):
    li = s1.split(' ')
    return li


print(f'After converting string to list - {str_to_list(str1)}')