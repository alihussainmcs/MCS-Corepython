original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

odd_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0}
print(odd_dict)
