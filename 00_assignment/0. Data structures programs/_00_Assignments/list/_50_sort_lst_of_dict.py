"""
Sort a list of nested dictionaries

"""

my_list = [{'key': {'sub key': 1}}, {'key': {'sub key': 10}}, {'key': {'sub key': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['sub key'], reverse=True)
print("Sorted List: ")
print(my_list)
